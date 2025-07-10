# 2) დაწერე ფუნქცია, რომელიც ბეჭდავს "Hello, world!"
def greet():
    print('hello world')
greet()
# 3) დაწერე ფუნქცია, რომელიც იღებს სახელს და ბეჭდავს "Hello, [სახელი]!"
name = input('enter ur name')
def greet1():
    print(f'hello,{name}')
greet1()
# 4) დაწერე ფუნქცია, რომელიც იღებს ორ რიცხვს და აბრუნებს მათ ჯამს
def sum(a,b):
    return a + b
print(sum(3,5))
# 5) დაწერე ფუნქცია, რომელიც იღებს ერთ რიცხვს და აბრუნებს "Even" თუ ლუწია, ან "Odd" თუ კენტია
def numbers(num):
    if num % 2 == 0:
        return 'even'
    else:
        return 'Odd'
print(numbers(4))
# 6) დაწერე ფუნქცია, რომელიც იღებს სიის ელემენტებს და აბრუნებს მათ საშუალოს
def numberss(a,b,c):
    return (a + b + c) // 3
print(numberss(4,6,8))

# 7) დაწერე ფუნქცია, რომელიც იღებს სტრიქონს და აბრუნებს ამ სტრიქონის სიგრძეს
striqoni = input('sheiyvane sheni striqoni')
def length(str):
    return len(str)
print(length(striqoni))

# 8) დაწერე ფუნქცია, რომელიც იღებს სიას და აბრუნებს მას შებრუნებულ მდგომარეობაში
list1 = ['niako','nia', 'goa']
def list():
    if 2 > 1:
        return list1[::-1]
    else:
        print('error')
print(list())

# 9) დაწერე ფუნქცია, რომელიც იღებს სტრიქონს და აბრუნებს მას დიდ ასოებად გადაყვანილს
striqoni = input('sheiyvane sheni striqoni')
def length(str):
    return striqoni.upper()
print(length(striqoni))
# 10) დაწერე ფუნქცია, რომელიც იღებს ორ რიცხვს და აბრუნებს მათ შორის უმეტესს
def find_max(a, b):
    if a > b:
        return a
    else:
        return b
print(find_max(5,6))
# 11) დაწერე ფუნქცია, რომელიც იღებს რიცხვს და აბრუნებს True თუ ის უარყოფითია, False თუ არა
num = int(input('enter ur num: '))
def negative():
    if num < 0:
        print(True)
    else:
        print(False)
# 12) დაწერე ფუნქცია, რომელიც იღებს სიტყვების სიას და აბრუნებს სიის ყველაზე გრძელ სიტყვას. გამოიყენე ციკლი და 'len()' შედარებისთვის
words = ["apple", "banana", "kiwi", "strawberry"]
def find_longest_word(words):
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest
print(find_longest_word(words))

# 13) დაწერე ფუნქცია, რომელიც იღებს რიცხვს 'n' და აბრუნებს სიას 1-დან 'n'-ის ჩათვლით ყველა ლუწი რიცხვით. გამოიყენე for ციკლი და if-else
def even_numbers(n):
    evens = []
    for i in range(1, n + 1):
        if i % 2 != 0:
            continue 
        evens.append(i)
    return evens

# 14) დაწერე ფუნქცია, რომელიც იღებს სტრიქონს და აბრუნებს მასში ხმოვნების (a, e, i, o, u) რაოდენობას. გამოიყენე ციკლი და if-else
def count_vowels(text):
    text = text.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for letter in text:
        if letter in vowels:
            count += 1
    return count
print(count_vowels("Programming is awesome"))





