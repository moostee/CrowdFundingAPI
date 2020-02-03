from DataAccessLayer.BaseRepository import BaseRepository

class BeneficiarySourceRepository(BaseRepository):
    

    def HasBeneficiarySource(self,userId):
        return self.GetUserBeneficiarySource(userId).exists()
    
    def GetUserBeneficiarySource(self,userId):
        return self.model.objects.filter(user_id=userId,isDeleted=False)

    def GetOneBeneficiaryUserSource(self,userId,primaryKey):
        return self.model.objects.filter(id=primaryKey,user_id=userId,isDeleted=False)

    def DeleteUserBeneficiarySource(self,userId,primaryKey):
        return self.GetOneBeneficiaryUserSource(userId,primaryKey).update(isDeleted=True)

    def CheckUserIsTiedToBeneficiarySource(self,userId,primaryKey):
        return self.GetOneBeneficiaryUserSource(userId,primaryKey).exists()
    
    def CheckIfUserDestinationAccountExists(self,issuerId,beneficiarySourceTypeId,destinationNumber):
        return self.model.objects.filter(issuer_id=issuerId,beneficiarySourceType_id=beneficiarySourceTypeId,destinationNumber=destinationNumber,isDeleted=False).exists()