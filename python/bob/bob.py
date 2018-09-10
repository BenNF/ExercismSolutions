import string
def hey(phrase):
    phrase = phrase.strip()
    if (len(phrase) == 0):
        return "Fine. Be that way!"
    elif isYelling(phrase) and isQuestion(phrase):
        return "Calm down, I know what I'm doing!"
    elif(isYelling(phrase) and not isQuestion(phrase)):
        return "Whoa, chill out!"
    elif(isQuestion(phrase) and not isYelling(phrase)):
        return "Sure."
    else:
        return "Whatever."
def isYelling(phrase):
    if any(ch in phrase for ch in string.ascii_uppercase):
        return phrase.isupper()
    return False
def isQuestion(phrase):
    return phrase.endswith('?')
