import threading
import unittest
import urllib2
import random

from honeypot import Server


class WebHoneyPotTest(unittest.TestCase):
    def test_whenRequestToSlash_thenExpectResponseSent(self):
        port = random.randrange(8000, 60000)
        server = Server(FakeLogger(), port, port + 1)
        threading.Thread(target=server.run, args=()).start()
        self.assertEqual(urllib2.urlopen("http://127.0.0.1:" + str(port) + "/").read(), "<html><body><h2>Welcome to router admin page</h2><p>Please, log in</p><form action='/login' method='POST'>username: <input name='username' value=''/><br />password: <input name='password' type='password' value=''/><br /><input type='submit'/></form></body></html>")
        server.stop()
        urllib2.urlopen("http://127.0.0.1:" + str(port) + "/")

    def test_whenRequestToLogin_thenExpectResponseSent(self):
        port = random.randrange(8000, 60000)
        server = Server(FakeLogger(), port, port + 1)
        threading.Thread(target=server.run, args=()).start()
        self.assertEqual(urllib2.urlopen("http://127.0.0.1:" + str(port) + "/login").read(), "<html><body><h2>Welcome to router admin page</h2><p>Invalid Password!</p><p>Please, log in</p><form action='/login' method='POST'>username: <input name='username' value=''/><br />password: <input name='password' type='password' value=''/><br /><input type='submit'/></form></body></html>")
        server.stop()
        urllib2.urlopen("http://127.0.0.1:" + str(port) + "/")

    def test_whenRequestToHNAP1_thenExpectResponseSent(self):
        port = random.randrange(8000, 60000)
        server = Server(FakeLogger(), port, port + 1)
        threading.Thread(target=server.run, args=()).start()
        self.assertEqual(urllib2.urlopen("http://127.0.0.1:" + str(port) + "/HNAP1").read(), '<?xml version="1.0" encoding="utf-8"?>\n<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="\nhttp://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/en\nvelope/">\n<soap:Body>\n<GetDeviceSettingsResponse xmlns="http://purenetworks.com/HNAP1/">\n<GetDeviceSettingsResult>OK</GetDeviceSettingsResult>\n<Type>GatewayWithWiFi</Type>\n<DeviceName>Cisco40033</DeviceName>\n<VendorName>Linksys</VendorName>\n<ModelDescription>Linksys E4200</ModelDescription>\n<ModelName>E4200</ModelName>\n<FirmwareVersion>1.0.04 build 11</FirmwareVersion>\n<PresentationURL>http://192.168.1.1/</PresentationURL>\n<SOAPActions>\n<string>http://purenetworks.com/HNAP1/IsDeviceReady</string>\n<string>http://purenetworks.com/HNAP1/GetDeviceSettings</string>\n<string>http://purenetworks.com/HNAP1/SetDeviceSettings</string>\n<string>http://purenetworks.com/HNAP1/GetDeviceSettings2</string>\n<string>http://purenetworks.com/HNAP1/SetDeviceSettings2</string>\n<string>http://purenetworks.com/HNAP1/Reboot</string>\n<string>http://purenetworks.com/HNAP1/RestoreFactoryDefaults</string>\n<string>http://purenetworks.com/HNAP1/RenewWanConnection</string>\n<string>http://purenetworks.com/HNAP1/GetWanSettings</string>\n<string>http://purenetworks.com/HNAP1/SetWanSettings</string>\n<string>http://purenetworks.com/HNAP1/GetRouterLanSettings2</string>\n<string>http://purenetworks.com/HNAP1/SetRouterLanSettings2</string>\n<string>http://purenetworks.com/HNAP1/GetWanInfo</string>\n<string>http://purenetworks.com/HNAP1/GetPortMappings</string>\n<string>http://purenetworks.com/HNAP1/AddPortMapping</string>\n<string>http://purenetworks.com/HNAP1/DeletePortMapping</string>\n<string>http://purenetworks.com/HNAP1/GetMACFilters2</string>\n<string>http://purenetworks.com/HNAP1/SetMACFilters2</string>\n<string>http://purenetworks.com/HNAP1/GetConnectedDevices</string>\n<string>http://purenetworks.com/HNAP1/GetNetworkStats</string>\n<string>http://purenetworks.com/HNAP1/GetClientStats</string>\n<string>http://purenetworks.com/HNAP1/GetWLanRadios</string>\n<string>http://purenetworks.com/HNAP1/GetWLanRadioSettings</string>\n<string>http://purenetworks.com/HNAP1/SetWLanRadioSettings</string>\n<string>http://purenetworks.com/HNAP1/GetWLanRadioSecurity</string>\n<string>http://purenetworks.com/HNAP1/SetWLanRadioSecurity</string>\n<string>http://purenetworks.com/HNAP1/GetRouterSettings</string>\n<string>http://purenetworks.com/HNAP1/SetRouterSettings</string>\n<string>http://purenetworks.com/HNAP1/GetFirmwareSettings</string>\n<string>http://purenetworks.com/HNAP1/FirmwareUpload</string>\n<string>http://purenetworks.com/HNAP1/DownloadSpeedTest</string>\n<string>http://cisco.com/HNAPExt/HND/GetPolicySettings</string>\n<string>http://cisco.com/HNAPExt/HND/SetPolicySettings</string>\n<string>http://cisco.com/HNAPExt/HND/GetDefaultPolicySetting</string>\n<string>http://cisco.com/HNAPExt/HND/SetDefaultPolicySetting</string>\n<string>http://cisco.com/HNAPExt/HND/GetTMSSSLicense</string>\n<string>http://cisco.com/HNAPExt/HND/ActivateTMSSS</string>\n<string>http://cisco.com/HNAPExt/HND/GetTMSSSSettings</string>\n<string>http://cisco.com/HNAPExt/HND/SetTMSSSSettings</string>\n<string>http://cisco.com/HNAPExt/HND/GetPolicySettingsCapabilities</string>\n<string>http://cisco.com/HNAPExt/HotSpot/GetDeviceInfo</string>\n<string>http://cisco.com/HNAPExt/HotSpot/SetDeviceInfo</string>\n<string>http://cisco.com/HNAPExt/HotSpot/GetGuestNetwork</string>\n<string>http://cisco.com/HNAPExt/HotSpot/SetGuestNetwork</string>\n<string>http://cisco.com/HNAPExt/HotSpot/GetGuestNetworkLANSettings</string>\n<string>http://cisco.com/HNAPExt/HotSpot/SetDefaultWireless</string>\n<string>http://cisco.com/HNAPExt/HotSpot/GetWANAccessStatuses</string>\n<string>http://cisco.com/HNAPExt/HotSpot/AddWebGUIAuthExemption</string>\n<string>http://cisco.com/HNAPExt/HotSpot/CheckParentalControlsPassword</string>\n<string>http://cisco.com/HNAPExt/HotSpot/GetParentalControlsResetQuestion</string>\n<string>http://cisco.com/HNAPExt/HotSpot/HasParentalControlsPassword</string>\n<string>http://cisco.com/HNAPExt/HotSpot/ResetParentalControlsPassword</string>\n<string>http://cisco.com/HNAPExt/HotSpot/SetParentalControlsPassword</string>\n<string>http://cisco.com/HNAPExt/HotSpot/SetParentalControlsResetQuestion</string>\n<string>http://cisco.com/HNAPExt/HotSpot/GetSwitchPortLEDSettings</string>\n<string>http://cisco.com/HNAPExt/HotSpot/SetSwitchPortLEDSettings</string>\n<string>http://cisco.com/HNAPExt/HotSpot/GetUSBCapability</string>\n<string>http://cisco.com/HNAPExt/HotSpot/GetUSBPortSettings</string>\n<string>http://cisco.com/HNAPExt/HotSpot/SetUSBPortSettings</string>\n<string>http://cisco.com/HNAPExt/HotSpot/DisconnectVirtualUSB</string>\n</SOAPActions>\n<SubDeviceURLs></SubDeviceURLs>\n<Tasks>\n<TaskExtension>\n<Name>Status Page</Name>\n<URL>/Status_Router.asp</URL>\n<Type>Browser</Type>\n</TaskExtension>\n<TaskExtension>\n<Name>Basic Wireless Settings</Name>\n<URL>/Wireless_Basic.asp</URL>\n<Type>Browser</Type>\n</TaskExtension>\n<TaskExtension>\n<Name>Linksys E4200</Name>\n<URL>http://www.linksys.com/support/E4200</URL>\n<Type>Browser</Type>\n</TaskExtension>\n</Tasks>\n</GetDeviceSettingsResponse>\n</soap:Body>\n</soap:Envelope>')
        server.stop()
        urllib2.urlopen("http://127.0.0.1:" + str(port) + "/")

    def test_whenRequestWebCalendar_thenExpectResponseSent(self):
        port = random.randrange(8000, 60000)
        server = Server(FakeLogger(), port, port + 1)
        threading.Thread(target=server.run, args=()).start()
        self.assertEqual(urllib2.urlopen("http://127.0.0.1:" + str(port) + "/webcalendar/install/index.php").read(), '<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"\n "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">\n<head><title>WebCalendar Setup Wizard</title>\n<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />\n<script type="text/javascript">\n<!-- <![CDATA[\n// detect browser\nNS4 = (document.layers) ? 1 : 0;\nIE4 = (document.all) ? 1 : 0;\n// W3C stands for the W3C standard, implemented in Mozilla (and Netscape 6) and IE5\nW3C = (document.getElementById) ? 1 : 0;\n\nfunction makeVisible ( name, hide ) {\n //alert (name);\n var ele;\n  if ( W3C ) {\n    ele = document.getElementById(name);\n  } else if ( NS4 ) {\n    ele = document.layers[name];\n  } else { // IE4\n    ele = document.all[name];\n  }\n\n  if ( NS4 ) {\n    ele.visibility = "show";\n  } else {  // IE4 & W3C & Mozilla\n    ele.style.visibility = "visible";\n    if ( hide )\n     ele.style.display = "";\n  }\n}\n\nfunction makeInvisible ( name, hide ) {\n  //alert (name);\n if (W3C) {\n    document.getElementById(name).style.visibility = "hidden";\n    if ( hide )\n      document.getElementById(name).style.display = "none";\n  } else if (NS4) {\n    document.layers[name].visibility = "hide";\n  } else {\n    document.all[name].style.visibility = "hidden";\n    if ( hide )\n      document.all[name].style.display = "none";\n  }\n}\n\nfunction showTab ( name ) {\n  if ( ! document.getElementById )\n    return true;\n\n  var div, i, tab, tname;\n\n  for ( i = 0; i < tabs.length; i++ ) {\n    tname = tabs[i];\n    tab = document.getElementById ( "tab_" + tname);\n    // We might call without parameter, if so display tabfor div.\n    if ( tab && ! name ) {\n      if ( tab.className == "tabfor" )\n        name = tname;\n    } else if ( tab ) {\n      tab.className = ( tname == name ? "tabfor" : "tabbak" );\n    }\n    div = document.getElementById ( "tabscontent_" + tname );\n    if ( div )\n      div.style.display = ( tname == name ? "block" : "none" );\n  }\n  return false;\n}\n\nfunction visByClass(classname, state){\n var inc=0;\n var alltags=document.all? document.all : document.getElementsByTagName("*");\n for (i=0; i<alltags.length; i++){\n var str=alltags[i].className;\n   if ( str && str.match(classname) )\n     if ( state=="hide")\n       alltags[i].style.display = "none";\n     else\n       alltags[i].style.display = "";\n }\n}\n\nfunction getScrollingPosition ()\n{\n var position = [0, 0];\n\n if (typeof window.pageYOffset != "undefined")\n {\n   position = [\n       window.pageXOffset,\n       window.pageYOffset\n   ];\n }\n\n else if (typeof document.documentElement.scrollTop\n     != "undefined" && document.documentElement.scrollTop > 0)\n {\n   position = [\n       document.documentElement.scrollLeft,\n       document.documentElement.scrollTop\n   ];\n }\n\n else if (typeof document.body.scrollTop != "undefined")\n {\n   position = [\n       document.body.scrollLeft,\n       document.body.scrollTop\n   ];\n }\n\n return position;\n}\n\n//these common function is placed here because all the files that use it\n//also use visibility functions\nfunction selectDate ( day, month, year, current, evt, form ) {\n  // get currently selected day/month/year\n  monthobj = eval( "document." + form.id + "." + month);\n  curmonth = monthobj.options[monthobj.selectedIndex].value;\n  yearobj = eval( "document." + form.id + "." + year );\n  curyear = yearobj.options[yearobj.selectedIndex].value;\n  date = curyear;\n  evt = evt? evt: window.event;\n  var scrollingPosition = getScrollingPosition ();\n\n  if (typeof evt.pageX != "undefined" &&\n     typeof evt.x != "undefined")\n {\n   mX = evt.pageX + 40;\n   mY = self.screen.availHeight - evt.pageY;\n }\n else\n {\n   mX = evt.clientX + scrollingPosition[0] + 40;\n   mY = evt.clientY + scrollingPosition[1];\n }\n//alert ( mX + " " + mY );\n  var MyPosition = "scrollbars=no,toolbar=no,screenx=" + mX + ",screeny=" + mY + ",left=" + mX + ",top=" + mY ;\n  if ( curmonth < 10 )\n    date += "0";\n  date += curmonth;\n  date += "01";\n  url = "datesel.php?form=" + form.id + "&fday=" + day +\n    "&fmonth=" + month + "&fyear=" + year + "&date=" + date;\n  var colorWindow = window.open (url,"DateSelection","width=300,height=180,"  + MyPosition);\n}\n\nfunction selectColor ( color, evt ) {\n  url = "colors.php?color=" + color;\n  if (document.getElementById) {\n    mX = evt.clientX   + 40;\n  }\n  else {\n    mX = evt.pageX + 40;\n  }\n  var mY = 100;\n  var MyOptions = "width=390,height=365,scrollbars=0,left=" + mX + ",top=" + mY + ",screenx=" + mX + ",screeny=" + mY;\n  var colorWindow = window.open (url,"ColorSelection","width=390,height=365," + MyOptions );\n}\n\nfunction valid_color ( str ) {\n var validColor = /^#[0-9a-fA-F]{3}$|^#[0-9a-fA-F]{6}$/;\n\n return validColor.test ( str );\n}\n\n// Updates the background-color of a table cell\n// Parameters:\n//    input - element containing the new color value\n//    target - id of sample\nfunction updateColor ( input, target ) {\n // The cell to be updated\n var colorCell = document.getElementById(target);\n // The new color\n var color = input.value;\n\n if (!valid_color ( color ) ) {\n   // Color specified is invalid; use black instead\n  colorCell.style.backgroundColor = "#000000";\n  input.select ();\n  input.focus ();\n  alert ( "Invalid Color");\n } else {\n  colorCell.style.backgroundColor = color;\n }\n}\n\nfunction toggle_datefields( name, ele ) {\n  var enabled = document.getElementById(ele.id).checked;\n  if ( enabled ) {\n      makeInvisible ( name );\n  } else {\n      makeVisible ( name );\n  }\n}\n\nfunction callEdit () {\n  var features = "width=600,height=500,resizable=yes,scrollbars=no";\n  var url = "edit_entry.php";\n  editwin = window.open ( url, "edit_entry", features );\n}\n//]]> -->\n</script>\n<script language="JavaScript" type="text/javascript">\n<!-- <![CDATA[\nfunction validate ( form )\n{\n  var form = document.form_app_settings;\n  var err = "";\n  // only check is to make sure single-user login is specified if\n  // in single-user mode\n  // find id of single user object\n  var listid = 0;\n  for ( i = 0; i < form.form_user_inc.length; i++ ) {\n    if ( form.form_user_inc.options[i].value == "none" )\n      listid = i;\n  }\n  if ( form.form_user_inc.options[listid].selected ) {\n    if ( form.form_single_user_login.value.length == 0 ) {\n      // No single user login specified\n      alert ("Error you must specify a\nSingle-User Login ");\n      form.form_single_user_login.focus ();\n      return false;\n    }\n  }\n  if ( form.form_server_url.value == "" ) {\n    err += "Server URL is required." + "\n";\n    form.form_server_url.select ();\n    form.form_server_url.focus ();\n  }\n  else if ( form.form_server_url.value.charAt (\n    form.form_server_url.value.length - 1 ) != "/" ) {\n    err += "Server URL must end with "/".\n";\n    form.form_server_url.select ();\n    form.form_server_url.focus ();\n  }\n if ( err != "" ) {\n    alert ( "Error:\n\n" + err );\n    return false;\n  }\n  // Submit form...\n  form.submit ();\n}\nfunction auth_handler () {\n  var form = document.form_app_settings;\n  // find id of single user object\n  var listid = 0;\n  for ( i = 0; i < form.form_user_inc.length; i++ ) {\n    if ( form.form_user_inc.options[i].value == "none" )\n      listid = i;\n  }\n  if ( form.form_user_inc.options[listid].selected ) {\n    makeVisible ( "singleuser" );\n  } else {\n    makeInvisible ( "singleuser" );\n  }\n}\n\nfunction db_type_handler () {\n  var form = document.dbform;\n  // find id of db_type object\n  var listid = 0;\n  var selectvalue = form.form_db_type.value;\n  if ( selectvalue == "sqlite" || selectvalue == "ibase" ) {\n      form.form_db_database.size = 65;\n    document.getElementById("db_name").innerHTML =\n    "Database Name" + ": " +\n   "Full Path (no backslashes)";\n  } else {\n      form.form_db_database.size = 20;\n    document.getElementById("db_name").innerHTML = "Database Name" + ": ";\n  }\n}\nfunction chkPassword () {\n  var form = document.dbform;\n  var db_pass = form.form_db_password.value;\n  var illegalChars = /\#/;\n  // do not allow #.../\#/ would stop all non-alphanumeric\n  if (illegalChars.test(db_pass)) {\n    alert( "The password contains illegal characters.");\n    form.form_db_password.select ();\n    form.form_db_password.focus ();\n    return false;\n  }\n}\n //]]> -->\n</script>\n<style type="text/css">\nbody {\n  background-color: #ffffff;\n  font-family: Arial, Helvetica, sans-serif;\n  margin: 0;\n}\ntable {\n  border: 0px solid #ccc;\n}\nth.pageheader {\n  font-size: 18px;\n padding:10px;\n  background-color: #eee;\n}\nth.header {\n  font-size: 14px;\n  background-color: #eee;\n}\nth.redheader {\n  font-size: 14px;\n  color: red;\n  background-color: #eee;\n}\ntd {\n  padding: 5px;\n}\ntd.prompt {\n  font-weight: bold;\n  padding-right: 20px;\n}\ntd.subprompt {\n  font-weight: bold;\n  padding-right: 20px;\n font-size: 12px;\n}\ndiv.nav {\n  margin: 0;\n  border-bottom: 1px solid #000;\n}\ndiv.main {\n  margin: 10px;\n}\nli {\n  margin-top: 10px;\n}\ndoc.li {\n  margin-top: 5px;\n}\n.recommended {\n  color: green;\n}\n.notrecommended {\n  color: red;\n}\n</style>\n</head>\n<body  >\n<table border="1" width="90%" align="center">\n<tr><th class="pageheader"  colspan="2">WebCalendar Installation Wizard Step 1</th></tr>\n<tr><td colspan="2" width="50%">\nThis installation wizard will guide you through setting up a basic WebCalendar installation. For help and troubleshooting see:<br />\n<ul>\n<li><a href="../docs/WebCalendar-SysAdmin.html" target="_docs">System Administrator"s Guide</a></li>\n<li><a href="../docs/WebCalendar-SysAdmin.html#faq" target="_docs">FAQ</a></li>\n<li><a href="../docs/WebCalendar-SysAdmin.html#trouble" target="_docs">Troubleshooting</a></li>\n<li><a href="../docs/WebCalendar-SysAdmin.html#help" target="_docs">Getting Help</a></li>\n<li><a href="../UPGRADING.html" target="_docs">Upgrading Guide</a></li>\n<li><a href="http://www.k5n.us/dokuwiki/doku.php" target="_docs">User Supported Wiki</a></li>\n</ul>\n</td></tr>\n<tr><th class="header"  colspan="2">PHP Version Check</th></tr>\n<tr><td>\nCheck to see if PHP 4.1.0 or greater is installed.\n</td>\n  <td class="recommended"><img src="recommended.gif" alt="" />&nbsp;PHP version 5.5.36</td></tr>\n<tr><th class="header" colspan="2">\n PHP Settings</th></tr>\n  <tr><td class="prompt">Safe Mode</td>\n  <td class="recommended"><img src="recommended.gif" alt=""/>&nbsp;OFF   </td></tr>\n  <tr><td class="prompt">Safe Mode Allowed Vars  (required only if Safe Mode is On)</td>\n  <td class="notrecommended"><img src="not_recommended.jpg" alt=""/>&nbsp;   </td></tr>\n  <tr><td class="prompt">Register Globals</td>\n  <td class="recommended"><img src="recommended.gif" alt=""/>&nbsp;OFF   </td></tr>\n  <tr><td class="prompt">Display Errors</td>\n  <td class="recommended"><img src="recommended.gif" alt=""/>&nbsp;ON   </td></tr>\n  <tr><td class="prompt">File Uploads</td>\n  <td class="recommended"><img src="recommended.gif" alt=""/>&nbsp;ON   </td></tr>\n  <tr><td class="prompt">Allow URL fopen  (required only if Remote Calendars are used)</td>\n  <td class="recommended"><img src="recommended.gif" alt=""/>&nbsp;ON   </td></tr>\n  <tr><td class="prompt">GD  (needed for Gradient Image Backgrounds)</td>\n  <td class="recommended"><img src="recommended.gif" alt=""/>&nbsp;ON   </td></tr>\n\n <tr><th class="header" colspan="2">Session Check</th></tr>\n <tr><td>\n  To test the proper operation of sessions, reload this page<br />You should see the session counter increment each time.</td>\n<td class="recommended"><img src="recommended.gif" alt=""/>&nbsp;SESSION COUNTER: 1 </td></tr>\n <tr><th class="header" colspan="2">Settings.php Status</th></tr>\n\n  <tr><td>\n   Your <b>settings.php</b> file appears to be valid.</td><td class="recommended">\n   <img src="recommended.gif" alt=""/>&nbsp;OK\n  </td></tr>\n\n <tr><th colspan="2" class="header">Configuration Wizard Password</th></tr>\n <tr><td colspan="2" align="center" style="border:none">\n   <form action="index.php" method="post" name="dblogin">\n   <table>\n    <tr><th>\n     Password:</th><td>\n     <input name="password3" type="password" />\n     <input type="submit" value="Login" />\n    </td></tr>\n   </table>\n  </form>\n </td></tr></table>\n\n</body>\n</html>\n')
        server.stop()
        urllib2.urlopen("http://127.0.0.1:" + str(port) + "/")


    def test_whenRequestFooCalendar_thenExpectResponseSent(self):
        port = random.randrange(8000, 60000)
        server = Server(FakeLogger(), port, port + 1)
        threading.Thread(target=server.run, args=()).start()
        self.assertEqual(urllib2.urlopen("http://127.0.0.1:" + str(port) + "/foo/calendar/install/index.php").read(), '<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"\n "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">\n<head><title>WebCalendar Setup Wizard</title>\n<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />\n<script type="text/javascript">\n<!-- <![CDATA[\n// detect browser\nNS4 = (document.layers) ? 1 : 0;\nIE4 = (document.all) ? 1 : 0;\n// W3C stands for the W3C standard, implemented in Mozilla (and Netscape 6) and IE5\nW3C = (document.getElementById) ? 1 : 0;\n\nfunction makeVisible ( name, hide ) {\n //alert (name);\n var ele;\n  if ( W3C ) {\n    ele = document.getElementById(name);\n  } else if ( NS4 ) {\n    ele = document.layers[name];\n  } else { // IE4\n    ele = document.all[name];\n  }\n\n  if ( NS4 ) {\n    ele.visibility = "show";\n  } else {  // IE4 & W3C & Mozilla\n    ele.style.visibility = "visible";\n    if ( hide )\n     ele.style.display = "";\n  }\n}\n\nfunction makeInvisible ( name, hide ) {\n  //alert (name);\n if (W3C) {\n    document.getElementById(name).style.visibility = "hidden";\n    if ( hide )\n      document.getElementById(name).style.display = "none";\n  } else if (NS4) {\n    document.layers[name].visibility = "hide";\n  } else {\n    document.all[name].style.visibility = "hidden";\n    if ( hide )\n      document.all[name].style.display = "none";\n  }\n}\n\nfunction showTab ( name ) {\n  if ( ! document.getElementById )\n    return true;\n\n  var div, i, tab, tname;\n\n  for ( i = 0; i < tabs.length; i++ ) {\n    tname = tabs[i];\n    tab = document.getElementById ( "tab_" + tname);\n    // We might call without parameter, if so display tabfor div.\n    if ( tab && ! name ) {\n      if ( tab.className == "tabfor" )\n        name = tname;\n    } else if ( tab ) {\n      tab.className = ( tname == name ? "tabfor" : "tabbak" );\n    }\n    div = document.getElementById ( "tabscontent_" + tname );\n    if ( div )\n      div.style.display = ( tname == name ? "block" : "none" );\n  }\n  return false;\n}\n\nfunction visByClass(classname, state){\n var inc=0;\n var alltags=document.all? document.all : document.getElementsByTagName("*");\n for (i=0; i<alltags.length; i++){\n var str=alltags[i].className;\n   if ( str && str.match(classname) )\n     if ( state=="hide")\n       alltags[i].style.display = "none";\n     else\n       alltags[i].style.display = "";\n }\n}\n\nfunction getScrollingPosition ()\n{\n var position = [0, 0];\n\n if (typeof window.pageYOffset != "undefined")\n {\n   position = [\n       window.pageXOffset,\n       window.pageYOffset\n   ];\n }\n\n else if (typeof document.documentElement.scrollTop\n     != "undefined" && document.documentElement.scrollTop > 0)\n {\n   position = [\n       document.documentElement.scrollLeft,\n       document.documentElement.scrollTop\n   ];\n }\n\n else if (typeof document.body.scrollTop != "undefined")\n {\n   position = [\n       document.body.scrollLeft,\n       document.body.scrollTop\n   ];\n }\n\n return position;\n}\n\n//these common function is placed here because all the files that use it\n//also use visibility functions\nfunction selectDate ( day, month, year, current, evt, form ) {\n  // get currently selected day/month/year\n  monthobj = eval( "document." + form.id + "." + month);\n  curmonth = monthobj.options[monthobj.selectedIndex].value;\n  yearobj = eval( "document." + form.id + "." + year );\n  curyear = yearobj.options[yearobj.selectedIndex].value;\n  date = curyear;\n  evt = evt? evt: window.event;\n  var scrollingPosition = getScrollingPosition ();\n\n  if (typeof evt.pageX != "undefined" &&\n     typeof evt.x != "undefined")\n {\n   mX = evt.pageX + 40;\n   mY = self.screen.availHeight - evt.pageY;\n }\n else\n {\n   mX = evt.clientX + scrollingPosition[0] + 40;\n   mY = evt.clientY + scrollingPosition[1];\n }\n//alert ( mX + " " + mY );\n  var MyPosition = "scrollbars=no,toolbar=no,screenx=" + mX + ",screeny=" + mY + ",left=" + mX + ",top=" + mY ;\n  if ( curmonth < 10 )\n    date += "0";\n  date += curmonth;\n  date += "01";\n  url = "datesel.php?form=" + form.id + "&fday=" + day +\n    "&fmonth=" + month + "&fyear=" + year + "&date=" + date;\n  var colorWindow = window.open (url,"DateSelection","width=300,height=180,"  + MyPosition);\n}\n\nfunction selectColor ( color, evt ) {\n  url = "colors.php?color=" + color;\n  if (document.getElementById) {\n    mX = evt.clientX   + 40;\n  }\n  else {\n    mX = evt.pageX + 40;\n  }\n  var mY = 100;\n  var MyOptions = "width=390,height=365,scrollbars=0,left=" + mX + ",top=" + mY + ",screenx=" + mX + ",screeny=" + mY;\n  var colorWindow = window.open (url,"ColorSelection","width=390,height=365," + MyOptions );\n}\n\nfunction valid_color ( str ) {\n var validColor = /^#[0-9a-fA-F]{3}$|^#[0-9a-fA-F]{6}$/;\n\n return validColor.test ( str );\n}\n\n// Updates the background-color of a table cell\n// Parameters:\n//    input - element containing the new color value\n//    target - id of sample\nfunction updateColor ( input, target ) {\n // The cell to be updated\n var colorCell = document.getElementById(target);\n // The new color\n var color = input.value;\n\n if (!valid_color ( color ) ) {\n   // Color specified is invalid; use black instead\n  colorCell.style.backgroundColor = "#000000";\n  input.select ();\n  input.focus ();\n  alert ( "Invalid Color");\n } else {\n  colorCell.style.backgroundColor = color;\n }\n}\n\nfunction toggle_datefields( name, ele ) {\n  var enabled = document.getElementById(ele.id).checked;\n  if ( enabled ) {\n      makeInvisible ( name );\n  } else {\n      makeVisible ( name );\n  }\n}\n\nfunction callEdit () {\n  var features = "width=600,height=500,resizable=yes,scrollbars=no";\n  var url = "edit_entry.php";\n  editwin = window.open ( url, "edit_entry", features );\n}\n//]]> -->\n</script>\n<script language="JavaScript" type="text/javascript">\n<!-- <![CDATA[\nfunction validate ( form )\n{\n  var form = document.form_app_settings;\n  var err = "";\n  // only check is to make sure single-user login is specified if\n  // in single-user mode\n  // find id of single user object\n  var listid = 0;\n  for ( i = 0; i < form.form_user_inc.length; i++ ) {\n    if ( form.form_user_inc.options[i].value == "none" )\n      listid = i;\n  }\n  if ( form.form_user_inc.options[listid].selected ) {\n    if ( form.form_single_user_login.value.length == 0 ) {\n      // No single user login specified\n      alert ("Error you must specify a\nSingle-User Login ");\n      form.form_single_user_login.focus ();\n      return false;\n    }\n  }\n  if ( form.form_server_url.value == "" ) {\n    err += "Server URL is required." + "\n";\n    form.form_server_url.select ();\n    form.form_server_url.focus ();\n  }\n  else if ( form.form_server_url.value.charAt (\n    form.form_server_url.value.length - 1 ) != "/" ) {\n    err += "Server URL must end with "/".\n";\n    form.form_server_url.select ();\n    form.form_server_url.focus ();\n  }\n if ( err != "" ) {\n    alert ( "Error:\n\n" + err );\n    return false;\n  }\n  // Submit form...\n  form.submit ();\n}\nfunction auth_handler () {\n  var form = document.form_app_settings;\n  // find id of single user object\n  var listid = 0;\n  for ( i = 0; i < form.form_user_inc.length; i++ ) {\n    if ( form.form_user_inc.options[i].value == "none" )\n      listid = i;\n  }\n  if ( form.form_user_inc.options[listid].selected ) {\n    makeVisible ( "singleuser" );\n  } else {\n    makeInvisible ( "singleuser" );\n  }\n}\n\nfunction db_type_handler () {\n  var form = document.dbform;\n  // find id of db_type object\n  var listid = 0;\n  var selectvalue = form.form_db_type.value;\n  if ( selectvalue == "sqlite" || selectvalue == "ibase" ) {\n      form.form_db_database.size = 65;\n    document.getElementById("db_name").innerHTML =\n    "Database Name" + ": " +\n   "Full Path (no backslashes)";\n  } else {\n      form.form_db_database.size = 20;\n    document.getElementById("db_name").innerHTML = "Database Name" + ": ";\n  }\n}\nfunction chkPassword () {\n  var form = document.dbform;\n  var db_pass = form.form_db_password.value;\n  var illegalChars = /\#/;\n  // do not allow #.../\#/ would stop all non-alphanumeric\n  if (illegalChars.test(db_pass)) {\n    alert( "The password contains illegal characters.");\n    form.form_db_password.select ();\n    form.form_db_password.focus ();\n    return false;\n  }\n}\n //]]> -->\n</script>\n<style type="text/css">\nbody {\n  background-color: #ffffff;\n  font-family: Arial, Helvetica, sans-serif;\n  margin: 0;\n}\ntable {\n  border: 0px solid #ccc;\n}\nth.pageheader {\n  font-size: 18px;\n padding:10px;\n  background-color: #eee;\n}\nth.header {\n  font-size: 14px;\n  background-color: #eee;\n}\nth.redheader {\n  font-size: 14px;\n  color: red;\n  background-color: #eee;\n}\ntd {\n  padding: 5px;\n}\ntd.prompt {\n  font-weight: bold;\n  padding-right: 20px;\n}\ntd.subprompt {\n  font-weight: bold;\n  padding-right: 20px;\n font-size: 12px;\n}\ndiv.nav {\n  margin: 0;\n  border-bottom: 1px solid #000;\n}\ndiv.main {\n  margin: 10px;\n}\nli {\n  margin-top: 10px;\n}\ndoc.li {\n  margin-top: 5px;\n}\n.recommended {\n  color: green;\n}\n.notrecommended {\n  color: red;\n}\n</style>\n</head>\n<body  >\n<table border="1" width="90%" align="center">\n<tr><th class="pageheader"  colspan="2">WebCalendar Installation Wizard Step 1</th></tr>\n<tr><td colspan="2" width="50%">\nThis installation wizard will guide you through setting up a basic WebCalendar installation. For help and troubleshooting see:<br />\n<ul>\n<li><a href="../docs/WebCalendar-SysAdmin.html" target="_docs">System Administrator"s Guide</a></li>\n<li><a href="../docs/WebCalendar-SysAdmin.html#faq" target="_docs">FAQ</a></li>\n<li><a href="../docs/WebCalendar-SysAdmin.html#trouble" target="_docs">Troubleshooting</a></li>\n<li><a href="../docs/WebCalendar-SysAdmin.html#help" target="_docs">Getting Help</a></li>\n<li><a href="../UPGRADING.html" target="_docs">Upgrading Guide</a></li>\n<li><a href="http://www.k5n.us/dokuwiki/doku.php" target="_docs">User Supported Wiki</a></li>\n</ul>\n</td></tr>\n<tr><th class="header"  colspan="2">PHP Version Check</th></tr>\n<tr><td>\nCheck to see if PHP 4.1.0 or greater is installed.\n</td>\n  <td class="recommended"><img src="recommended.gif" alt="" />&nbsp;PHP version 5.5.36</td></tr>\n<tr><th class="header" colspan="2">\n PHP Settings</th></tr>\n  <tr><td class="prompt">Safe Mode</td>\n  <td class="recommended"><img src="recommended.gif" alt=""/>&nbsp;OFF   </td></tr>\n  <tr><td class="prompt">Safe Mode Allowed Vars  (required only if Safe Mode is On)</td>\n  <td class="notrecommended"><img src="not_recommended.jpg" alt=""/>&nbsp;   </td></tr>\n  <tr><td class="prompt">Register Globals</td>\n  <td class="recommended"><img src="recommended.gif" alt=""/>&nbsp;OFF   </td></tr>\n  <tr><td class="prompt">Display Errors</td>\n  <td class="recommended"><img src="recommended.gif" alt=""/>&nbsp;ON   </td></tr>\n  <tr><td class="prompt">File Uploads</td>\n  <td class="recommended"><img src="recommended.gif" alt=""/>&nbsp;ON   </td></tr>\n  <tr><td class="prompt">Allow URL fopen  (required only if Remote Calendars are used)</td>\n  <td class="recommended"><img src="recommended.gif" alt=""/>&nbsp;ON   </td></tr>\n  <tr><td class="prompt">GD  (needed for Gradient Image Backgrounds)</td>\n  <td class="recommended"><img src="recommended.gif" alt=""/>&nbsp;ON   </td></tr>\n\n <tr><th class="header" colspan="2">Session Check</th></tr>\n <tr><td>\n  To test the proper operation of sessions, reload this page<br />You should see the session counter increment each time.</td>\n<td class="recommended"><img src="recommended.gif" alt=""/>&nbsp;SESSION COUNTER: 1 </td></tr>\n <tr><th class="header" colspan="2">Settings.php Status</th></tr>\n\n  <tr><td>\n   Your <b>settings.php</b> file appears to be valid.</td><td class="recommended">\n   <img src="recommended.gif" alt=""/>&nbsp;OK\n  </td></tr>\n\n <tr><th colspan="2" class="header">Configuration Wizard Password</th></tr>\n <tr><td colspan="2" align="center" style="border:none">\n   <form action="index.php" method="post" name="dblogin">\n   <table>\n    <tr><th>\n     Password:</th><td>\n     <input name="password3" type="password" />\n     <input type="submit" value="Login" />\n    </td></tr>\n   </table>\n  </form>\n </td></tr></table>\n\n</body>\n</html>\n')
        server.stop()
        urllib2.urlopen("http://127.0.0.1:" + str(port) + "/")

    def test_whenRequestXmlRpc_thenExpectResponseSent(self):
        port = random.randrange(8000, 60000)
        server = Server(FakeLogger(), port, port + 1)
        threading.Thread(target=server.run, args=()).start()
        self.assertEqual(urllib2.urlopen("http://127.0.0.1:" + str(port) + "/xmlrpc.php").read(), '<?xml version="1.0"?>\n<methodCall>\n   <methodName>examples.getStateName</methodName>\n   <params>\n      <param>\n         <value><i4>41</i4></value>\n         </param>\n      </params>\n   </methodCall>')
        server.stop()
        urllib2.urlopen("http://127.0.0.1:" + str(port) + "/")

    def test_whenRequestFooXmlRpc_thenExpectResponseSent(self):
        port = random.randrange(8000, 60000)
        server = Server(FakeLogger(), port, port + 1)
        threading.Thread(target=server.run, args=()).start()
        self.assertEqual(urllib2.urlopen("http://127.0.0.1:" + str(port) + "/foo/xmlrpc.php").read(), '<?xml version="1.0"?>\n<methodCall>\n   <methodName>examples.getStateName</methodName>\n   <params>\n      <param>\n         <value><i4>41</i4></value>\n         </param>\n      </params>\n   </methodCall>')
        server.stop()
        urllib2.urlopen("http://127.0.0.1:" + str(port) + "/")


    def test_whenTelnetRequest_tenResponseSent(self):
        port = random.randrange(8000, 60000)
        server = Server(FakeLogger(), port, port + 1)
        threading.Thread(target=server.run, args=()).start()
        self.assertEqual(urllib2.urlopen("http://127.0.0.1:" + str(port) + "/foo/xmlrpc.php").read(), 'foo')
        server.stop()
        urllib2.urlopen("http://127.0.0.1:" + str(port) + "/")


class FakeLogger:
    def info(self, msg):
        pass
