import suds
import os
import re
import openpyxl
from openpyxl import workbook

from suds.client import Client
from suds.sax.text import Raw

class FetchReqs:
    "Fetch all requests"
    def __init__(self, url):
        self.url = url
        self.client = Client(url)
        self.data = self.client
        #print(self.data)
        self.dict_parse = {}

    def xl(self):
        os.chdir("D:\\Personal\\PythonPrac\\Excel\\")
        self.wb = openpyxl.load_workbook("Study01.xlsx")
        print(self.wb.get_sheet_names())

    def parseMethod(self):
        print("Parsing the method...")
        parseMethod = self.client.factory.create("ns0:UtilsDvceERPSmrtMtrRegCrteReqMsg")
            #UtilsDvceERPSmrtMtrCrteReqMsg
            #("ns0:UtilsDvceERPSmrtMtrCrteReqUtilsDvce")
        dict_parse = dict(parseMethod)
        print(dict_parse.keys())
        print(dict_parse.values())
        return dict_parse

Fetchit = FetchReqs("http://ral-skeena.itronhdc.com:8000/V1/IEESAPAdapter?wsdl")
Fetchit.xl()
Fetchit.parseMethod()
