destinations = {}

def add_destination(data):
    (city,distance,cost,country,like) = data.split(',')
    cost = int(cost)
    distance = int(distance)
    destinations[city] = {'distance': distance, 'cost':cost, 'country':country, 'rating':like}

with open("destinations.csv","r") as data_access:
    cities_information = data_access.read()
    #cities_information = cities_information.rstrip()

for city_data in cities_information.split('\n'):
    add_destination(city_data)

entered_dist = raw_input("maximum travel distance: ")
dist = int(entered_dist)

for place_name in destinations.keys():
    place_details = destinations[place_name]
    if place_details["distance"] <= dist:
        print "if you go to: " + place_name + " it'll set you back " + '$' * place_details['cost']
        if place_details["rating"] == 5:
            print place_name + " is one of my favourite places to visit"
        elif place_details["country"] == "USA":
            print place_name + " is in the USA - you'll need an ESTA"
        else:
            print place_name + " is " + str(place_details["distance"]) + " miles from London"
    # else:
    #     print "not working?"
