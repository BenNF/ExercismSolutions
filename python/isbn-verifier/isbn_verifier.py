import itertools
def verify(isbn):
    isbn = isbn.replace('-',"")
    if (len(isbn) != 10): return False

    vals = []
    for x in isbn[:9]:
        if x.isdigit():
            vals.append(int(x))
        else:
            return False

    if isbn[9] == "X": vals.append(10)
    elif isbn.isdigit(): vals.append(int(isbn[9]))
    else: return False

    total = 0
    for i,j in zip(vals,range(1,11)[::-1]):
        total += i * j
    return total % 11 ==0

