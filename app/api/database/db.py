from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi



class Database():
    def __init__(self,password,database):
        self.uri = f"mongodb+srv://hamxa:{password}@cluster0.rkwyhgm.mongodb.net/?retryWrites=true&w=majority"
        self.client = MongoClient(self.uri, server_api=ServerApi('1'))

        self.db=self.client.get_database(database)
        self.record = self.db.verification_records
        self.userRecord = self.db.admins
    def writeRecords(self,data):
        self.record.insert_one(data)

    def read(self,query):
        data= self.record.find_one(query)
        return data
    def checkAdmin(self,Username,Password):
        data=self.userRecord.find_one({"Username":Username})

        if data==None:
            return False,1

        if data["Password"] != Password:
           return False,2
        return True,0
