# 1) შემქენით ფუნქცია რომელიც მიიღებს სტრინგს და დააბრუნებს ამ სტრინგს დიდი ასოებით
upp = str(input('enter any string'))
def upper(upp):
    return upp.upper()
print(upper(upp))

# 2) მომხმარებელს შემოატანინეთ თავისი სახელი და გამოიტანეთ ამ სახელის პირველი ასო upper_case'ში 
name = str(input('enter your name: '))
def upper(name):
    return name.upper()
print(upper(name))

# 3) შექმენით ცვლადი სადაც შეიყვანთ რაღაც წინადადებას შემდეგ კი ამ წინდადებაში მოძებნდეთ თქვენთვის სასურველი სიტყვა 
def nia(a):
    return a.find(a)
print(nia('nia is prettiest'))
# 4) შექმენით ფუნქცია რომელიც მიიღებს 2 არგუმენტს შემდეგ კი გამოიტანეთ პირველი არგუმენტი რომელიც იქნება upper_case'ში ხოლო მეორე lower_case'ში და დაამეტეთ ეს არგუმენტები ერთმანეთს
def smth(a,b):
    return a.upper() + b.lower()
print(smth('nia', 'lamazi'))
# 5) დღეს ნასწავლ ყველა მეთოდზე გააკეთეთ 5-5 მაგალითი.
#upper 
def nia(a):
    return a.upper()
print(nia('nia'))
#lower
def nia(a):
    return a.lower()
print(nia('BANANA'))
#find
def nia(a):
    return a.find('ako')
print(nia('niako'))
#capitalize
def nia(a):
    return a.capitalize()
print(nia('dog'))
#split
def nia(a):
    return a.split('nia')
print(nia('nia is the prettiest girl'))
