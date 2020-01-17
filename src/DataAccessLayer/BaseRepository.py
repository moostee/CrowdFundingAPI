class BaseRepository:
    def __init__(self, model):
        self.model = model

    def getAll(self):
        return self.model.objects.filter(isDeleted=False)

    def getOne(self, primaryKey):
        return self.model.objects.get(pk=primaryKey, isDeleted=False)

    def update(self, serializeData, primaryKey):
        return self.model.objects.filter(id=primaryKey).update(**serializeData)

    def delete(self, primaryKey):
        return self.model.objects.filter(id=primaryKey).update(isDeleted=True)

    def create(self, validatedData):
        return self.model.objects.create(**validatedData)

    def IsExists(self, pk):
        return self.model.objects.filter(id=pk, isDeleted=False).exists()
