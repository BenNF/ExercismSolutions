def slices(series, length):
    l = []
    if length <= 0 or length > len(series):
        raise ValueError("Error invalide slice length")

    for x in range(0,len(series)-length+1):
        l.append(series[x:x+length])
    l = [[int(x) for x in s] for s in l]
    return l
