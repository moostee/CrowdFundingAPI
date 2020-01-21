from DataAccessLayer.DataModule import DataModule
from DataAccessLayer.User.serializer import UserSerializer
from Utility.Requests import Request
from Utility.Response import Response
from Utility.jwt import Jwt
from DataAccessLayer.User.loginSerializer import LoginSerializer
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

    def createUser(self, data, client_secret):
        requestId = uuid.uuid4()
        try:
            headers = {'client-secret': client_secret,
                       'Content-Type': 'application/json'}
            formatedData = {('mobileNumber' if key == 'phoneNumber' else key): value for (
                key, value) in data.items()}
            response = Request.post(
                env('UMS_URL')+"/account/signup", json.dumps(formatedData), headers=headers)
            if not response['data']:
                self.logger.Info(r"User with mobile number --> {} could not be onboarded on UMS, n\ REQUESTID => {}".format(
                    formatedData['mobileNumber'], requestId))
                return Response.error(requestId, error=response['responseMessage'], responseCode='01')
            decodedResponse = Jwt.DecodeJWT(
                response['data']['token'], env('UMS_SECRET'))
            decapitalizedDecodedResponse = {(key[0].lower(
            )+key[1:]): value for (key, value) in json.loads(decodedResponse['actort']).items()}

            if 'id' not in decapitalizedDecodedResponse.keys():
                self.logger.Info(r"User token --> {} did not contain an id, n\ REQUESTID => {}".format(
                    response['data']['token'], requestId))
                return Response.error(requestId, error="Failed to create new user "+response['responseMessage'])
            data['userId'] = decapitalizedDecodedResponse['id']
            savedUser = self.data.userRepository.create(data)
            token = Jwt.EncodeJWT({'id': str(
                savedUser.id), 'roleName': decapitalizedDecodedResponse['roleName']}, env('JWT_SECRET'))
            self.logger.Info(r"User with mobile number --> {} was successfully onboarded, n\ REQUESTID => {}".format(
                formatedData['mobileNumber'], requestId))
            return Response.success(requestId, data={"user": UserSerializer(savedUser, many=False).data, "token": token})
        except BaseException as ex:
            self.logger.Info(r"User with mobile number --> {} could not be onboarded. An exception occured: {}, n\ REQUESTID => {}".format(
                formatedData['mobileNumber'], str(ex), requestId))
            return Response.error(requestId, error=str(ex))

    def verifyUser(self, data, clientSecret):
        requestId = uuid.uuid4()

        try:
            formatedData = {('mobileNumber' if key == 'phoneNumber' else key): value for (
                key, value) in data.items()}
            response = Request.post(
                env('UMS_URL')+"/account/signin",
                json.dumps(formatedData),
                headers={"Content-Type": "application/json", "client-secret": clientSecret})
            if 'data' in response:
                if ('token' in response["data"]):
                    decodedToken = Jwt.DecodeJWT(
                        response["data"]["token"], env('UMS_SECRET'))
                    payload = json.loads(decodedToken["actort"])
                    user = self.data.userRepository.getByUserId(payload["id"])[
                        0]
                    if user:
                        token = Jwt.EncodeJWT(
                            {"userId": str(user.id), "roleName": str(
                                payload["roleName"])},
                            env('JWT_SECRET')
                        )
            else:
                self.logger.Info(
                    r"The user with mobile number {} could not be authenticated, \n REQUESTID => {}".format(formatedData['mobileNumber'], requestId))
                return Response.error(requestId, error=response["message"], responseCode='02')
        except Exception as exception:
            self.logger.Info(
                r"User with mobile number --> {} could not be onboarded, An exception occured: {},  \n REQUESTID --> {}".format(formatedData["mobileNumber"], str(exception), requestId))
            return Response.error(requestId, error=str(exception))
        self.logger.Info(
            r"User with mobile number --> {} was successfully logged in, \n REQUESTID --> {}".format(payload["mobileNumber"], requestId))
        return Response.success(requestId, data={"token": token, "user": LoginSerializer(user, many=False).data})
