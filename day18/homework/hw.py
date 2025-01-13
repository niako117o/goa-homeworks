#1)შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა ორი რიცხვი შემდეგ კი გამოიტანეთ ამ რიცხვების ნამრავლი.

def niangi(num1 , num2):
    return num1 * num2

print(niangi(2,3))

#2)შექმენით ფუნქცია რომელსაც გადაეცემა არგუმენტად რიცხვი შემდეგ კი მან უნდა დაგვიბრუნოს ლუწია ეს რიცხვი თუ კენტი.

def tarakana(num1):
    if num1 > 0:
        print("even")
    elif num1 > 7:
        print("odd")
tarakana(6)

#3)შექმენით ფუნქცია, რომელსაც არგუმენტად გადაეცემა სახელი და დაბეჭდავს მისთვის მიესალმებას (მაგალითად: "Hello Giorgi"). გამოძახეთ ეს ფუნქცია 2-ჯერ და გადაეცით სხვადასხვა სახელი.
def name1(namee):
    return "Hello" + " " + namee


print(name1("Niako"))
print(name1(namee="Giorgi"))
print(name1(namee="Barbare"))

#4)შექმენით ფუნქცია, რომელიც იღებს ორ სტრინგს და მოახდინეთ კონკატენაცია.
def drakoni(str1 , str2):
    print(str1 + str2)
drakoni("ice" , "cream")

