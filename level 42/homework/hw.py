numbers = []
numbers.append(10)
numbers.append(20)
numbers.append(30)
numbers.insert(1, 15)
numbers.pop()
print(numbers)

def greetings():
    print("zd")
greetings()

def repeat_word(times, word):
    for _ in range(times):
        print(word)
repeat_word(3, "hello")


