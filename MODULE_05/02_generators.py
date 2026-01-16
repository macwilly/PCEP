# The yeild makes this function a generator
def get_number():
    for i in range(1,4):
        yield i

gen = get_number()
print(next(gen))
print(next(gen))
print(next(gen))

for x in get_number():
    print(x)

numbers = list(get_number())
print(numbers)