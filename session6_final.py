import csv

restaurants = {}

with open('restaurantData.csv') as csvfile:
    reader = csv.DictReader(csvfile)

    for rest_details in reader:

        print "\nprinting with restaurant name:"
        print rest_details # prints each restaurant detail in dictionary format

        restaurant_name = rest_details['name'] # store restaurant name in a new container

        del rest_details['name'] # delete the restaurant name from rest_details dictionary

        print "\nprinting without restaurant name:"
        print rest_details # this will print the rest_details dictionary with the name deleted

        # making a new dictionary using the name stored in our new container as key and the
        # dictionary without the restaurant name as the value
        restaurants[restaurant_name] = rest_details

print "\n print out new dictionary"       
print restaurants

