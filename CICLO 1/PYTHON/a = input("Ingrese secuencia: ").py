a = input("Ingrese secuencia: ")




i = True
f = 0
new_sec = "" 

while i == True:
    if new_sec == "":
        if a[f] == a[f+1]:
            new_sec = a[f+2:]
            print(new_sec)
            x = "check" 



        else:
            new_sec = a
            print(new_sec)
            x = "no-check"



    if x == "check":
        f = f

    elif x == "no-check":
        f += 1

    if f < (len(new_sec)-1):
        if new_sec[f] == new_sec[f+1]:
            new_sec = new_sec[:f] + new_sec[f+2:]
            #new_sec =  new_sec[f+2:]
            print(new_sec)
            x = "check"

        elif new_sec[f] == new_sec[f - 1]:
            new_sec = new_sec[:f-1] + new_sec[f+1:]
            #new_sec =  new_sec[f+2:]
            print(new_sec)
            x = "check"

        else:
            new_sec = new_sec
            print(new_sec)
            x = "no-check"

        if new_sec == "":
            new_sec = "Secuencia vacia"

    elif f == len(new_sec)-1:
        if new_sec[f] == new_sec[f-1]:
            new_sec = "Secuencia vacía"

    else:
        i = False


print(f"secuencia: {a}")