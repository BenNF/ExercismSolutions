def is_isogram(string):
    list = []
    string = string.lower()
    for x in string:
        if x in list:
            return False
        if (x.isalpha()):
            list.append(x)
    return True
