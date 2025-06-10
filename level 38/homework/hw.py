# # 2) დეტალურად ახსენით რა არის ფუნქცია, რა არის არგუმენტი, როგორ ვიძახებთ ფუნქციას, რისთვის ვიყენებთ
#-----------------------
# ფუნქცია არის კოდის ბლოკი, რომელსაც ვიძახებთ რამდენჯერმე კონკრეტული ამოცანის შესასრულებლად.
# მაგალითად: print(), input(), len() — ეს ყველაფერი ფუნქციებია.
# არგუმენტი არის მონაცემი, რომელსაც ფუნქციას ვაწვდით მუშაობისთვის.

# 3) თითოეულ ფუნქციაზე რომელიც აქამდე ვისწავლეთ: print(), input(), type(), int(), str(), float(), range() შეასრულეთ 5 მაგალითი
print('nia')
print(6)
print(6.6)
print(True)

print(str('nia'))
print(str(8))
print(str(8.8))
print(str(True))

print(float('nia'))
print(float(2))
print(float(2,2))
print(float(False))

for i in range(5):
    print(i)

for i in range(1, 6):
    print(i)

for i in range(2, 10, 2):
    print(i)
# 4) დაწერეთ პროგრამა, რომელიც ითხოვს ორ რიცხვს მომხმარებლისგან. შემოაყვანინეთ მომხმარებელს დაწყების და დასრულების რიცხვი. თუ მეორე რიცხვი ნაკლებია პირველზე, გამოუტანეთ შეტყობინება: არასწორი შუალედი. სხვა შემთხვევაში დაბეჭდეთ ყველა რიცხვი მოცემულ შუალედში ჩათვლით და იპოვეთ ამ რიცხვების ჯამი. გამოიყენეთ for ციკლი, if-else პირობა, input ფუნქცია, და int ტიპში გადაყვანა
start = int(input("write en start number "))
end = int(input("write en stop number"))

if end < start:
    print("error")
else:
    total = 0
    for num in range(start, end + 1):
        print(num)
        total += num
    print(total)

# 5) შექმენით პროგრამა რომელშიც გექნებათ ხილის სია კალათა (list), 
# შემდეგ მომხარებელს შემოატანინეთ თავისი საყვარელი ხილი (input), 
# დაადეკლარირეთ ცვლადი რომელიც დაადგენს არის თუ არა ხილი 
# კალათაში (variable) fruit_in_basket რომლის მნიშვნელობა თავიდან 
# იქნება False, for ციკლის საშვალებით (for loop) განიხილეთ კალათა 
# და პირობითი განცხადების საშვალებით (if-else) შეადარეთ მომხარებლის 
# საყვარელ ხილს, თუ ისინი ტოლი იქნება fruit_in_basket ცვლადის 
# მნიშვნელობა შეცვალეთ True boolean-ით, საბოლოოდ პირობითი განცხადების 
# საშვალებით (if-else) შეამოწმეთ მომხმარებლის საყვარელი ხილი არის თუ 
# არა კალათაში fruit_in_basket, თუ არის დაუბეჭდეთ 'Good choice' თუ
# არ არის 'Fruit not in basket'
basket = ["ვაშლი", "ბანანი", "ატამი", "სტაფილო", "მსხალი"]
favorite_fruit = input("erter ur fav fruit")
fruit_in_basket = False

for fruit in basket:
    if fruit == favorite_fruit:
        fruit_in_basket = True
if fruit_in_basket:
    print("Good choice!")
else:
    print("Fruit not in basket.")


