# 2) შექმენით ცვლადი რომელშიც შეინახავთ თქვენს სახელს დიდი ასოებით, შემდეგ შექმენით ახალი ცვლადი new_name რომელშიც თქვენი სახელი ეწერება პატარა ასოებით, ჯერ გამოიყენეთ for ციკლი და if. შემდეგ კი გააკეთეთ ეს lower მეთოდით
name = "nia"
new_name = ""
for letter in name:
    if letter.upper():
        new_name += letter.lower()
    else:
        new_name += letter
print(new_name)


# 3) თქვენი სახელის სტრინგზე გამოიყენეთ მეთოდები: lower, upper, capitalize და დაბეჭდეთ. შემდეგ მოიყვანეთ .find მეთოდზე 3 მაგალითი თითოეულზე განსხვავებული შემთხვევით: მოიძნება, ვერ მოიძებნა, გამოიტანა error
name = "nia"

print(name.lower())  
print(name.upper())
print(name.capitalize())

text = "Hello, my name is nia"
index = text.find("name")
print(index)

