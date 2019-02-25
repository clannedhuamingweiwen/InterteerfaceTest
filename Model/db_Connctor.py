#coding:utf-8
import DB
from Settings import sql
import unittest


class db(DB.dbutils):

    def __init__(self):
        pass

    @staticmethod
    def query(sql):
        return DB.dbutils.query()


#(仅供测试用途)
# class db_test(unittest.TestCase):
#
#     def setUp(self):
#         pass
#
#     def test01(self):
#         data =DB.mysql.db_Operator(sql.SQL_SELECT["g"])
#         print data
#         return data
#
#
#
#
# if __name__ == '__main__':
#
#     case_Name ="test01"
#     suite =unittest.TestSuite()
#     suite.addTest(db_test(case_Name))
#
#     runner=unittest.TextTestRunner()
#
#     runner.run(suite)
#
#
#





