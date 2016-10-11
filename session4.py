
file_access = open("restaurant.csv",'r')
data = file_access.read()
file_access.close()
data = data.rstrip()

def read_restaurant(row):
	(name,type,cost,fave,dist) = row.split(",")
	restaurants[name] = {"type":type, "cost":cost, "fave":fave, "dist":dist}


restaurants = {}

for line in data.split("\n"):
	read_restaurant(line)

#print restaurants["pret"] #1.1

entered_dist = raw_input("Maximum distance: ")
dist = int(entered_dist)

#for restName in restaurants.keys():
#	details = restaurants[restName] #1.1 returns a dictionary containing values of the indexed restaurant
#	if int(details["dist"]) <= dist:
#		print '\n' + restName + " distance is less than you specified - GoGoGo!\n"


print '\n' + str(restaurants.keys()) +'\n'

for restName in restaurants.keys():
	details = restaurants[restName] 
	if int(details["dist"]) <= dist:
		print '\n' + restName + " distance is less than you specified - GoGoGo!\n"
		if details['type'] == "sandwich":
			print restName + " serves sandwiches"
		elif details['fave'] == "1":
			print " ... AWFULL RESTAURANT"
		else: # do this if none of the above conditons match
			star_rating = int(details['fave'])
			print restName + " Its rated as " + str(star_rating) + " " + star_rating *  "*"

# Output:
#
# pret distance is less than you specified - GoGoGo!
# pret serves sandwiches
# Jamie's Italian distance is less than you specified - GoGoGo!
# ... AWFULL RESTAURANT
# brewhouse distance is less than you specified - GoGoGo!
# brewhouse Its rated as 3

