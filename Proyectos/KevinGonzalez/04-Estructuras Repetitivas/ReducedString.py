'''def function'''
# abcaabbccaaabbbccc

def ReducedString(string):
    flag = ""
    i = 0
    string = string.lower()
    while i < len(string):
        if i == flag or i == flag[i:+1] or i == flag[i:-1]:
            i += 1
        elif i != flag:
            flag += string[i]
            i += 1
        


    return flag        
            

string = input("Ingrese cadena de caracteres conforme al ejercecio: ")
print(ReducedString(string))