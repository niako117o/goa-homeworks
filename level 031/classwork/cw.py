# ცვლადში შეინახეთ თქვენი სახელი. შემდეგ მომხმარებელს შემოატანინეთ თავისი სახელი და if-else statement-ების საშუალებით შეამოწმეთ ემთხვევა თუარა თქვენი სახელები ერთმანეთს. თუ ემთხვევა გამოიტანეთ - True, თუ არა - False.
name = 'niako'
name1 = str(input('enter ur name: '))
if name == name1:
    print('names are the same')
else:
    if name != name1:
        print('they are not same')

# თქვენს მიერ შექმნილი პროგრამა უნდა იყოს Case-insensitive. (ამისთვის გამოიყენეთ ჩამოთვლილი ფუნქციებიდან რომელიმე:
# upper()
# lower()
# capitalize()
b = str(input('enter ur word: '))
def upper(a):
    return a.upper()
print(upper(b))