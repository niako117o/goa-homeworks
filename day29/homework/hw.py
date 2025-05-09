# 1) შექმენით ფუნქცია რომელიც არგუმენტად მიიღებს სიას შემდეგ კი ამ სიიდან დააბრუნედ მხოლოდ კენტი რიცხვების ჯამი
def funct1(a):
    x = 0
    for i in a:
        if i % 2 != 0:
            x += 1
    print(x)
print(funct1([1,2,3,4,5,6,7,8,9]))

# 2) შექმენით ფუნქცია რომელიც მიიღებს სახელებით სავსე სიას შემდეგ კი დააბრუნეთ ყველა ის სახელი რომელიც შედგება მხოლოდ 4 ასოსგან
def name(nl):
    x = []
    for i in nl:
        if len(i) == 4:
            x.append(i)
    return x
print(name(['nodo','ჭipo','zaza','nodari']))

# 3) შექმენით ფუნქცია რომელიც მიიღებს რიცხვებით სავსე სიას შემდეგ კი გამოიტანეთ ისეთი რიცხვები რომლებიც იყოფა 3'ზეც და 5'ზეც
def numbers(nn):
    ff = []
    for i in nn:
        if i % 3 == 0 or i % 5 == 0:
            ff.append(i)
        return ff
print(numbers([15,30,6,9]))

# 4) ახსენით როგორ გამოიყენება f'სტრინგი
# name = 'niako'
# surname = 'simonia'
# print(f'hello my name is {name} and my surname is {surname}')



