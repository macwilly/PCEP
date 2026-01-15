# Key must be immutable. So it could be a string, int, or a tuple. But it cannot be a list
spanish_animals = {
    'dog': 'el perro',
    'cat': 'el gato',
    'horse': 'el caballo',
    'bird': ['el pajaro', 'el ave'],
    (1,): 'Something'
}
print(spanish_animals['dog'])
print(spanish_animals['bird'])
print(spanish_animals[(1,)])