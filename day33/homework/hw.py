# 1)განიხილეთ ეს კოდი:

def word_len(sentance): #შევქმენით ფუნქცია და დავარქვით word_len,და პარამეტრებში გადავეცით sentance
    result = [] #შევქმენით ცვლადი და გავუტოლეთ ცარიელ სიას
    words = ""

    for i in sentance: # for ციკლით გადავუარეთ sentances
        if i != " ": # თუ საიტერაციო ცვლადი არ უდრის spaces
            words += i #words დაემატოს საიტერაციო ცვლადი
        else: #სხვა შემთვევაში
            result.append(words + str(len(words))) #words დაემატება wordis სიგრძე ოღნდ სტრინგად
            words = "" #გასუფთავება
    result.append(words + str(len(words))) #ანალოგიური result ზეც
    print(result) #დავპრინტავთ რეზულტს

word_len("Hello how are you") #გამოვიძახებთ ფუნქციას