top_us_cities = ['New York', 'Los Angeles', 'Singapore','Chicago', 'Houston', 'Phoenix']
del top_us_cities[2]
print(top_us_cities)

del top_us_cities[3:]
print(top_us_cities)

# TO clear the list del with empty slice
del top_us_cities[::]
print(top_us_cities)

# to delete the list  del <list>
del top_us_cities
print(top_us_cities)