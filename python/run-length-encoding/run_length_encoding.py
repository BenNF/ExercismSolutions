def decode(string):
    i, n, t = 0, len(string), ''
    while i < n:
        m = ''
        while string[i].isdigit():
            m += string[i]
            i += 1
        if m:
            t += int(m) * string[i]
        else:
            t += string[i]
        i += 1
    return t


def encode(string):
    if len(string) <= 0: return ""
    char = string[0]
    count = 0
    output = ""
    for x in string:
        if x == char:
            count+=1
        else:
            if (count > 1):
                output += str(count)
            count = 1
            output += char
            char = x
    if count > 1:
        output += str(count)
    output += char
    return output

print(encode("AAAABBBBCCCC"))
print(decode("4A4B4C6 G"))