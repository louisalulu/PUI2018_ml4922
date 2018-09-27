# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from __future__ import print_function
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
import sys

MTAkey = sys.argv[1]
BUSline= sys.argv[2]

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s"%(MTAkey,BUSline)

#print (url)
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
#use the json.loads method to obtain a dictionary representation of the responose string 
dataDict = json.loads(data)

data1 = dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

print("Bus line : %s"%(BUSline))
print("Number of Active Buses : %s"%(len(data1)))
for i in range (0,len(data1)):
    print(" Bus %s is at latitude %s and longitude %s"%(i,data1[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude'],data1[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']))
