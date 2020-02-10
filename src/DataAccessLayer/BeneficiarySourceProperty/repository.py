from DataAccessLayer.BaseRepository import BaseRepository

class BeneficiarySourcePropertyRepository(BaseRepository):
    def DeleteByBeneficiarySourceId(self,beneficiarySourceId):
        return self.model.objects.filter(beneficiarySource_id=beneficiarySourceId).update(isDeleted=True)