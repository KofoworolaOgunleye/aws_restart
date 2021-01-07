# Lab 7: Categorize values into an appropriate data type
# This program prints the datatype of each value stored in myMixedbagList using for loop to loop
# through the list and the format method

# Exercise 1: Mixed Bag
myMixedBagList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]

for item in myMixedBagList:
    print("{} is of data type {}".format(item,type(item)))
