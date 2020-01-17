from DataAccessLayer.DataModule import DataModule
from DataAccessLayer.User.serializer import UserSerializer
from Utility.Requests import Request
from Utility.Response import Response
from Utility.jwt import Jwt
from Utility.logger import Logger

import uuid
import json
import environ

env = environ.Env()
environ.Env.read_env()

class UserService:
    def __init__(self):
        self.data = DataModule()
        self.logger = Logger('LogicLayer.UserService')

    def createUser(self,data,client_secret):
        requestId = uuid.uuid4()
        try:
            headers = {'client-secret': client_secret, 'Content-Type': 'application/json'}
            formatedData = {('mobileNumber' if key == 'phoneNumber' else key):value for (key,value) in data.items()}
            response = Request.post(env('UMS_URL')+"/account/signup", json.dumps(formatedData), headers=headers)
            if not response['data']:
                self.logger.Info(r"User with mobile number --> {} could not be onboarded on UMS, n\ REQUESTID => {}".format(formatedData['mobileNumber'],requestId))
                return Response.error(requestId, error=response['responseMessage'], responseCode='01')
            decodedResponse = Jwt.DecodeJWT(response['data']['token'], env('UMS_SECRET'))
            decapitalizedDecodedResponse = {(key[0].lower()+key[1:]):value for (key, value) in json.loads(decodedResponse['actort']).items()}

            if 'id' not in decapitalizedDecodedResponse.keys():
                self.logger.Info(r"User token --> {} did not contain an id, n\ REQUESTID => {}".format(response['data']['token'],requestId))
                return Response.error(requestId, error="Failed to create new user "+response['responseMessage'])
            data['userId'] = decapitalizedDecodedResponse['id']
            savedUser = self.data.userRepository.create(data)
            token = Jwt.EncodeJWT({'id': str(savedUser.id), 'roleName': decapitalizedDecodedResponse['roleName']}, env('JWT_SECRET'))
            self.logger.Info(r"User with mobile number --> {} was successfully onboarded, n\ REQUESTID => {}".format(formatedData['mobileNumber'],requestId))
            return Response.success(requestId, data={"user":UserSerializer(savedUser,many=False).data, "token":token})
        except BaseException as ex:
            self.logger.Info(r"User with mobile number --> {} could not be onboarded. An exception occured: {}, n\ REQUESTID => {}".format(formatedData['mobileNumber'],str(ex),requestId))
            return Response.error(requestId, error=str(ex))
