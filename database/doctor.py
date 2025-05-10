import sqlite3

class Doctor():
    def __init__(self):
        self._tableName = 'DOCTOR'
        self._columns = {"name" : "NAME", 
                         "speciality" : "SPECIALITY",
                         "phone" : "PHONE",
                         "email" : "EMAIL" }

    def getColumnName(self):
        return self._columns

    def createSqlStatement(self):
        return f"""create table if not exists {self._tableName}(
            {self._columns["name"]} text,
            {self._columns["speciality"]} text,
            {self._columns["phone"]} text,
            {self._columns["email"]} text);
        """
    
    def insertSqlStatement(self, doctorDict):
        name = doctorDict["name"]
        speciality = doctorDict["speciality"]
        phone = doctorDict["phone"]
        email = doctorDict["email"]

        return f"""insert into {self._tableName} values(
            '{name}',
            '{speciality}',
            '{phone}',
            '{email}');
        """
    
    def readAllSqlStatement(self):
        return f"""select * from {self._tableName};"""
    
    def readByIdSqlStatement(self, id):
        return f"""select * from {self._tableName}
            where id={id};
        """
    
    def updateByIdSqlStatement(self, id, doctorDict):
        name = doctorDict['name']
        speciality = doctorDict['speciality']
        phone = doctorDict['phone']
        email = doctorDict['email']

        return f"""update {self._tableName}
            set {self._columns["name"]}={name},
                {self._columns["speciality"]}={speciality},
                {self._columns["phone"]}={phone},
                {self._columns["email"]}={email}
            where id={id};
        """
    
    def deleteByIdSqlStatement(self, id):
        return f"""delete from {self._tableName}
            where id={id};
        """