# value
# data types
# input

# number: 1, 2, -1, 0 (int - so nguyen), 1.25, 3.14, 0.0 (float)
# string: "hello", 'main'
# boolean: True False

print(type(1)) # int
print(type(1.25)) # float
print(type('')) # str
print(type(True)) # bool

# variables
x = 5
print(type(x)) # int

x = 6
print(x) # int

_ = 6
print(_) # int

# input -> str

full_name = input("Nhap ten: ")
print(full_name)

number = input("Nhap so nguyen: ")
number_as_int = int(number)
print(type(number_as_int))
print(number_as_int + 3)

# so phuc (a + bj)
print(type(1 + 2j))

# --------------------------------

# Operators
# + - * / // ** %
print(1 + 2)
print(1 - 2)
print(1 * 2)
print(1 / 2) # float
print(1 // 2) # int
print(1 ** 2) # mu
print(1 % 2) # lay phan du

# > < >= <= == !=
# bool --- True/False

# and or not
print(True and True) # True
print(True and False) # False
print(False and False) # False
print(False and True) # False

print(True or True) # True
print(True or False) # True
print(False or False) # False
print(False or True) # True

print(not True) # False
print(not False) # True

print(bool(0)) # False
print(bool(1)) # True
print(1 and 2) # 2

print(0 or 2) # 2
print(1 or 2) # 1

print(not 1) # False
print(not 0) # True

# falsy: 0, 0.0, 0j, None: no value
# list: []
# set: set()
# dict: {}
# tuple: ()
# empty string: '' = ""
# bool(falsy) = False
print(bool(None)) # False

# +=, -=, *=, /=, //=, %=, **=

x = 5

x += 5 # x = x + 5
x -= 9
x *= 12


print('x =', x)

age = 30
age_as_str = str(age)
print('I am ' + age_as_str)
# f-strings
print(f"I am {age}")
print('I am {}'.format(age))

s = 'hello world!'
s = s.upper()
s = s.capitalize()
s = s.title()
s = s.lower()
print(s)

lst =  s.split()
print(lst)