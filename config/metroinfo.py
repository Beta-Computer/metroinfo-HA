import requests
import datetime
from dateutil.parser import parse
currenttime = datetime.datetime.now()
baseurl = 'https://apis.metroinfo.co.nz/rti/siri/v1/sm?stopcode='
# Change this \/ to a different code
stopcode = '53088'
# Change this \/ to your api token
apitoken = '1279u3392r9dj9328sfj983289hmafjkaj821ujd291'
# Change this to the bus number you would like the sensor to filter
# Set filterbuscode = 0 if you would like to get the next bus regardless of bus code
filterbuscode = '29'
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
print("time till next bus is:", Difftimemin, "minutes")
print("next bus code: " + nextbuscode)
