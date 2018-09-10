from collections import OrderedDict
import string
def word_count(phrase):
    words = [word.strip(string.punctuation) for word in phrase.lower().replace("_", " ").replace(","," ").replace(":"," ").split()]
    return {x : words.count(x) for x in list(OrderedDict.fromkeys(words))}
