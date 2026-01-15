grades = {}

grades['John'] = 'A-'
grades['Anne'] = 'B'

print(grades)
grades['Anne'] = 'A'
print(grades)
grades.update({'John': 'A+'})
print(grades)

print(len(grades))

if 'Anne' in grades:
    print(f'Anne got',grades['Anne'])

for el in grades:
    print(el)

for el in grades.keys():
    print(el)

for el in grades.values():
    print(el)

for person,grades in grades.items():
    print(person,grades)
