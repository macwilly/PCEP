cities = ['Mumbai', 'Pune', 'New York', 'Chicago', 'Dallas']

# Normal for loop. But there is no access to indices
for city in cities:
    print(city)

for city_index in range(len(cities)):
    print(f'Current index: {city_index} | Current value: {cities[city_index]}')



spendings = [1346.0, 987.50, 1734.40, 2567.0, 3271.45, 2500.0, 2130.0, 2510.30, 2987.34, 3120.50, 4069.78, 1000.0]

lower_than_1k = 0
normal = 0
high = 0

for spending in spendings:
    if spending < 1000.0:
        lower_than_1k += 1
    elif 1000.0 <= spending <= 2500.0:
        normal += 1
    else:
        high += 1

print(f'Numbers of months with low spendings: {lower_than_1k}, normal spendings: {normal}, high spendings: {high}.')

print(57-39)