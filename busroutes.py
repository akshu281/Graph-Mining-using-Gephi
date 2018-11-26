import requests
import json
import csv
import datetime
import time
headers={'AccountKey':'RAGHPk3qTNC685iHir8V8w==','accept':'application/json'}
url="http://datamall2.mytransport.sg/ltaodataservice/BusRoutes?$skip="
count=0
outputfile=open("outputfile.csv","a")
csvwriter = csv.writer(outputfile)
while(True):
    print("Fetching",str(count))
    local_url=url+str(count)
    resp=requests.get(local_url,headers=headers)
    print(count)
    print(len(list(resp.json()['value'])))
    if(len(list(resp.json()['value']))<500):
        break;
    else:
        count+=500
    for data in list(resp.json()['value']):
            locallist=[]
            locallist.append(data["ServiceNo"])
            locallist.append(data["Operator"])
            locallist.append(data["Direction"])
            locallist.append(data["StopSequence"])
            locallist.append(data["BusStopCode"])
            locallist.append(data["Distance"])
            locallist.append(data["WD_FirstBus"])
            locallist.append(data["WD_LastBus"])
            locallist.append(data["SAT_FirstBus"])
            locallist.append(data["SAT_LastBus"])
            locallist.append(data["SUN_FirstBus"])
            locallist.append(data["SUN_LastBus"])
            csvwriter.writerow(locallist)
outputfile.close()
    # time.sleep(420)




#r=requests.get(url,headers=headers)
#print(r.json())
