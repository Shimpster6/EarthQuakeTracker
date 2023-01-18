import requests
import json
import time
import datetime
import os


run = True
while run == True:
	response = requests.get('https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_hour.geojson')
	quakes = json.loads(response.text)
	count = quakes['metadata']['count']
	features = quakes['features']

	localtime = time.localtime()
	result = time.strftime("%I:%M:%S %p", localtime)
	print(result)

	print("Count: " + str(count) + "\n")

	i = 0
	while i < count:
		if str(features[i]['properties']['type']) == "earthquake":
			print("Type: Earthquake")
		else:
			print("Type: " + str(features[i]['properties']['type']))
		print("Place: " + str(features[i]['properties']['place']))
		print("Magnitude: " + str(features[i]['properties']['mag']))
		try: 
			print("Depth(km): " + str(features[i]['properties']['depth']))
		except:
			print("Depth(km): Unknown")
		epochTime = (features[i]['properties']['time'])/1000
		quakeTime = datetime.datetime.fromtimestamp(epochTime)
		print("Time: " + str(quakeTime))
		print("Status: " + str(features[i]['properties']['status']))
		if str(features[i]['properties']['alert']) == "None":
			print("Alert: " + str(features[i]['properties']['alert']))
		else:
			print("*********************Alert: " + str(features[i]['properties']['alert']) + "*********************")
		print("Felt by: " + str(features[i]['properties']['felt']))


		print("\n")
		i+=1
	time.sleep(60)
	os.system('cls')
	i = 0


