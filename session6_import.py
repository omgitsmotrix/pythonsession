
import csv

print "\nWithout headers, file is read as a list:\n"
with open('restaurant.csv') as csvfile:
    reader = csv.reader(csvfile)

    for row in reader:
        print row
        # print row[0], row[1], row[2], row[3], row[4]
