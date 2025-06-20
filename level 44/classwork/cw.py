#1th classwork
def multiply (a,b):
    return a * b
product1 = multiply(3, 4) 
product2 = multiply(7, 5)  
product3 = multiply(10, 2)
print(product1)
print(product2)
print(product3)


#2th classwork
def hello(name):
    print("Hello", name)
my_name = hello("Niako")
print(my_name) 
# ფუნქცია hello() ბეჭდავს ტექსტს, მაგრამ არ აბრუნებს (return) არაფერს.
# Python-ში, როცა ფუნქციას არ აქვს return, იგი ავტომატურად აბრუნებს None.
# ამიტომ my_name = None ხდება, რადგან hello("Niako") არაფერი დააბრუნა. 

# print() – აჩვენებს შედეგს ეკრანზე ანუ ტერმინალში
# return – აბრუნებს მნიშვნელობას ფუნქციიდან, რათა შემდგომ გამოვიყენოთ ანუ (შევინახოთ, ვამუშავოთ)

