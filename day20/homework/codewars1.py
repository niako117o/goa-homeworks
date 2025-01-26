#1)Code as fast as you can! You need to double the integer and return it.
#https://www.codewars.com/kata/53ee5429ba190077850011d4/train/python
def double_integer(i):
    return (i) * 2

#2)Make a program that filters a list of strings and returns a list with only your friends name in it.
#If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...
#https://www.codewars.com/kata/55b42574ff091733d900002f/train/python
# Input = ["Ryan", "Kieran", "Jason", "Yous"]
# Output = ["Ryan", "Yous"]

# Input = ["Peter", "Stephen", "Joe"]
# Output = []
def friend(x):
    return [name for name in x if len(name) == 4]

#3)Given a non-empty array of integers, return the result of multiplying the values together in order. Example:
#https://www.codewars.com/kata/57f780909f7e8e3183000078/train/python
#[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24
def grow(arr):
    result = 1
    for num in arr:
        result *= num
    return result

#4)Write a function which calculates the average of the numbers in a given array.
#Note: Empty arrays should return 0.
#https://www.codewars.com/kata/57a2013acf1fa5bfc4000921/train/python
def find_average(numbers):
    if not numbers: 
        return 0
    return sum(numbers) / len(numbers)

#5)Messi goals function
#https://www.codewars.com/kata/55f73be6e12baaa5900000d4/train/python
def goals(laLiga, copaDelRey, championsLeague):
    return laLiga + copaDelRey + championsLeague

#6)Examples (Input -> Output):
#https://www.codewars.com/kata/56b1f01c247c01db92000076/train/python
def double_char(s):
    result = ""
    for char in s:
        result += char * 2
    return result

#7)Complete the function/method so that it returns the url with anything after the anchor (#) removed.
# https://www.codewars.com/kata/51f2b4448cadf20ed0000386/train/python
def remove_url_anchor(url):
  return url.split('#')[0]

#8)Write a function that takes a positive integer n, sums all the cubed values from 1 to n (inclusive), and returns that sum.
#https://www.codewars.com/kata/59a8570b570190d313000037/train/python
def sum_cubes(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i**3
    return sum
