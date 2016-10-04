restaurants = {}
file_access = open("restaurant.csv",'r')
data = file_access.read()
file_access.close()
data = data.rstrip() #Will remove all white spaces from the "end", you can also specify a char

arr = data.split('\n')

for line in arr:
	(name, type, cost, like, dist) = line.split(',')
	restaurants[name] = {"type": type, "cost": cost, "fave": like, "minutes":dist}


name = raw_input("Restaurant name: ")
print restaurants[name]["cost"]

