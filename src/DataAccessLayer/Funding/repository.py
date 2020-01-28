from DataAccessLayer.BaseRepository import BaseRepository

class FundingRepository(BaseRepository):

    def doesBeneficiaryExist(self, beneficiaryId, fundingGroupId):
        return self.model.objects.filter(beneficiary=beneficiaryId, fundingGroup=fundingGroupId).exists()
