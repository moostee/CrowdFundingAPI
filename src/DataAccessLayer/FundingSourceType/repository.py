from DataAccessLayer.BaseRepository import BaseRepository

class FundingSourceTypeRepository(BaseRepository):
    def SaveFundingSourceType(self, name, config):
        return self.model.objects.create(name=name, config=config)