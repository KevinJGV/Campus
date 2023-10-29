'''def function'''
# abcaabbccaaabbbccc

def ReducedString(string):
    newString = ""
    modif = False
    i = 0
    string = string.lower()
    while i < len(string):
        if i < len(string) - 2:
            if len(newString) == 0:
                if string[i] == string[i+1]:
                    newString = string[i+2:]
                    modif = True
                else:
                    i += 1
            else:
                break
        else:
            break
    while i < len(newString):
        if i < len(newString) - 2:
            if newString[i] == newString[i-1]:
                newString = newString[i+1:]
                modif = True
            elif newString[i] == newString[i+1]:
                newString = newString[:i] + newString[i+2:]
                modif = True
                i += 1
            else:
                i += 1
        else:
            break
    if not modif:
        return string
    if newString == "":
        return "Empty string"
    else:
        return newString

string = input("Ingrese cadena de caracteres conforme al ejercecio: ")
print(ReducedString(string))