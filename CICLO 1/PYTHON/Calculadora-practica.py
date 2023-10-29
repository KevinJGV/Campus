# calculadora interactiva,verificar que se dio el primer numero, si no repetir que la ingrese, luego ingresar operacion, caso contrario pedir operacion, luego pedir otro numero, el resultado se va a guardad como el primer numero y continuara solicitando la operacion para el nuevo calculo.

salir = False
while not salir:
    dato1 = input("CALCULADORA\nIngresa 'salir' para finalizar o un número para operar: ")
    if dato1.lower() == "salir":
        salir == True
        break
    elif not dato1.isnumeric():
        print("Dato inválido. Ingresa un valor numérico para operar.")
        input()
        continue
    else:
        dato1 = int(dato1)
        
        while True:
            op = input("Qué operacion desea ejecutar\n  1 = suma\n  2 = resta\n  3 = multiplicación\n  4 = división\n  5 = modulo\n ")
            if op == "1":
                dato2 = input("Ingresa un número para operar con el primer ingreso: ")
                if dato2.isnumeric():
                    dato2 = int(dato2)
                    result = dato1 + dato2
                    print("Resultado final: ", result)
                else:
                    print("Dato inválido. Ingresa un valor numérico para operar.")
                    continue
            elif op == "2":
                dato2 = input("Ingresa un número para operar con el primer ingreso: ")
                if dato2.isnumeric():
                    dato2 = int(dato2)
                    result = dato1 - dato2
                    print("Resultado final: ", result)
                else:
                    print("Dato inválido. Ingresa un valor numérico para operar.")
                    continue
            elif op == "3":
                dato2 = input("Ingresa un número para operar con el primer ingreso: ")
                if dato2.isnumeric():
                    dato2 = int(dato2)
                    result = dato1 * dato2
                    print("Resultado final: ", result)
                else:
                    print("Dato inválido. Ingresa un valor numérico para operar.")
                    continue
            elif op == "4":
                dato2 = input("Ingresa un número para operar con el primer ingreso: ")
                if dato2.isnumeric():
                    dato2 = int(dato2)
                    result = dato1 / dato2
                    print("Resultado final: ", result)
                else:
                    print("Dato inválido. Ingresa un valor numérico para operar.")
                    continue
            elif op == "5":
                dato2 = input("Ingresa un número para operar con el primer ingreso: ")
                if dato2.isnumeric():
                    dato2 = int(dato2)
                    result = dato1 % dato2
                    print("Resultado final: ", result)
                else:
                    print("Dato inválido. Ingresa un valor numérico para operar.")
                    continue
print("PROGRAMA FINALIZADO.")