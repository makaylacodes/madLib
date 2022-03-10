def madlib():
    emotion = input("Emotion: ")
    weather = input("Weather: ")
    color = input("Color: ")
    clothes = input("Clothes: ")
    food = input("Food: ")
    noun1 = input("Noun: ")
    noun_plural_1 = input("Noun (plural): ")
    adj1 = input("Adjective: ")
    adj2 = input("Adjective: ")
    adj3 = input("Adjective: ")


    madlib = f"One day I woke up feeling {emotion}, and I knew it was \
    going to be a special day. The sky was {color} and the weather was {weather}, so I hopped out of \
    bed, put on my {clothes}  "
    
    print(madlib)