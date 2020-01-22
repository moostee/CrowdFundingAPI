from DataAccessLayer.Role.serializer import RoleSerializer
from DataAccessLayer.DataModule import DataModule
from Utility.Response import Response
from Utility.Utility import Utility
from Utility.logger import Logger
import uuid
from django.db import IntegrityError

class RoleService:
    def __init__(self):
        self.data = DataModule()
        self.logger = Logger('Logiclayer.RoleService')

    def createRole(self,data):
        requestId = uuid.uuid4()
        try:
            validData = RoleSerializer(data=data)
            if not validData.is_valid():
                self.logger.Info(r"Role with data \"{}\" could not be validated  with error {} n\ REQUESTID => {}".format(data,validData.errors,requestId))
                return Response.error(requestId, error=validData.errors, responseCode='01')

            if 'name' in data: formattedData = Utility.convertFieldValueToLowerCase(data, 'name')
            savedRole = self.data.roleRepository.create(formattedData)
            self.logger.Info(r"Role with name --> {} was successfully created, n\ REQUESTID => {}".format(data['name'],requestId))
            return Response.success(requestId, data=RoleSerializer(savedRole,many=False).data)
        except IntegrityError:
            self.logger.Info(r"Role with name --> {} was not created. Role already exist. n\ REQUESTID => {}".format(data['name'],requestId))
            return Response.error(requestId, error=r"{} role already exist".format(data['name']), responseCode='01')
        except BaseException as ex:
            self.logger.Info(r"Role with name --> {} was not created. An exception occured: {}, n\ REQUESTID => {}".format(data['name'],str(ex),requestId))
            return Response.error(requestId, error=str(ex))

    def getAllRoles(self):
        requestId = uuid.uuid4()
        try:
            data = self.data.roleRepository.getAll()
            self.logger.Info(r"Successfully fetched all roles, requestId --> {}".format(requestId))
            return Response.success(requestId, data=RoleSerializer(data, many=True).data)
        except Exception:
            self.logger.Info(r"Unable to fetch all roles due to exception--> {}, requestId --> {}".format(str(Exception), requestId))
            return Response.error(requestId, error=str(Exception))

    def getOneRole(self, pk):
        requestId = uuid.uuid4()
        try:
            if self.data.roleRepository.IsExists(pk):
                role = self.data.roleRepository.getOne(pk)
                self.logger.Info(r"Successfully fetched role with id --> {}, requestId --> {}".format(pk, requestId))
                return Response.success(requestId, data=RoleSerializer(role).data)
            else:
                self.logger.Info(r"Role with id --> {} was not found, requestId --> {}".format(pk, requestId))
                return Response.error(requestId, error="Role does not exist", responseCode="03")
        except Exception:
            self.logger.Info(r"Unable to fetch role with id --> {} due to exception--> {}, requestId --> {}".format(pk, str(Exception), requestId))
            return Response.error(requestId, error=str(Exception))

    def updateRole(self, data, pk):
        requestId = uuid.uuid4()
        try:
            if self.data.roleRepository.IsExists(pk):
                updatedRole = self.data.roleRepository.update(data, pk)
                self.logger.Info(r"Successfully updated role with id --> {}, requestId --> {}".format(pk, requestId))
                return Response.success(requestId, data=RoleSerializer(updatedRole, many=False).data, message="Role name successfully updated")
            else:
                self.logger.Info(r"Role with id --> {} was not found, requestId --> {}".format(pk, requestId))
                return Response.error(requestId, error="Role does not exist", responseCode="03")
        except BaseException as ex:
            self.logger.Info(r"Unable to update role with id --> {} due to exception--> {}, requestId --> {}".format(pk, str(Exception), requestId))
            return Response.error(requestId, error=str(ex))

    def deleteRole(self, pk):
        requestId = uuid.uuid4()
        try:
            if self.data.roleRepository.IsExists(pk):
                self.data.roleRepository.delete(pk)
                self.logger.Info(r"Successfully deleted role with id --> {}, requestId --> {}".format(pk, requestId))
                return Response.success(requestId, message="Role name successfully deleted")
            else:
                self.logger.Info(r"Role with id --> {} was not found, requestId --> {}".format(pk, requestId))
                return Response.error(requestId, error="Role does not exist", responseCode="03")
        except Exception:
            self.logger.Info(r"Unable to delete role with id --> {} due to exception--> {}, requestId --> {}".format(pk, str(Exception), requestId))
            return Response.error(requestId, error=str(Exception))
    
        