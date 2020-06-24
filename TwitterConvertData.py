#convert twitter csv data to json
import csv 
import json

#access appropriate files and create new json 
csvfile = open('/home/colinphillips17/Desktop/TAVtech/tweetData.csv',"r")
jsonfile = open("/home/colinphillips17/Desktop/TAVtech/tweetData.json","w")

fieldnames = ("Number","Tweet","Date","Latitude","Longitude")
reader = csv.DictReader(csvfile,fieldnames
for row in reader:
	json.dump(row,jsonfile)
	jsonfile.write("\n")

csvfile.close()
jsonfile.close()

