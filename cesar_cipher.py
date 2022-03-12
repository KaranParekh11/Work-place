def enfunc(txt, s):
    result = ""
    # transverse the plain txt
    for i in range(len(txt)):
        char = txt[i]
        if (char.isupper()):
            result += chr((ord(char) + s ) % 256)
            # encypt_func lowercase characters in plain txt
        else:
            result += chr((ord(char) + s ) % 256)
    return result
def decfunc(txt1, s):
    result1 = ""
    # transverse the plain txt
    for i in range(len(txt1)):
        char = txt1[i]
        if (char.isupper()):
            result1 += chr((ord(char) -s ) % 256)
            # encypt_func lowercase characters in plain txt
        else:
            result1 += chr((ord(char) - s ) % 256)
    return result1
txt="KARkaran123@#$"
txt1="NDUndudq456C&'"
s=3
print(enfunc(txt,s))
print(decfunc(txt1,s))