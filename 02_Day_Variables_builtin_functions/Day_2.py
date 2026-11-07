import math

# Omondi Makalliwa
# 30 Days of Python
# Day 2: Variables

first_name = 'Omondi'
last_name = 'Makalliwa'
full_name = f'{first_name} {last_name}'
country = 'Kenya'
city = 'Nairobi'
age = 36
year = 1989
is_married = True
is_light_on = True
# Multiple variables on a single line
nickname = 'Max'; first_school = 'Moi Educational Centre'; home_town = 'Kisumu'

# Evaluate data types
datatype = {first_name :type(first_name),
            last_name :type(last_name),
            full_name :type(full_name),
                country :type(country),
            city :type(city),
            age :type(age),
            year :type(year),
            is_married :type(is_married),
            is_light_on :type(is_light_on),
            nickname :type(nickname),
            first_school :type(first_school),
            home_town :type(home_town),}

# Length of your first, last, and full name
len_first_name = len(first_name)
len_last_name = len(last_name)
len_full_name = len(full_name)

# Compare length of names
def name_length():
    if len(first_name) > len_first_name:
        print(f'First Name: {first_name}' f'is longer than {last_name}')
    elif len(last_name) > len(first_name):
        print(f'Last Name: {last_name}' f'is longer than {full_name}')
    elif len(first_name) == len(last_name):
        print(f'First Name: {first_name}' f'and Last Name: {last_name}' 'are equal')
    else:
        print("Review your names")

# Call name_length
name_length()

# Other variable declarations
num_one = int(input("Please enter a number: "))
num_two = int(input("Please enter another number: "))
# Operators
sum = num_one + num_two
difference = num_one - num_two
multiplication = num_one * num_two
division = num_one / num_two
modulus = num_one % num_two
exponent = num_one ** num_two
floor_division = num_one // num_two

# Circmumference and Area
radius = int(input("Please enter the radius: "))
circumference = 2 * math.pi * radius
area = math.pi * (radius**2)







