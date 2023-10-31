def ordenar_key(dic):
    for clave,valor in dic.items():
        print(clave,valor)

listado = {"1": {"id": "1", "nombre": "asd", "precio": "1.0", "cantidad": "1"}, "2": {"id": "2", "nombre": "sdf", "precio": "2.0", "cantidad": "2"}, "3": {"id": "3", "nombre": "dfg", "precio": "3.0", "cantidad": "3"},"asdf": {"id": "1", "nombre": "asd", "precio": "1.0", "cantidad": "1"}}

list_ado = list()
a= ordenar_key(listado)
print(a)