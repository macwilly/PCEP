try:
    value = int(input("Enter a number: "))
    print(f'The inverse of {value} is {1 / value}')
except ValueError:
    print('You did not provide a number.')
# except ZeroDivisionError:
#     print('We cannot divide by zero.')
except Exception as e:
    print("Exception type:", type(e))  # shows the class
    print("Exception name:", type(e).__name__)