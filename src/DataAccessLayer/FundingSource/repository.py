from DataAccessLayer.BaseRepository import BaseRepository

class FundingSourceRepository(BaseRepository):
    
    def HasFundingSource(self,usersId):
        return self.GetUserFundingSource(usersId).exists()
    
    def GetUserFundingSource(self,usersId):
        return self.model.objects.filter(userId=usersId,isDeleted=False)