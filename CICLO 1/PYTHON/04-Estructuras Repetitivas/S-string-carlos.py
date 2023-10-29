a = "aaaabbbbcccd"
#a[3] = "z" NO SE PUEDE HACER.. Cadenas INMUTABLES
new_sec = ""
for i in range(1,len(a),2):
    print(i)
    new_sec += a[i]
    print(new_sec)