# 1) შექმენით ფუნქცია რომელსაც გადასცემთ 2 არგუმენტს და შემდეგ დააბრუნეთ მათი ნამრავლი 
def niako(a,b):
    return a * b
print(niako(4,5))

# 2) შექმენით ფუნქცია რომელსაც არგუმენტად გადასცემთ ცვლადს სადაც შემდეგ შეინახავთ სახელს ფუნქციაში კი მიესალმეთ ამ სახელს 
def greet(name):
    print(f"gamarjoba, {name}!")
print(greet("mziko"))

# 3) შექმენით ფუნქცია რომელსაც მიანიჭებთ 3 არგუმენტს და გამოიტანეთ მათი ჯამი
def numbers(a,b,c):
    return a + b + c
print(numbers(1,2,3))
# 4) შექმენით ფუნქცია რომელსაც გადაეცემა 2 არგუმენტი და შემდეგ მათ გაუკეთეთ კონკატენაცია
def str(a,b):
    return a + ' ' + b
print(str('nia','lamazi'))

#მეორე საკლასო <3
#replace -ს ვიყენებთ ტექსტის შესაცვლელად
text = "hellow world"
new_text = text.replace("world", "friend")
print(new_text)

#Upper და lower
#upper ადიდებს მოცემულ წინადადებაში ყველა ასოს,მაგალითად:
name = 'niako'
new_name = name.upper()
print(new_name)
#და lower აპატარავებს ყველა სიტყვის ასოებს,მაგალითად:
name2 = 'niako'
new_name = name.lower()
print(new_name)

#find ფუნქცია,რომელიც ეძებს ჩვენს მითითებულ სიტყვას,მოცემულ წინადადებაში
name3 = 'nia lamazia'
new_name = name.find('l')
print(new_name)

#capitalize ადიდებს მოცემული სიტყვის პირველივე ასოს
name4 = 'niako'
new_name = name.capitalize()
print(new_name)

#swapcase პატარა ასოებს ადიდებს,ხოლო დიდებს,აპატარავებს
name4 = 'niako lamazi gogoa'
new_name = name.swapcase()
print(new_name)


