import time
import sys
import string

alphanumeric = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def to_decimal(number_string, original_base):
    if number_string == '0':
        return 0
    
    total = 0

    for c in range(len(number_string)):
        total += alphanumeric.index(number_string[-(c+1)])*(original_base**c)
    
    return total


def from_decimal(decimal_number, target_base):
    if decimal_number == 0:
        return '0'
    
    converted = ''

    while decimal_number > target_base:
        converted = str(alphanumeric[decimal_number % target_base]) + converted
        decimal_number = decimal_number // target_base
    
    converted = str(alphanumeric[decimal_number]) + converted
    return converted


def base_input_validation(base):
    if not base.isnumeric():
        return base_input_validation(input("Please make sure your base is a number"))
    elif int(base) > 36 or int(base) < 2:
        return base_input_validation(input("Please make sure your base from 2-36(inclusive)"))
    return base
    

def number_input_validation(number, base):
    number = number.upper()
    if not number.isalnum():
        return number_input_validation(input("Only alphanumeric values please, I don't have forever "),base)
    elif not set(number) <= set(alphanumeric[0:(int(base))+1]):
        return number_input_validation(input("Make sure that your number is in the correct base "),base)
    return number


if __name__ == '__main__':
    while True:
        print("Welcome to the abode of the hexorcist, I see not only did you not want to do the calculation yourself, or just google it, but went out of your way to get a python script to do it!\n")
        print("Well i guess lets do this then since you put so much work in to get here\n")

        original_base = base_input_validation(input("Alright, well what base is it in?(2-36) ")).upper()
        original_number = number_input_validation(input("Well get on with it, what's your number? "),original_base)
        for c in '\nPython scripting your results\n':
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.1)

        print()

