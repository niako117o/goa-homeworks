#1) We need a function that can transform a string into a number. What ways of achieving this do you know?
#https://www.codewars.com/kata/544675c6f971f7399a000e79/train/python
# "1234" --> 1234     
# "605"  --> 605
# "1405" --> 1405
# "-7" --> -7

def string_to_number(s):
    return int(s)

#2) Implement a function which convert the given boolean value into its string representation.
#https://www.codewars.com/kata/551b4501ac0447318f0009cd/train/python
def boolean_to_string(b):
    return str(b)

#3)Write a function which converts the input string to uppercase.
#https://www.codewars.com/kata/57a0556c7cb1f31ab3000ad7/train/python
def make_upper_case(s):
    return s.upper()

#4)Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.
# https://www.codewars.com/kata/53369039d7ab3ac506000467/train/python
def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    else:
        return "No"

#5)https://www.codewars.com/kata/55685cd7ad70877c23000102/train/python
# https://www.codewars.com/kata/55685cd7ad70877c23000102/train/python
def make_negative( number ):
    if number < 0:
        return number
    else:
        return -number

