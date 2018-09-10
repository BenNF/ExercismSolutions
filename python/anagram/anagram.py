def detect_anagrams(word, candidates):
    return [x for x in candidates if isanagram(word.lower(),x.lower())]
def isanagram(first,second):
    if (len(first) != len(second)):
        return False
    if first == second:
        return False

    for x in first:
        if first.count(x) != second.count(x):
            return False
    return True