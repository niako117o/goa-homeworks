# მომხმარებლის სახელის შეყვანა
name = input("გთხოვთ, შეიყვანოთ თქვენი სახელი: ")

# იკითხება, როგორ უნდა შეცვალოს სახელი
choice = input("როგორ გსურთ სახელის შეცვლა? (lower/upper/capitalize): ").lower()

# მომხმარებლის არჩევის მიხედვით სახელის ცვლილება
if choice == "upper":
    print("თქვენი სახელი გადიდებულად: ", name.upper())
elif choice == "lower":
    print("თქვენი სახელი დაპატარავებულად: ", name.lower())
elif choice == "capitalize":
    print("თქვენი სახელი პირველი ასოს გადიდებით: ", name.capitalize())
else:
    print("მოცემული არჩევანი არასწორია.")





# #2)
# print = input('enter youre lastname ')
# if name == "simonia":
#     print('rogor xar?')
# else:
#     print('muwo req')

# #3)
# names = ['nia' , 'tamo' , 'saba' , 'anri']









