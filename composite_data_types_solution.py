# Lab 8: Composite Data Type
# This exercise involves creating a data type that consists of a string inside a dictionary inside a list.
# The program reads an inventory from a csv file (carfleet.csv) and prints the inventory from the copy in memory. 
# it uses open syntax statement, which keeps a file open as long as you are reading data, it will automatically close the
# CSV file when the code inside the with block is finished executing.

import csv
import copy

#Exercise 1: Car Inventory

# Define a dictionary to hold our data.
myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>",
    "model" : "<empty>",
    "year" : 0,
    "range" : 0,
    "topSpeed": 0,
    "zeroSixty": 0.0,
    "mileage": 0
    }

# Print out the initial key and values.
for key, value in myVehicle.items():
    print("{} : {}".format(key,value))

# Define an empty list to keep a copy in memory.
myInventoryList = []

# Read the inventory from the csv file.
with open('car_fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    lineCount = 0
    for row in csvReader:
        if lineCount == 0:
            print(f'Column names are: {", ".join(row)}')
            lineCount += 1
        else:
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')
            currentVehicle = copy.deepcopy(myVehicle) # points to the storage location of the myVehicle dictionary variable
            currentVehicle["vin"] = row[0]
            currentVehicle["make"] = row[1]
            currentVehicle["model"] = row[2]
            currentVehicle["year"] = row[3]
            currentVehicle["range"] = row[4]
            currentVehicle["topSpeed"] = row[5]
            currentVehicle["zeroSixty"] = row[6]
            currentVehicle["mileage"] = row[7]
            myInventoryList.append(currentVehicle)
            lineCount += 1
    print(f'Processed {lineCount} lines.')

# Print the inventory from the copy in memory.
for myCarProperties in myInventoryList:
    for key, value in myCarProperties.items():
       print("{} : {}".format(key,value))
    print("-----")
                  
                  
 
# Without deepcopy, you would only have one storage box and only the last item in the list would be copied into memory. 
# it makes sure new storage boxes are created in memory to put the new tabular data being read in.
