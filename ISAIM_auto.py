import suds
import os, time
import sys, uuid
import datetime
import pymssql

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

    #Parse the method
    def parse(self):
        print("Parsing the method...")
        parseMethod = self.client.factory.create("ns0:UtilsDvceERPSmrtMtrCrteReqMsg")
        dict_parse = dict(parseMethod)
        #print(dict_parse.keys())
        #print(dict_parse.values())
        return dict_parse

    #Pack the data and send it.
    def PackNsend(self, dict_parse):
        self.dict_parse['MessageHeader'] = Raw('''<UUID>SUDS8999124-8c76-61c2345612317212</UUID><CreationDateTime>2017-01-04T17:39:24Z</CreationDateTime>
                                               <SenderBusinessSystemID>SapDefaultSystem</SenderBusinessSystemID> ''')
        self.dict_parse['UtilitiesDevice'] = Raw('''<ID>SUDS_meterX4</ID>
                                                <StartDate>2000-01-01</StartDate>
                                                <EndDate>9999-12-31</EndDate>
                                                <SerialID>MRR2111256234</SerialID>
                                                <MaterialID>M616523456243</MaterialID>
                                                <ProductUniqueItemID>MFin011234</ProductUniqueItemID>
                                                <SmartMeter>
                                                <UtilitiesAdvancedMeteringSystemID>I210</UtilitiesAdvancedMeteringSystemID>
                                                </SmartMeter>  ''')
        sendingData = self.client.service.UtilitiesDeviceERPSmartMeterCreateRequest_In(self.dict_parse['MessageHeader'], self.dict_parse['UtilitiesDevice'])
        print("Parsed and sent the data to webservice...")
    #Check the database for the task and meter getting created.
    def DBcheck(self):
        print("Entering DB zone...")
        self.cnxn = pymssql.connect("RAL-Redwood-db.itronhdc.com\int83_2014", "sa", "Meterguy1", "ItronEE")
        self.cursor = self.cnxn.cursor(as_dict=True)
        time.sleep(60)
        self.cursor.execute("select * from Meter where MeterID='SUDS_meterX4'")
        self.rows = dict(self.cursor)
        print(self.rows)
        if self.rows[0]==0:
            print("Meter not yet added... wait a while...\n")
            self.cnxn.close()
            time.sleep(30)
            self.DBcheck()
        else:
            row = self.cursor.fetchone()
            print(row)
            if row['MeterID'] == "SUDS_meterX4":
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