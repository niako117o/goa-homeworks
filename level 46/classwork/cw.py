# 1) შექმენით ფუნქცია რომელიც დაადგენს პარამეტრად გადაცემული n რიცხვი ლუწია თუ კენტი, იმის მიხედვით დააბრუნებს მნიშვნელობა
# 'Even' ან 'Odd'. ფუნქცია გამოიძახეთ მინიმუმ 4-ჯერ და შეამოწმეთ როგორც ლუწი ისე კენტი რიცხვები
def even_or_odd(s):
    if s % 2 == 0:
        return 'even'
    else:
        return 'odd'
print(even_or_odd(6))
print(even_or_odd(11))
print(even_or_odd(5))

#bonus classwork
# შეამოწმე რიცხვი დადებითია თუ უარყოფითი, თუ დადებითია შეამოწმე ლუწია თუ კენტი და სამივე შემთვევაში დააბრუნე შედეგი შესაბამისად
def negative_or_positive(n):
    if n < 0:
        return 'the n is negative'
    elif n > 0:
        if n % 2 == 0:
            return 'its positive'
    else:
        return 'none'
print(negative_or_positive(-3))
print(negative_or_positive(2))
print(negative_or_positive(11))



