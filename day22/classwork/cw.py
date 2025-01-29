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

