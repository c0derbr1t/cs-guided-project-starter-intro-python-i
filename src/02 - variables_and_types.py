"""
Variable and Types
"""
print("#1: ")
# 1. Integers
myint = 9
print(myint)

print("#2: ")
# 2. Floating point numbers
myfloat = 7.245
print(myfloat)
myfloat = float(7)
print(myfloat)

print("#3: ")
# 3. Strings can use " or '
# convention is "" so if you need to use ', but it doesn't matter.
mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)

print("#4: ")
# 4. Apostophes
mystring = "Don't worry about apostrophes"
print(mystring)

print("#5: ")
# 5. Simple Operations
one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

print("#6: ")
# 6. Simultaneous assignemnt
a, b = 3, 4
print(a, b)

print("#7: ")
# 7. Can avoid temp pattern
a = 3
b = 4
print(a, b)
temp = a
a = b
b = temp
print(a, b)

a = 3
b = 4
print(a, b)
a, b = b, a
print(a, b)

print("#9: ")
# 8. Mixing operators with strings and numbers
# This will not work! ->  print(one + two + hello)
one = 1
two = 2
hello = "hello"

print(str(one) + str(two) + hello)
