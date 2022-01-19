import requests
import datetime
from dateutil.parser import parse
import Setup
currenttime = datetime.datetime.now()
baseurl = 'https://apis.metroinfo.co.nz/rti/siri/v1/sm?stopcode='
stopcode = Setup.stopcode
apitoken = Setup.apitoken
filterbuscode = Setup.filterbuscode
nextbus = 0
headers = {'Ocp-Apim-Subscription-Key': apitoken}
fullurl = baseurl + stopcode
responsejson = (requests.get(fullurl, headers=headers)).json
# Get data
def getbustime(nextbusnumber):
    nextbustime = responsejson()['Siri']['ServiceDelivery']['StopMonitoringDelivery'][0]['MonitoredStopVisit'][int(nextbusnumber)]['MonitoredVehicleJourney']['MonitoredCall']['ExpectedArrivalTime']
    return nextbustime
def getbuscode(nextbusnumber):
    nextbuscode = responsejson()['Siri']['ServiceDelivery']['StopMonitoringDelivery'][0]['MonitoredStopVisit'][int(nextbusnumber)]['MonitoredVehicleJourney']['PublishedLineName']
    return nextbuscode
# If get next bus is true it will get the next bus else it will look for the filtered bus
if Setup.get_next_bus != "true":
    nextbuscode = (getbuscode(nextbus))
    if nextbuscode == Setup.filterbuscode:
        nextbustime = (getbustime(nextbus))
        nextbuscode = (getbuscode(nextbus))
    else:
        while nextbuscode != filterbuscode:
            nextbus = nextbus + 1
            nextbustime = (getbustime(nextbus))
            nextbuscode = (getbuscode(nextbus))
            print(nextbus)
else:
    nextbustime = (getbustime(nextbus))
    nextbuscode = (getbuscode(nextbus))
# Turn time of bus into time till bus
Bustime = parse(nextbustime)
Difftimemin = (Bustime.minute - currenttime.minute)
Difftimehour = (Bustime.hour - currenttime.hour)
Difftimemin = Difftimemin + (Difftimehour * 60)
print(Difftimemin)
# Debug
# print("time till next bus is:", Difftimemin, "minutes")
# print("next bus code: " + nextbuscode)
