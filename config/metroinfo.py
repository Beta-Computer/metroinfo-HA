import requests
import datetime
from dateutil.parser import parse
import Setup
currenttime = datetime.datetime.now()
baseurl = 'https://apis.metroinfo.co.nz/rti/siri/v1/sm?stopcode='
stopcode = Setup.stopcode
apitoken = Setup.apitoken
filterbuscode = Setup.filterbuscode
nextbusnumber = 0
headers = {'Ocp-Apim-Subscription-Key': apitoken}
fullurl = baseurl + stopcode
responsejson = (requests.get(fullurl, headers=headers)).json
nextbuscode = responsejson()['Siri']['ServiceDelivery']['StopMonitoringDelivery'][0]['MonitoredStopVisit'][nextbusnumber]['MonitoredVehicleJourney']['PublishedLineName']
nextbustime = responsejson()['Siri']['ServiceDelivery']['StopMonitoringDelivery'][0]['MonitoredStopVisit'][nextbusnumber]['MonitoredVehicleJourney']['MonitoredCall']['ExpectedArrivalTime']
if filterbuscode != 0:
    while nextbuscode != filterbuscode:
        nextbusnumber = int(nextbusnumber + 1)
        nextbuscode = responsejson()['Siri']['ServiceDelivery']['StopMonitoringDelivery'][0]['MonitoredStopVisit'][nextbusnumber]['MonitoredVehicleJourney']['PublishedLineName']
        nextbustime = responsejson()['Siri']['ServiceDelivery']['StopMonitoringDelivery'][0]['MonitoredStopVisit'][nextbusnumber]['MonitoredVehicleJourney']['MonitoredCall']['ExpectedArrivalTime']
    
Bustime = parse(nextbustime)
Difftimemin = (Bustime.minute - currenttime.minute)
Difftimehour = (Bustime.hour - currenttime.hour)
Difftimemin = Difftimemin + (Difftimehour * 60)
print(Difftimemin)
# Debug
# print("time till next bus is:", Difftimemin, "minutes")
# print("next bus code: " + nextbuscode)
