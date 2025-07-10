# # 1) შექმენით სია სადაც ჩამოწერეთ 4 ბოსტნეულს, შემდეგ თქვენთვის ყველაზე 2 არასასურველი ამ სიიდან ჩაანცვლეთ ახალი ელემენტებით
vegetables = ["kartofili", "stafilo", "brokoli", "kombosto","xaxvi"]
vegetables[2]= 'badrijani'
vegetables[3]= 'pamidori'
print(vegetables)
# 2) მომხმარებელს შემოატანინეთ რიცხვი 0-იდან 4-მდე და შეინახეთ ის "user_cohice"-ის ცვლადში, შემდეგ ბოსტნეულსი სიიდან დაუბეჭდეთ ის ელემენტი რომელიც მომხმარებელმა აირჩია, ესეიგი იმ user_choice ინდექსზე მყოფი ელემენტი სიაში
user_choice = int(input('enter ur number: '))
print(vegetables[user_choice])
# 3) შექმენით 3 სხადასხვა ცვლადი რომელშიც შეინახავთ მომხმარებლის შემოტანილ 3 პროდუქტს. შემდეგ შექმენით სია სადაც ჩამოწერთ ამ პროდქუტებს, საბოლოოდ კი დაბეჭდეთ სია
a = str(input('chawere sheni produqti: '))
b = str(input('chawere sheni produqti: '))
c = str(input('chawere sheni produqti: '))
produqti = [a,b,c]
print(produqti)