# uppend - სიის ბოლოში ამატებს რაიმე ობიექტს - string ს
fav = ['kvara','zivzivadze','ramosi','ronaldo']
fav1 = fav.append('messi')
print(fav)

#pop - შლის ელემენტს სიიდან(დამოკიდებულია ინდექსზე)
fav2 = fav.pop(2)
print(fav)

# insert - ამატებს სიაში ჩვენს გადაცემულ ელემენტს(დამოკიდებულია ინდექსზე)

fav3 = fav.insert(2,'dvali')
print(fav)

#remove - შლის სიიდან ელემენტს(დამოკიდებულია მნიშვნელობაზე)
fav4 = fav.remove('kvara')
print(fav)


#2
def greet(name):
    return 'hii nice to meet you' + ' ' + name
print(greet('nia'))