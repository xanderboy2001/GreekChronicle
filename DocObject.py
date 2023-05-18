class DocObject():

    def __init__(self,id,name,location,create_date,modify_date):
        self._id = id
        self._name=name
        self._location = location
        self._create_date = create_date
        self._modify_date = modify_date

    def __str__(self):
        return str(self._id) + str(self._name) + str(self._location)+ str(self._create_date) + str(self._modify_date)

    def getName(self):
        return self._name
    
    def getId(self):
        return self._id

    def getLocation(self):
        return self._location

    def getCreateDate(self):
        return self._create_date

    def getModifyDate(self):
        return self._modify_date

    def setName(self,name):
        self._name=name
    
    def setId(self,id):
        self._id = id

    def setLocation(self,location):
        self._location = location

    def setCreateDate(self,create_date):
        self._create_date = create_date

    def setModifyDate(self,modify_date):
        self._modify_date = modify_date
