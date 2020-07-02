import json
import enchant

data = json.load(open("data.json"))
d = enchant.Dict("en_US")


def translate(word):
    word = word.lower()
    flag = d.check(word)
    if(flag):
        if word in data:
            return data[word]
        else:
            return "Word doesn't exists, kindly enter correct word!"
    else:
        print("Do you mean ?")
        print(d.suggest(word))


word = input("Enter word :")
output = (translate(word))

if type(output) == list:
    for i in range(len(output)):
        print(output[i])
else:
    print(output)
