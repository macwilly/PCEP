def get_factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

print(get_factorial(5))

def get_factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * get_factorial_recursive(n - 1)

print(get_factorial_recursive(6))