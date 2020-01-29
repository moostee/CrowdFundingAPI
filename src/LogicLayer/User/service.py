from DataAccessLayer.DataModule import DataModule
from DataAccessLayer.User.serializer import UserSerializer
from DataAccessLayer.User.signupSerializer import SignupSerializer
from Utility.Requests import Request
from Utility.Response import Response
from Utility.jwt import Jwt
from Utility.logger import Logger
import json
import environ
import uuid

env = environ.Env()
environ.Env.read_env()


class UserService:

    def __init__(self):
        self.data = DataModule()
        self.logger = Logger('LogicLayer.UserService')
        self.requestId = uuid.uuid4()

    def createUser(self, data, client_secret):
        try:
            validData = SignupSerializer(data=data)
            if not validData.is_valid():
                self.logger.Info(r"User signup. Failed validation with: {}, n\ REQUESTID => {}".format(str(validData.errors), self.requestId))
                return Response.error(self.requestId, message="Validation error occured processing request", error=validData.errors, responseCode='01'),400
            
            headers = {'client-secret': client_secret,'Content-Type': 'application/json'}
            formatedData = {('mobileNumber' if key == 'phoneNumber' else key): value for (key, value) in data.items()}
            response = Request.post(env('UMS_URL')+"/account/signup", json.dumps(formatedData), headers=headers)
            
            if not response['data']:
                self.logger.Info(r"User with data --> {} could not be onboarded on UMS, n\ requestId => {}".format(formatedData, self.requestId))
                return Response.error(self.requestId, error=response['responseMessage'], responseCode='01'),400
            
            decodedResponse = Jwt.DecodeJWT(response['data']['token'], env('UMS_SECRET'))
            decapitalizedDecodedResponse = {(key[0].lower()+key[1:]): value for (key, value) in json.loads(decodedResponse['actort']).items()}

            if 'id' not in decapitalizedDecodedResponse.keys():
                self.logger.Info(r"User token --> {} did not contain an id, n\ REQUESTID => {}".format(response['data']['token'], self.requestId))
                return Response.error(self.requestId, error="Unauthorized. Failed to create new user "+response['responseMessage']),401
            
            userData = self.__pickUserData(data)
            userData['userId'] = decapitalizedDecodedResponse['id']
            savedUser = self.data.userRepository.create(userData)
            token = Jwt.EncodeJWT({'id': str(savedUser.id), 'roleName': decapitalizedDecodedResponse['roleName']}, env('JWT_SECRET'))
            
            self.logger.Info(r"User with data --> {} was successfully onboarded, n\ REQUESTID => {}".format(formatedData, self.requestId))
            savedUserSerializer = UserSerializer(savedUser, many=False).data
            savedUserSerializer['token'] = token
            return Response.success(self.requestId, data=savedUserSerializer),201
        except BaseException as ex:
            self.logger.Info(r"User with data --> {} could not be onboarded. An exception occured: {}, n\ REQUESTID => {}".format(formatedData, str(ex), self.requestId))
            return Response.error(self.requestId, error=str(ex)),500

    def verifyUser(self, data, clientSecret):
        try:
            formatedData = {('mobileNumber' if key == 'phoneNumber' else key): value for (
                key, value) in data.items()}
            response = Request.post(
                env('UMS_URL')+"/account/signin",
                json.dumps(formatedData),
                headers={"Content-Type": "application/json", "client-secret": clientSecret})
            if response['data']:
                if ('token' in response["data"]):
                    decodedToken = Jwt.DecodeJWT(
                        response["data"]["token"], env('UMS_SECRET'))
                    payload = json.loads(decodedToken["actort"])
                    user = self.data.userRepository.getByUserId(payload["id"])[
                        0]
                    if user:
                        token = Jwt.EncodeJWT(
                            {"id": str(user.id), "roleName": str(
                                payload["roleName"])},
                            env('JWT_SECRET')
                        )
            else:
                self.logger.Info(
                    r"The user with details: {} could not be authenticated, \n REQUESTID => {}".format(formatedData, self.requestId))
                return Response.error(self.requestId, message=response["responseMessage"], error=response["responseMessage"], responseCode='02'),401
        except Exception as exception:
            self.logger.Info(
                r"User with detials --> {} could not be onboarded, An exception occured: {},  \n REQUESTID --> {}".format(formatedData, str(exception), self.requestId))
            return Response.error(self.requestId, error=str(exception)),500
        self.logger.Info(
            r"User with details --> {} was successfully logged in, \n REQUESTID --> {}".format(payload, self.requestId))
        userSerializer = UserSerializer(user, many=False).data
        userSerializer['token'] = token
        return Response.success(self.requestId, data=userSerializer),200

    def __pickUserData(self, data):
        userSerializerDataKeys = ['firstName', 'lastName', 'phoneNumber']
        UserSerializerData = {key:data[key] for key in userSerializerDataKeys}
        return UserSerializerData
        # userSerializerData = {('mobileNumber' if key == 'phoneNumber' else key): value for (key, value) in data.items()}