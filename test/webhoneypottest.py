import threading
import unittest
import urllib2
import random

from webhoneypot import Server


class WebHoneyPotTest(unittest.TestCase):
    def test_whenRequestToSlash_thenExpectResponseSent(self):
        port = random.randrange(8000, 60000)
        server = Server(FakeLogger(), port)
        threading.Thread(target=server.run, args=()).start()
        self.assertEqual(urllib2.urlopen("http://127.0.0.1:" + str(port) + "/").read(), "<html><body><h2>Welcome to router admin page</h2><p>Please, log in</p><form action='/login' method='POST'>username: <input name='username' value=''/><br />password: <input name='password' type='password' value=''/><br /><input type='submit'/></form></body></html>")
        server.stop()
        urllib2.urlopen("http://127.0.0.1:" + str(port) + "/")

    def test_whenRequestToLogin_thenExpectResponseSent(self):
        port = random.randrange(8000, 60000)
        server = Server(FakeLogger(), port)
        threading.Thread(target=server.run, args=()).start()
        self.assertEqual(urllib2.urlopen("http://127.0.0.1:" + str(port) + "/login").read(), "<html><body><h2>Welcome to router admin page</h2><p>Invalid Password!</p><p>Please, log in</p><form action='/login' method='POST'>username: <input name='username' value=''/><br />password: <input name='password' type='password' value=''/><br /><input type='submit'/></form></body></html>")
        server.stop()
        urllib2.urlopen("http://127.0.0.1:" + str(port) + "/")

    def test_whenRequestToHNAP1_thenExpectResponseSent(self):
        port = random.randrange(8000, 60000)
        server = Server(FakeLogger(), port)
        threading.Thread(target=server.run, args=()).start()
        self.assertEqual(urllib2.urlopen("http://127.0.0.1:" + str(port) + "/HNAP1").read(), '<?xml version="1.0" encoding="utf-8"?>\n<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="\nhttp://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/en\nvelope/">\n<soap:Body>\n<GetDeviceSettingsResponse xmlns="http://purenetworks.com/HNAP1/">\n<GetDeviceSettingsResult>OK</GetDeviceSettingsResult>\n<Type>GatewayWithWiFi</Type>\n<DeviceName>Cisco40033</DeviceName>\n<VendorName>Linksys</VendorName>\n<ModelDescription>Linksys E4200</ModelDescription>\n<ModelName>E4200</ModelName>\n<FirmwareVersion>1.0.04 build 11</FirmwareVersion>\n<PresentationURL>http://192.168.1.1/</PresentationURL>\n<SOAPActions>\n<string>http://purenetworks.com/HNAP1/IsDeviceReady</string>\n<string>http://purenetworks.com/HNAP1/GetDeviceSettings</string>\n<string>http://purenetworks.com/HNAP1/SetDeviceSettings</string>\n<string>http://purenetworks.com/HNAP1/GetDeviceSettings2</string>\n<string>http://purenetworks.com/HNAP1/SetDeviceSettings2</string>\n<string>http://purenetworks.com/HNAP1/Reboot</string>\n<string>http://purenetworks.com/HNAP1/RestoreFactoryDefaults</string>\n<string>http://purenetworks.com/HNAP1/RenewWanConnection</string>\n<string>http://purenetworks.com/HNAP1/GetWanSettings</string>\n<string>http://purenetworks.com/HNAP1/SetWanSettings</string>\n<string>http://purenetworks.com/HNAP1/GetRouterLanSettings2</string>\n<string>http://purenetworks.com/HNAP1/SetRouterLanSettings2</string>\n<string>http://purenetworks.com/HNAP1/GetWanInfo</string>\n<string>http://purenetworks.com/HNAP1/GetPortMappings</string>\n<string>http://purenetworks.com/HNAP1/AddPortMapping</string>\n<string>http://purenetworks.com/HNAP1/DeletePortMapping</string>\n<string>http://purenetworks.com/HNAP1/GetMACFilters2</string>\n<string>http://purenetworks.com/HNAP1/SetMACFilters2</string>\n<string>http://purenetworks.com/HNAP1/GetConnectedDevices</string>\n<string>http://purenetworks.com/HNAP1/GetNetworkStats</string>\n<string>http://purenetworks.com/HNAP1/GetClientStats</string>\n<string>http://purenetworks.com/HNAP1/GetWLanRadios</string>\n<string>http://purenetworks.com/HNAP1/GetWLanRadioSettings</string>\n<string>http://purenetworks.com/HNAP1/SetWLanRadioSettings</string>\n<string>http://purenetworks.com/HNAP1/GetWLanRadioSecurity</string>\n<string>http://purenetworks.com/HNAP1/SetWLanRadioSecurity</string>\n<string>http://purenetworks.com/HNAP1/GetRouterSettings</string>\n<string>http://purenetworks.com/HNAP1/SetRouterSettings</string>\n<string>http://purenetworks.com/HNAP1/GetFirmwareSettings</string>\n<string>http://purenetworks.com/HNAP1/FirmwareUpload</string>\n<string>http://purenetworks.com/HNAP1/DownloadSpeedTest</string>\n<string>http://cisco.com/HNAPExt/HND/GetPolicySettings</string>\n<string>http://cisco.com/HNAPExt/HND/SetPolicySettings</string>\n<string>http://cisco.com/HNAPExt/HND/GetDefaultPolicySetting</string>\n<string>http://cisco.com/HNAPExt/HND/SetDefaultPolicySetting</string>\n<string>http://cisco.com/HNAPExt/HND/GetTMSSSLicense</string>\n<string>http://cisco.com/HNAPExt/HND/ActivateTMSSS</string>\n<string>http://cisco.com/HNAPExt/HND/GetTMSSSSettings</string>\n<string>http://cisco.com/HNAPExt/HND/SetTMSSSSettings</string>\n<string>http://cisco.com/HNAPExt/HND/GetPolicySettingsCapabilities</string>\n<string>http://cisco.com/HNAPExt/HotSpot/GetDeviceInfo</string>\n<string>http://cisco.com/HNAPExt/HotSpot/SetDeviceInfo</string>\n<string>http://cisco.com/HNAPExt/HotSpot/GetGuestNetwork</string>\n<string>http://cisco.com/HNAPExt/HotSpot/SetGuestNetwork</string>\n<string>http://cisco.com/HNAPExt/HotSpot/GetGuestNetworkLANSettings</string>\n<string>http://cisco.com/HNAPExt/HotSpot/SetDefaultWireless</string>\n<string>http://cisco.com/HNAPExt/HotSpot/GetWANAccessStatuses</string>\n<string>http://cisco.com/HNAPExt/HotSpot/AddWebGUIAuthExemption</string>\n<string>http://cisco.com/HNAPExt/HotSpot/CheckParentalControlsPassword</string>\n<string>http://cisco.com/HNAPExt/HotSpot/GetParentalControlsResetQuestion</string>\n<string>http://cisco.com/HNAPExt/HotSpot/HasParentalControlsPassword</string>\n<string>http://cisco.com/HNAPExt/HotSpot/ResetParentalControlsPassword</string>\n<string>http://cisco.com/HNAPExt/HotSpot/SetParentalControlsPassword</string>\n<string>http://cisco.com/HNAPExt/HotSpot/SetParentalControlsResetQuestion</string>\n<string>http://cisco.com/HNAPExt/HotSpot/GetSwitchPortLEDSettings</string>\n<string>http://cisco.com/HNAPExt/HotSpot/SetSwitchPortLEDSettings</string>\n<string>http://cisco.com/HNAPExt/HotSpot/GetUSBCapability</string>\n<string>http://cisco.com/HNAPExt/HotSpot/GetUSBPortSettings</string>\n<string>http://cisco.com/HNAPExt/HotSpot/SetUSBPortSettings</string>\n<string>http://cisco.com/HNAPExt/HotSpot/DisconnectVirtualUSB</string>\n</SOAPActions>\n<SubDeviceURLs></SubDeviceURLs>\n<Tasks>\n<TaskExtension>\n<Name>Status Page</Name>\n<URL>/Status_Router.asp</URL>\n<Type>Browser</Type>\n</TaskExtension>\n<TaskExtension>\n<Name>Basic Wireless Settings</Name>\n<URL>/Wireless_Basic.asp</URL>\n<Type>Browser</Type>\n</TaskExtension>\n<TaskExtension>\n<Name>Linksys E4200</Name>\n<URL>http://www.linksys.com/support/E4200</URL>\n<Type>Browser</Type>\n</TaskExtension>\n</Tasks>\n</GetDeviceSettingsResponse>\n</soap:Body>\n</soap:Envelope>')
        server.stop()
        urllib2.urlopen("http://127.0.0.1:" + str(port) + "/")


class FakeLogger:
    def info(self, msg):
        pass