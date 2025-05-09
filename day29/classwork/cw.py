# შექმენით ფუნცქიცა რომელსაც გადასცემთ რაღაც სახელს შემდეგ გადაუარეთ ამ სახელს for loop'ით და დააბრუნეთ თითოეული ელემენტი upper ქეისში
name = str(input("enter your name: "))
def name1(name):
    for letter in name:
        print(letter.upper())
name1(name)
def list(my_list):
    for element in my_list:
        print(element)
friends = ["niako", "andria", "tamo"]
list(friends)
print('55' * 2)

