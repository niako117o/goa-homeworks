#პირველი საკლასო დავალება:
#1)
def niako(a,b):
    return a - b
print(niako(9,4))

#2)
def comment(a,b):
    return a + b
print(comment("niako","lamazia"))

#3)
def even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]
numbers = [1, 2, 3, 4, 5, 6, 9, 11, 24, 42]
print(even_numbers(numbers))

#MEORE SAKLASO DAVALEBA(codewars)
#link:https://www.codewars.com/kata/57356c55867b9b7a60000bd7/train/python
def basic_op(operator, value1, value2):
  if operator == '+':
    return value1 + value2
  elif operator == '-':
    return value1 - value2
  elif operator == '*':
    return value1 * value2
  elif operator == '/':
    return value1 / value2

#3
#link:https://www.codewars.com/kata/583710ccaa6717322c000105/train/python
def simple_multiplication(number):
    if number % 2 == 0:
        return number * 8
    else:
        return number * 9

