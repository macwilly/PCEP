# In most languages you need a temp var to swap two values.
# You have A and B and you want A = B and B = A so you us a temp c

# A = int(input('Enter the first number: '))
# B = int(input('Enter the second number: '))
#
# print(A,B)
# C = A
# A = B
# B = C
# print(A,B)
# # Python you can do this in open line without a temp
# A, B = B, A
# print(A,B)

cities = ['New York', 'Chicago', 'Los Angeles', 'Dallas']

cities[0], cities[1] = cities[1], cities[0]
print(cities)

#list function sorted() takes a list as a parameter and returns a sorted list. doesn't change the original
print(sorted(cities))
print(cities)

#list method <list>.sort() will update the original list to a sorted version losing the original copy
cities.sort()
print(cities)