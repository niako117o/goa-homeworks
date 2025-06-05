# 2) კომენტარის სახით ჩამოწერეთ ყველა სტრინგის და სიის ფუნქცია რაც ვისწავლეთ და თითოეულს მიუწერეთ თუ რა დანიშნულება აქვს.
#______string fuctions__________
#upper - ჩვენს მოცემულ წინადადების/სიტყვის ყველა ასოს ადიდებს
#lower - upper - ის საპირისპიროა და იგი აპატარავებს ასოებს
#capitalize - ყოველი პირველი სიტყვის ასოს ადიდებს
#find - ფუნქცია,რომელიც ეძებს ჩვენს მითითებულ სიტყვას,მოცემულ წინადადებაში
#swapcase - პატარა ასოებს ადიდებს ხოლო პატარა ასოებს ადიდებს

# 3) ცვლადში შეინახეთ თქვენი გვარი. შემდეგ მომხმარებელს შემოატანინეთ გვარი. შეამოწმეთ თქვენი გვარები ემთხვევა თუ არა ერთმანეთს. თუ ემთხვევა ტერმინალში დაუბეჭდეთ - "Our surnames are similar." სხვა შემთხვევაში - "We have different surnames". ეს პროგრამა აუცილებლად Case Insensitive უნდა იყოს.
surname = 'simonia'
surname1 =str(input('enter ur surname: '))
if surname == surname1:
    print('Our surnames are similar.')
else:
    if surname != surname1:
        print("We have different surnames")
# 4) შექმენით სია სახელწოდებით food და მასში შეინახეთ არაჯანსაღი საკვები. .pop() და .append() ფუნქციების გამოყენებით სიიდან ამოაგდეთ არაჯანსაღი საკვები და ჩაამატეთ ჯანსაღი საკვები. დაბეჭდეთ საბოლოო სიის მნიშვნელობა.
foods = ['salati','cezari','badrijani','qatami']
while foods :
    foods.pop()
foods.append('lobiani')
foods.append('shaurma')
foods.append('xinkali')
foods.append('pica')
print(foods)
# 5) ცვლადში შეინახეთ სახელი. შემდეგ მომხმარებელსაც შემოატანინეთ თავისი სახელი. თუ თქვენი სახელების პირველი და ბოლო ასო ერთმანეთს დაემთხვევა გამოიტანეთ 2.
# თუ სახელის ან პირველი ან ბოლო ასო დაემთხვევა გამოიტანეთ 1. ყველა სხვა შემთხვევაში: 0.
name = 'niako'
name1 = input('enter ur name: ')
if name[0] == name1[0] and name[-1] == name1[-1]:
    print(2)
elif name[0] == name1[0] or name[-1] == name1[-1]:
    print(1)
else:
    print(0)
# BOSS LVL:
# Input() ის საშუალებით რამდენიმე მომხმარებელს შემოატანინეთ სახელი. ცვლადებში შეინახეთ მათ მიერ შემოტანილი სახელების Capitalized ვერსია. შექმენით names სია, რომელიც თავდაპირველად იქნება ცარიელი და თქვენი დავალება იქნება თითოეული სახელის შემოტანაზე დაამატოთ ეს სახელები სიაში, სიის თითოეულ განახლებაზე დაბეჭდეთ სია.
name3 = input('enter ur name: ')
name4 = input('enter ur name: ')
name3.capitalize()
name4.capitalize()
name = [name3,name4]
print(name)











