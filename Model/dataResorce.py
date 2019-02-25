from Model import DB
from Settings import sql






class DataInputstream(DB.mysql):
    def __init__(self):
        pass
    @staticmethod
    def get_sid():
        return DB.dbutils.query(sql.SQL_SELECT["get_id"])


    def get_Max(self):
        pass











