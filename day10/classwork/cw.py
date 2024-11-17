# for loops
#1)გამოიტანეთ მხოლოდ კენტი რიცხვები 50-დან 150-მდე
for i in range(51,150,2):
    print(i)

#2)მომხმარებელს შემოატანინეთ რაიმე წინადადება და გამოიტანეთ ამ წინადადების თითოეული ასო ცალცალკე

proposal = "youre favorite proposal"
for i in proposal:
    print(i)


#WHILE LOOPS:
#1)გამოიტანეთ მხოლოდ ლუწი რიცხვები 500-დან 700-მდე

i = 500
while i<700:
    print(i)
    i = i + 2


#2)გამოიტანეთ რიცხვები 50-დან 0-მდე


i = 50
while i > 0:
    print(i)
    i = i - 1

#1)ცვლადში შეინახეთ თქვენი საყვარელი რიცხვი და მომხმარებელს შემოატანინეთ რიცხვი იქმადე სანამ არ დაემთხვევა თქვენს რიცხვს

favorite_number = 117
user_input = 0
while user_input != favorite_number:
    user_input = int(input("enter youre number: "))


