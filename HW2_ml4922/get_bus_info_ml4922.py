#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 14:22:50 2018

@author: minqilu
"""

from __future__ import print_function
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
import sys

MTAkey = sys.argv[1]
BUSline = sys.argv[2]
BUSlinecsv = sys.argv[3]

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s"%(MTAkey,BUSline)

response = urllib.urlopen(url)
data = response.read().decode("utf-8")
#use the json.loads method to obtain a dictionary representation of the responose string 
dataDict = json.loads(data)
data1 = dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

#check how many arguments are passed to python
if not len(sys.argv) == 4:
   print ("Invalid number of arguments. Run as: python get_bus_info_ml4922.py <MTA_KEY> <BUS_LINE> <BUS_LINE>.csv")
   sys.exit()
    
fout = open(sys.argv[3], "w")
fout.write("Longitude,Latitude,Stop name, Stop status\n")

for i in range (0,len(data1)):
    Longitude = data1[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    Latitude = data1[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']

    if len(data1[i]['MonitoredVehicleJourney']['OnwardCalls']) == 0:
        StopName = 'N/A'
        StopStatus = 'N/A'
    else:
         StopName = data1[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]["StopPointName"]
         StopStatus = data1[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]["Extensions"]["Distances"]["PresentableDistance"]
        
    print(Longitude,Latitude,StopName, StopStatus)
    fout.write('%s,%s,%s,%s\n'%(Longitude,Latitude,StopName,StopStatus))

fout.close()
