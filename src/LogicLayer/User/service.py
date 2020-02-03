from DataAccessLayer.DataModule import DataModule
from DataAccessLayer.User.serializer import UserSerializer
from DataAccessLayer.User.signupSerializer import SignupSerializer
from Utility.Requests import Request
from Utility.Response import Response
from Utility.jwt import Jwt
from Utility.logger import Logger
from DataAccessLayer.User.loginSerializer import LoginSerializer
import json
import uuid
import os


ums_secret = os.environ.get('UMS_SECRET')
ums_url = os.environ.get('UMS_URL')
jwt_secret = os.environ.get('JWT_SECRET')

class UserService:
    

    def __init__(self):
        self.data = DataModule()
        self.logger = Logger('LogicLayer.UserService')

    def createUser(self, data, clientSecret):
        
        requestId = uuid.uuid4()
        try:
            validData = SignupSerializer(data=data)
            if not validData.is_valid():
                self.logger.Info(r"User signup. Failed validation with: {}, n\ REQUESTID => {}".format(str(validData.errors), requestId))
                return Response.error(requestId, message="Validation error occured processing request", error=validData.errors, responseCode='01'),400
            
            if clientSecret is None:
                return Response.error(requestId, error="Invalid Access Token",responseCode="01"),401

            if self.data.userRepository.checkPhoneNumberExist(data['phoneNumber']):
                self.logger.Info(r"User with details --> {} already exists. Phone number duplication, n\ REQUESTID => {}".format(data, requestId))
                return Response.error(requestId, error="Integrity error. User with Identity exists.", responseCode='01'),409

            headers = {'client-secret': clientSecret,'Content-Type': 'application/json'}
            formatedData = {('mobileNumber' if key == 'phoneNumber' else key): value for (key, value) in data.items()}
            response = Request.post(ums_url+"/account/signup", json.dumps(formatedData), headers=headers)            
            
            if 'data' not in response:  
                if 'status' in response:             
                    self.logger.Info(r"Bad request to UMS --> with error {} , n\ REQUESTID => {}".format(data, requestId))
                    return Response.error(requestId, error="Bad request. An error occured. "+str(response['errors']),responseCode="01"),400
            elif response['data'] is None:
                self.logger.Info(r"User with data --> {} could not be onboarded on UMS, n\ requestId => {}".format(formatedData, requestId))
                return Response.error(requestId, error=response['responseMessage'], responseCode='01'),400

            decodedResponse = Jwt.DecodeJWT(response['data']['token'], ums_secret)
            decapitalizedDecodedResponse = {(key[0].lower()+key[1:]): value for (key, value) in json.loads(decodedResponse['actort']).items()}

            if 'id' not in decapitalizedDecodedResponse.keys():
                self.logger.Info(r"User token --> {} did not contain an id, n\ REQUESTID => {}".format(response['data']['token'], requestId))
                return Response.error(requestId, error="Unauthorized. Failed to create new user "+response['responseMessage']),401
            
            userData = self.__pickUserData(data)
            userData['userId'] = decapitalizedDecodedResponse['id']
            savedUser = self.data.userRepository.create(userData)
            token = Jwt.EncodeJWT({'id': str(savedUser.id), 'roleName': decapitalizedDecodedResponse['roleName']}, jwt_secret)
            
            self.logger.Info(r"User with data --> {} was successfully onboarded, n\ REQUESTID => {}".format(formatedData, requestId))
            savedUserSerializer = UserSerializer(savedUser, many=False).data
            savedUserSerializer['token'] = token
            return Response.success(requestId, data=savedUserSerializer),201
        except ValueError as err:
            self.logger.Info(r"Unknown Client Access. Invalid client-secret ({}) with error {} n\ REQUESTID => {}".format(clientSecret,str(err),requestId))
            return Response.error(requestId,error="Invalid Client Secret.", responseCode="02"),401   
        except BaseException as ex:
            self.logger.Error("RequestID =>{} ERROR => {}".format(requestId,ex))
            return Response.error(requestId, error=str(ex)),500

    def verifyUser(self, data, clientSecret):
        requestId = uuid.uuid4()
        try:
            validData = LoginSerializer(data=data)
            if not validData.is_valid():
                self.logger.Info(r"User Login. Failed validation with: {}, n\ REQUESTID => {}".format(str(validData.errors), requestId))
                return Response.error(requestId, error=validData.errors),400

            formatedData = {('mobileNumber' if key == 'phoneNumber' else key): value for (key, value) in data.items()}
            response = Request.post(ums_url+"/account/signin",json.dumps(formatedData),headers={"Content-Type": "application/json", "client-secret": clientSecret})
            self.logger.Info(ums_url)
            if 'data' not in response:
                if 'status' in response:             
                    self.logger.Info(r"Bad request to UMS --> with error {} , n\ REQUESTID => {}".format(data, requestId))
                    return Response.error(requestId, error=response['errors'],responseCode="01"),400           
            elif response['data'] is None:
                self.logger.Info(r"The user with details: {} could not be authenticated, \n REQUESTID => {}".format(formatedData, requestId))
                return Response.error(requestId, message=response["responseMessage"], error={"auth" : response["responseMessage"]}, responseCode='01'),401


            decodedToken = Jwt.DecodeJWT(response["data"]["token"], ums_secret)
            payload = json.loads(decodedToken["actort"])
            user = self.data.userRepository.getByUserId(payload["id"])[0]

            token = Jwt.EncodeJWT({"id": str(user.id), "roleName": str(payload["roleName"])},jwt_secret)

            userSerializer = UserSerializer(user, many=False).data
            userSerializer['token'] = token
            self.logger.Info(r"User with details --> {} was successfully logged in, \n REQUESTID --> {}".format(payload, requestId))
        except ValueError as err:
            self.logger.Info(r"Unknown Client Access. Invalid client-secret ({}) with error {} n\ REQUESTID => {}".format(clientSecret,str(err),requestId))
            return Response.error(requestId,error="Invalid Client Secret.", responseCode="02"),401       
        except Exception as ex:
            self.logger.Error("RequestID =>{} ERROR => {}".format(requestId,ex))
            return Response.error(requestId, error=str(ex)),500        
        
        return Response.success(requestId, data=userSerializer),200

    def __pickUserData(self, data):
        userSerializerDataKeys = ['firstName', 'lastName', 'phoneNumber']
        UserSerializerData = {key:data[key] for key in userSerializerDataKeys}
        return UserSerializerData
