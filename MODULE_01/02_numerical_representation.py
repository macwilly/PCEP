# To make large ints more readable you can split them with an underscore and when printed or interacted with they
# will be normal
int = 123_456_789
print(int)
new_int = int +  555_123
print(new_int)

# Also can do scientific notation
print(3E4)
print (3e-4)

# Python can also do octal number (this is on the exam and that is why it is review)
# They will start with 0o or 0O then the numbers that follow will be 0-7 (octal meaning base 8, starting at 0.)
print(0o7)
print(0o10)

# Python can also do hexadecimal number (this is on the exam and that is why it is review)
# They will start with 0x or 0X then the numbers that follow will be 0-9 then A-F (This is base 16)
print(0xB)