from DataAccessLayer.BaseRepository import BaseRepository


class UserRepository(BaseRepository):

    def getByUserId(self, value):
        return self.model.objects.filter(userId=value, isDeleted=False)
