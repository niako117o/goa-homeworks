#lower
word = input("enter ur word: ")
print(word.lower())

word1 = input("enter first words: ")
word2 = input("enter second word: ")
print(word1.lower() == word2.lower())

countries = ["Georgia", "Armenia", "Greece", "Norway", "Denmark"]

for country in countries:
    print(country.lower())

#upper
word = input("enter ur word: ")
print(word.upper())

countries = ["Georgia", "Armenia", "Greece", "Norway", "Denmark"]

for country in countries:
    print(country.upper())

word = input("enter ur word:")
if word.isupper():
    print("upper")
else:
    print("error")

#capitalize
sentence = input("enter smth: ")
print(sentence.capitalize())

word = "gEoRGia"
new_word = word.capitalize()
print(new_word)


countries = ["georgia", "aRMENIA", "greeCE"]
for country in countries:
    print(country.lower().capitalize())

#find
word = input("enter ur word: ")
position = word.find("a")
print(position)


text = "I visited Georgia, Armenia and Greece"
position = text.find("Armenia")
print(position)

text = "This is a test sentence about Python programming."
word = input("what are u looking for: ")

position = text.find(word)

if position != -1:
    print(position)
else:
    print("word not found")
