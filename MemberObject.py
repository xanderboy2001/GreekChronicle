class MemberObject():

    def __init__(self,member_id,name,big,mentor_id,bdate,join_date):
        self._memberid = member_id
        self._name=name
        self._big = big
        self._mentorid = mentor_id
        self._bdate = bdate
        self._joindate = join_date

    def __str__(self):
        return str(self._memberid) + str(self._name) + str(self._big)+ str(self._mentorid) + str(self._bdate) + str(self._joindate)

    def getMemberId(self):
        return self._memberid
    
    def getName(self):
        return self._name

    def getBig(self):
        return self._big

    def getMentorId(self):
        return self._mentorid

    def getBdate(self):
        return self._bdate
    
    def getJoinDate(self):
        return self._joindate
