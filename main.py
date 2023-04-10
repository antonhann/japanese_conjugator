typeOfConjugation = "0"
from helper import teForm
ruExceptions = ["kaeru", "aru", "okoru",]
uEndings = ["ru", "mu", "nu", "fu", "su", "bu","ku", "gu", "pu"] 
naExeptions = ["genki", "kirei"]
while True:
    while typeOfConjugation not in [1,2,3,4,5,6]:
        typeOfConjugation = int(input("1 - Present\n2 - Past\n3 - Te Form\n4 - Present Short\n5 - Past Short\n6 - Exit\nEnter Choice: "))

        if typeOfConjugation == 6: #exit
            break
    word = input("Enter word: ")
    exceptions = ["kaeru", "kiru", "aru", "okoru",]
    if typeOfConjugation == 1: #present

        irregulars = {
            "suru": "shimasu | shimasen",
            "kuru": "kimasu | kimasen"
        }
        if word in irregulars: 
            print(irregulars[word])
        elif word[-3:] in ["eru", "iru"] and word not in ruExceptions:
            print(f"{word[:-2]}masu | {word[:-2]}masen")
        elif word[-2] in uEndings and word[-3:] != "tsu":
            print(f"{word[:-1]}imasu | {word[:-1]}imasen")

    elif typeOfConjugation == 2: #PAST TENSE
        irregulars = {
            "suru": "shimashita | shimasendeshita",
            "kuru": "kimashita | kimasendeshita"
        }
        if word in irregulars:
            print(irregulars[word])
        elif word[-3:] in ["eru", "iru"] and word not in ruExceptions:
            print(f"{word[:-2]}mashita | {word[:-2]}masendeshita")
        elif word[-2] in uEndings and word[-3:] != "tsu":
            print(f"{word[:-1]}imashita | {word[:-1]}imasendeshita")
        else:
            print("invalid")
            
    elif typeOfConjugation == 3: #TE FORM 
        print(teForm(word))

    elif typeOfConjugation == 4: #SHORT FORM
        irregulars = {
            "suru": "suru | shinai",
            "kuru": "kuru | konai",
            "aru": "aru | nai"
        }
        if word in irregulars: 
            print(irregulars[word])
        elif word[-3:] in ["eru", "iru"] and word not in ruExceptions:
            print(f"{word} | {word[:-2]}nai")
        elif word[-1] == "u" and word[-2] in ["a", "e", "i", "o", "u"]:
            print(f"{word} | {word[:-1]}wai")
        elif word[-3:] == "tsu":
            print(word[:-3])
            print(f"{word} | {word[:-2]}anai")
        elif word[-2:] in uEndings and word[-4:] != "desu":
            print(f"{word} | {word[:-1]}anai")
        else:
            if word[-4:] == "desu":
                print(f"{word[:-4]}da | {word[:-4]}janai")
            elif word[-1] == "i" and word not in naExeptions:
                print(f"{word} | {word[:-1]}kunai")
            else:
                print(f"{word}da | {word}janai")

    elif typeOfConjugation == 5: #PAST SHORT FORM
    
        affirmative = teForm(word)[:-1]
        irregulars = {
            "suru": "shita | shinakatta",
            "kuru": "kita | konakatta",
            "aru": "atta | nakatta"
        }
        if word in irregulars: 
            print(irregulars[word])
        elif word[-3:] in ["eru", "iru"] and word not in ruExceptions:
            print(f"{affirmative}a | {word[:-2]}nakatta")
        elif word[-1] == "u" and word[-2] in ["a", "e", "i", "o", "u"]:
            print(f"{affirmative}a | {word[:-1]}wakatta")
        elif word[-3:] == "tsu":
            print(f"{affirmative}a | {word[:-2]}anakatta")
        elif word[-2:] in uEndings and word[-4:] != "desu":
            print(f"{affirmative}a | {word[:-1]}anakatta")
        else:
            if word[-4:] == "desu":
                print(f"{word[:-4]}datta | {word[:-4]}janakatta")
            elif word[-1] == "i" and word not in naExeptions:
                print(f"{word[:-1]}katta | {word[:-1]}kunakatta")
            else:
                print(f"{word}datta | {word}janakatta")
    
