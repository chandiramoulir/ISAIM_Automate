import re

FuncCalls = ''' MeterReadingDocumentERPResultBulkCreateConfirmation_Out(ns0:BusinessDocumentMessageHeader MessageHeader, ns0:MtrRdngDocERPRsltCrteConfMsg[] MeterReadingDocumentERPResultCreateConfirmationMessage, ns0:Log Log, )
            SmartMeterMeterReadingDocumentERPBulkCancellationRequest_In(ns0:BusinessDocumentMessageHeader MessageHeader, ns0:SmrtMtrMtrRdngDocERPCanclnReqMsg[] SmartMeterMeterReadingDocumentERPBulkCancellationRequestMessage, )
            SmartMeterMeterReadingDocumentERPBulkCreateRequest_Out(ns0:BusinessDocumentMessageHeader MessageHeader, ns0:SmrtMtrMtrRdngDocERPCrteReqMsg[] SmartMeterMeterReadingDocumentERPCreateRequestMessage, )
            SmartMeterMeterReadingDocumentERPResultBulkChangeRequest_Out(ns0:BusinessDocumentMessageHeader MessageHeader, ns0:SmrtMtrMtrRdngDocERPRsltChgReqMsg[] SmartMeterMeterReadingDocumentERPResultChangeRequestMessage, )
            SmartMeterMeterReadingDocumentERPResultBulkCreateRequest_Out(ns0:BusinessDocumentMessageHeader MessageHeader, ns0:SmrtMtrMtrRdngDocERPRsltCrteReqMsg[] SmartMeterMeterReadingDocumentERPResultCreateRequestMessage, )
            SmartMeterUtilitiesConnectionStatusChangeRequestERPBulkCreateRequest_Out(ns0:BusinessDocumentMessageHeader MessageHeader, ns0:SmrtMtrUtilsConncnStsChgReqERPCrteReqMsg[] SmartMeterUtilitiesConnectionStatusChangeRequestERPCreateRequestMessage, )
            SmartMeterUtilitiesConnectionStatusChangeRequestERPBulkNotification_Out(ns0:BusinessDocumentMessageHeader MessageHeader, ns0:SmrtMtrUtilsConncnStsChgReqERPNotifMsg[] SmartMeterUtilitiesConnectionStatusChangeRequestERPNotificationMessage, )
            SmartMeterUtilitiesConnectionStatusChangeRequestERPCancellationBulkNotification_Out(ns0:BusinessDocumentMessageHeader MessageHeader, ns0:SmrtMtrUtilsConncnStsChgReqERPCanclnNotifMsg[] SmartMeterUtilitiesConnectionStatusChangeRequestERPCancellationNotificationMessage, )
            SmartMeterUtilitiesMeasurementTaskERPBulkChangeRequest_Out(ns0:BusinessDocumentMessageHeader MessageHeader, ns0:SmrtMtrUtilsMsmtTskERPChgReqMsg[] SmartMeterUtilitiesMeasurementTaskERPChangeRequestMessage, )
            SmartMeterUtilitiesMeasurementTaskERPPointOfDeliveryBulkAssignedNotification_Out(ns0:BusinessDocumentMessageHeader MessageHeader, ns0:SmrtMtrUtilsMsmtTskERPPtDelivAssgndNotifMsg[] SmartMeterUtilitiesMeasurementTaskERPPointOfDeliveryAssignedNotificationMessage, )
            UtilitiesDeviceERPSmartMeterBulkChangeRequest_Out(ns0:BusinessDocumentMessageHeader MessageHeader, ns0:UtilsDvceERPSmrtMtrChgReqMsg[] UtilitiesDeviceERPSmartMeterChangeRequestMessage, )
            UtilitiesDeviceERPSmartMeterBulkCreateRequest_In(ns0:BusinessDocumentMessageHeader MessageHeader, ns0:UtilsDvceERPSmrtMtrCrteReqMsg[] UtilitiesDeviceERPSmartMeterCreateRequestMessage, )
            UtilitiesDeviceERPSmartMeterCancellationBulkRequest_Out(ns0:BusinessDocumentMessageHeader MessageHeader, ns0:UtilsDvceERPSmrtMtrCanclnReqMsg[] UtilitiesDeviceERPSmartMeterCancellationRequestMessage, )
            UtilitiesDeviceERPSmartMeterLocationBulkNotification_Out(ns0:BusinessDocumentMessageHeader MessageHeader, ns0:UtilsDvceERPSmrtMtrLocNotifMsg[] UtilitiesDeviceERPSmartMeterLocationNotificationMessage, )
            UtilitiesDeviceERPSmartMeterRegisterBulkChangeRequest_Out(ns0:BusinessDocumentMessageHeader MessageHeader, ns0:UtilsDvceERPSmrtMtrRegChgReqMsg[] UtilitiesDeviceERPSmartMeterRegisterChangeRequestMessage, )
            UtilitiesDeviceERPSmartMeterRegisterBulkCreateRequest_Out(ns0:BusinessDocumentMessageHeader MessageHeader, ns0:UtilsDvceERPSmrtMtrRegCrteReqMsg[] UtilitiesDeviceERPSmartMeterRegisterCreateRequestMessage, )
            UtilitiesDeviceERPSmartMeterReplicationBulkConfirmation_Out(ns0:BusinessDocumentMessageHeader MessageHeader, ns0:UtilsDvceERPSmrtMtrRplctnConfMsg[] UtilitiesDeviceERPSmartMeterReplicationConfirmationMessage, ns0:Log Log, )
            UtilitiesDeviceERPSmartMeterReplicationBulkRequest_Out(ns0:BusinessDocumentMessageHeader MessageHeader, ns0:UtilsDvceERPSmrtMtrRplctnReqMsg[] UtilitiesDeviceERPSmartMeterReplicationRequestMessage, )
            UtilitiesDeviceERPSmartMeterTextBulkNotification_Out(ns0:BusinessDocumentMessageHeader MessageHeader, ns0:UtilsDvceERPSmrtMtrTxtNotifMsg[] UtilitiesDeviceERPSmartMeterTextNotificationMessage, )
            UtilitiesSmartMeterEventERPBulkCreateConfirmation_Out(ns0:BusinessDocumentMessageHeader MessageHeader, ns0:UtilsSmrtMtrEvtERPCrteConfMsg[] UtilitiesSmartMeterEventERPCreateConfirmationMessage, ns0:Log Log, )
            UtilitiesTimeSeriesBundleItemCreateConfirmation_In(ns1:BusinessDocumentMessageHeader MessageHeader, ns1:UtilitiesTimeSeriesItemCreateConfirmationMessage[] UtilitiesTimeSeriesItemCreateConfirmationMessage, ns1:Log Log, )
            UtilitiesTimeSeriesCalculationERPBulkCreateRequest_Out(ns0:BusinessDocumentMessageHeader MessageHeader, ns0:UtilsTmeSersCalcERPCrtReqMsg[] UtilitiesTimeSeriesCalculationERPCreateRequestMessage, )
            UtilitiesTimeSeriesCalculationERPCancellationBulkRequest_Out(ns0:BusinessDocumentMessageHeader MessageHeader, ns0:UtilsTmeSersCalcERPCanclnReqMsg[] UtilitiesTimeSeriesCalculationERPCancellationRequestMessage, )
            UtilitiesTimeSeriesERPItemBulkChangeConfirmation_Out(ns0:BusinessDocumentMessageHeader MessageHeader, ns0:UtilsTmeSersERPItmChgConfMsg[] UtilitiesTimeSeriesERPItemChangeConfirmationMessage, ns0:Log Log, )
            UtilitiesTimeSeriesERPItemBulkCreateConfirmation_Out(ns0:BusinessDocumentMessageHeader MessageHeader, ns0:UtilsTmeSersERPItmCrteConfMsg[] UtilitiesTimeSeriesERPItemCreateConfirmationMessage, ns0:Log Log, )
            UtilitiesTimeSeriesERPReplicationBulkRequest_Out(ns0:BusinessDocumentMessageHeader MessageHeader, ns0:UtilsTmeSersERPRplctnReqMsg[] UtilitiesTimeSeriesERPReplicationRequestMessage, )'''

ans = FuncCalls.split(" ")
for i in ans:
    if i.endswith('[]'):
        print(i)

#print(ans)