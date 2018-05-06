import suds
import os, time, sys, uuid
from datetime import datetime
import pymssql
from pymssql import Cursor
import openpyxl
from openpyxl import workbook

from suds.client import Client
from suds.sax.text import Raw
from suds.plugin import MessagePlugin

class ISAIM_auto:
    "This class automates the creation of meter and validating the same in database as well"

    #Initiate everything
    def __init__(self, url):
        self.url = url
        self.client = Client(url)
        #print(self.client)
        self.dict_parse = {}
        self.dataMH = ""
        self.dataUtil = ""
    #Parse the method
    def parse(self):
        ##Fetch from Excel
        os.chdir("C:\\Mouli\\Personal\\PythonPrac\\Excel\\")
        self.wb = openpyxl.load_workbook("ISAIM_DataInput.xlsx")

        ##Load Message header
        UUID = lambda: int(round(time.time()*1000))
        CreationDateTime = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
        print(UUID())
        print(CreationDateTime)
        print(datetime.utcnow().strftime('%Y%m%d-(%H-4)%M%S%f')[:-3])
        self.sheetMH = self.wb.get_sheet_by_name("MessageHeader")

        for x in self.sheetMH['A1':'C3']:
            for y in x:
                if(str(y.value)=='None'):
                    break
                elif(str(y.value)=='CreationDateTime'):
                    self.dataMH += CreationDateTime
                elif(str(y.value)=='UUID'):
                    self.dataMH += str(UUID())
                else:
                    self.dataMH += str(y.value)
            self.dataMH+="\n"
        print("Message Header:\n" + self.dataMH)

        ##Load main data from Excel
        self.sheet = self.wb.get_sheet_by_name("UtilsDvceERPSmrtMtrCrteReqMsg")

        for i in self.sheet['A1':'C9']:
            for j in i:
                if (str(j.value) == 'None'):
                    break
                else:
                    self.dataUtil += str(j.value)
            self.dataUtil += "\n"

        print("Util Device:\n" + self.dataUtil)
        print("Parsing the method...")
        parseMethod = self.client.factory.create("ns0:UtilsDvceERPSmrtMtrCrteReqMsg")
        dict_parse = dict(parseMethod)
        #print(dict_parse.keys())
        #print(dict_parse.values())
        return dict_parse

    #Pack the data and send it.
    def PackNsend(self, dict_parse):
        self.dict_parse['MessageHeader'] = Raw(self.dataMH)
        self.dict_parse['UtilitiesDevice'] = Raw(self.dataUtil)
        sendingData = self.client.service.UtilitiesDeviceERPSmartMeterCreateRequest_In(self.dict_parse['MessageHeader'], self.dict_parse['UtilitiesDevice'])
        print("Parsed and sent the data to webservice...")
    #Check the database for the task and meter getting created.
    def DBcheck(self):
        print("Entering DB zone...")
        self.cnxn = pymssql.connect("RAL-redwood-DB1.itronhdc.com\ARTPILOT", "sa", "Meterguy1", "ItronEE")
        self.db_cursor = self.cnxn.cursor(as_dict=True)
        time.sleep(10)
        self.db_cursor.execute("select * from Meter where MeterID='AutoMeter_010'")
        try:
            self.rows = dict(self.db_cursor.fetchone())
        except TypeError:
            print("Meter not yet added... wait a while...\n")
            self.cnxn.close()
            time.sleep(10)
            self.DBcheck()

        if self.rows['MeterID'] == "AutoMeter_010":
            print("Meter Added successfully!!!")
        else:
            print("Meter not added :( ")
        self.cnxn.close()
    # Check the IEESAPConfirmation folder for the response file.

WSDL_address = "http://ral-skeena.itronhdc.com:8000/V1/IEESAPAdapter?wsdl"
ISAIM = ISAIM_auto(WSDL_address)
inputXML = ISAIM.parse()
ISAIM.PackNsend(inputXML)
ISAIM.DBcheck()