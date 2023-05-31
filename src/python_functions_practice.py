def return_10():
    return 10

def add(a,b):
    return a+b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def length_of_string(string_input):
    return len(string_input)

def join_string(a,b):
    return a + b

def add_string_as_number(a,b):
    return (int(a) + int(b))

def number_to_full_month_name(number):
    months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    return months[number - 1]

def number_to_short_month_name(number):
    months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    return months[number - 1]

def volume_of_cube(length):
    return length ** 3

def reverse_string(string_input):
    return "".join(reversed(string_input))

def farenheit_to_celsius(temp):
    return (temp-32)/1.8
