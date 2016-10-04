restaurants = {}

data = """Pret,Sandwich,$,**,2
Brewhouse,Pub,$$,***,3
Jamies,Italian,$$$,*,1
Frederick's,British,$$$$$,*****,5"""
arr = data.split('\n')

# Line below is equivalent to: for line in data.split('\n'):

for line in arr:
	(name, type, cost, like, dist) = line.split(',')
	restaurants[name] = {"type": type, "cost": cost, "fave": like, "minutes":dist}

name = raw_input("Restaurant name: ")
#print data
#print arr
#print restaurants["Jamies"]["cost"]
#print restaurants[name]["cost"]

#Running the search until you specify you want to exit by writing 'exit' on the terminal as input

while name != "exit":
	print restaurants[name]["cost"]
	name = raw_input("Restaurant name-inner: ")


