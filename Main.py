import csv
import json
import urllib.request

def makeDataList(dataName):
    with open("earthquakes.csv", "r") as inFile:
        dataList = []

        csvReader = csv.reader(inFile)
        titles = next(csvReader)

        colNum = 0
        while colNum < len(titles) and titles[colNum] != dataName:
            colNum = colNum + 1

        if colNum == len(titles):
            print("Error: ", dataName, " not found.")
        else:
            dataList = [(float(line[colNum])) for line in csvReader]
            #for line in csvReader:
                #dataList.append(float(line[colNum]))

    return dataList

def makeMagList(earthquakeData):
    magList = []
    earthquakes = earthquakeData.get('features')
    for i in range(len(earthquakes)):
        earthquake = earthquakes[i]
        properties = earthquake.get('properties')
        mag = properties.get('mag')
        magList.append(mag)

    return magList

with open("rainfall.txt", "r") as rainFile:
    sum = 0
    count = 0

    for aLine in rainFile:
        values = aLine.split()
        count += 1
        sum += float(values[1])
        print(values[0], "had", values[1], "inches of rain")

    print("The average rainfall is: ", sum / count, "inches")

with open("rainfall.txt", "r") as rainFile:
    with open("rainfallInCM.txt", "w") as outFile:

        for aLine in rainFile:
            values = aLine.split()

            inches = float (values[1])
            cm = 2.54 * inches

            nChars = outFile.write(values[0] + " " + str(cm) + " cm" + "\n")

with open("earthquakes.csv", "r") as inFile:
    csvReader = csv.reader(inFile)
    titles = next(csvReader)
    colNum = 0
    while titles[colNum] != "mag":
        colNum = colNum + 1

print("The magnitude is found in column", colNum)

#print(makeDataList("mag"))

handle = urllib.request.urlopen("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_month.geojson")

data = handle.read()
eData = json.loads(data)

earthquakeList = eData.get('features')
print(len(earthquakeList))

print(makeMagList(eData))
