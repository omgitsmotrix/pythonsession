
import csv

# Before starting this make a new csv file with column titles for the restaurants data.

print "\nWith headers/column-titles you can read the file as a dictionary:\n"

with open('restaurantData.csv') as csvfileTwo:
    reader = csv.DictReader(csvfileTwo)
    for row in reader:
        print row
        # print row['name'], row['type'], row['cost']


# Note how differently a dictionary and a list is printed
# A dictionary prints with {} , but a list prints with [] 
# Has a direct relation with the way you specify the Data Type