# 1)შექმენით სია 10 ელემენტით, შემდეგ მომხმარებელს შემოატანინეთ ორი რიცხვი და იმ ორი რიცხვის დიაპაზონში გამოიტანეთ ელემენტები სიიდან
name = ['nia', 'giorgi', 'luka', 'nini' 'tamari' , 'nika' 'nikoloz' 'lizi', 'keso', 'mariami']
number = int(input('შეიყვანე სახელი: '))
number2 = int(input('შეიყვანე სახელი: '))
print(name[number:number2])



#2)შექმენით სია 5 ელემენტით, შემდეგ მომხმარებელს შემოატანინეთ ერთი რიცხვი და იმ ინდექსზე მდგომი ელემენტი გამოიტანეთ სიიდან

name = ['nia', 'giorgi', 'luka', 'nini' 'tamari']
number = int(input('შეიყვანე ინდექსი: '))
print(name[number])


#3)მომხმარებელს შემოატანინეთ მისი სახელი, ცვლადში შეინახეთ თქვენი სახელი და საბოლოოდ დაბეჭდეთ მომხმარებლის პირველ 3 ასოს დამატებული თქვენი სახელის ბოლო 2 ასო
user_name = input('please enter youre name: ')
name = 'niako'
print(user_name[:2]) + (name[2:])


# 4)კომენტარის სახით ახსენით რა განსხვავებაა indexing და slicing შორის
# Indexing საშუალებას გაძლევთ, აირჩიოთ კონკრეტული ერთი ელემენტი მონაცემთა სტრუქტურიდან ინდექსის მიხედვით.
# Slicing გამოიყენება ელემენტების ჯგუფის ან ქვეწარმოების გამოსაყოფად კონკრეტული ინდექსის დიაპაზონის გამოყენებით.


# 5)მომხმარებელს შემოატანინეთ მისი გვარი, შექმენნით ახალი ცვლადი სადაც შეინახავთ მის გვარს ოღონდ შებრუნებულად და საბოლოოდ დაბეჭდეთ ორივე ცვლადი
user_name = input('enter youre lastname: ')
reversed_user_name = (user_name[::-1])
print(reversed_user_name)