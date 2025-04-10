#1)def ის გამოყენებით ჩვენ შეგვიძძლია შევქმნათ ფუნქცია.
#სტრუქტურა:
#  def anything(პარამეტრი):
#      return or print(გააჩნია რა დავალება გაქვს)
#გამოვიძახოთ 'anything' - > anything()

#2)
def str(a,b):
    return a + b
print(str('nia','lamazia'))

#3)
num = int(input('enter ur number:'))
def int(g,c):
    return (g + c) * num
print(int('shagu','xordela'))
#4)
def greet(name):
    print(f"hiiiiii, {name}!")
print(greet("mziko"))
#5)
def format_words(words):
    return f"{words[0]}; {words[1]}; {words[2]}."
my_words = ["mziko", "lasha", "cow"]
print(format_words(my_words))

