import string
def is_pangram(sentence):
    return set([x for x in sentence.lower() if x.isalpha()]) == set(string.ascii_lowercase)


