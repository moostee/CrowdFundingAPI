from DataAccessLayer.BaseRepository import BaseRepository

class RoleRepository(BaseRepository):
    def getAdmin(self):
        return self.model.objects.get(name='admin', isDeleted=False)