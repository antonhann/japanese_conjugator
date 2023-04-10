ruExceptions = ["kaeru", "kiru", "aru", "okoru",]
def teForm(word):
    irregulars = {
        "suru": "shite",
        "kuru": "kite",
        "iku": "itte"
    }
    if word in irregulars:
        return(irregulars[word])

    elif word[-3:] in ["eru", "iru"] and word not in ruExceptions:
        return(f"{word[:-2]}te")

    elif word[-2:] == "ku":
        return(f"{word[:-2]}ite")

    elif word[-2:] == "gu":
        return(f"{word[:-2]}ide")

    elif word[-2:] == "su" and word[-3] != "t":
        return(f"{word[:-2]}shite")

    elif word[-2:] in ["mu","bu","nu"]:
        return(f"{word[:-2]}nde")
    elif word[-3:] == "tsu":
        return(f"{word[:-2]}te")
    elif word[-2:] == "ru":
        return(f"{word[:-2]}tte")
    elif word[-1] == "u":
        return (f"{word[:-1]}tte")
