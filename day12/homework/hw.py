# 1)მომხმარებელს შემოატანინეთ რაღაც რიცხვი და შემდეგ შეამოწმეთ თუ ეს რიცხვი არის ლუწი,დაბეჭდეთ "even", ხოლო თუ კენტია "odd"
num = int(input("შეიყვანეთ რიცხვი: "))
if num % 2 == 0:
    print("even")
else:
    print("odd")

# 2)(გაიხსენეთ for ციკლი) for loop ის საშუალებით დაბეჭდეთ 1 დან 50მდე ყველა ლუწი რიცხვი

for i in range(1, 51):
    if i % 2 == 0:
        print(i, end=" ")

# 3)შექმენით სია შემდგარი რიცხვებისგან, გადაუარეთ for ციკლით და გამოიტანეთ მხოლოდ ის რიცხვები რომელიც მეტია 10ზე
numbers = [3, 15, 7, 20, 8, 11, 30, 5, 18, 2]
for num in numbers:
    if num > 10:
        print(num)


# 4)შექმენით  სია,რომელიც შედგება 10 რიცხვისგან  და შემდეგ დაბეჭდეთ პირველი და ბოლო ელემენტის სხვაობა,ჯამი,ნამრავლი
numbers = [2, 5, 8, 12, 15, 18, 22, 25, 30, 35]
first = numbers[0]
last = numbers[-1]

print("სხვაობა:", last - first)
print("ჯამი:", last + first)
print("ნამრავლი:", last * first)

# 5)(რთული)მომხმარებელს შემოატანინეთ რიცხვი და შეინახეთ ეს როცხვი ცვლადში, შემდეგ კი შექმენით სია რომელიც შედგება 5 სახელისგან,შემდეგ გამოიტანეთ შემოტანილი რიცხვის ინდექსზე მდგომი სიის ელემენტი.
index = int(input("enter number: "))
names = ["barbare", "guramiko", "lenini", "luka", "anna"]

if 0 <= index < len(names):
    print("siis elementi:", names[index])
else:
    print("wrong index!")
