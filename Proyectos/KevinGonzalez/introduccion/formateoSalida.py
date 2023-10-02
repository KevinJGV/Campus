# Tipos de formatos de salida
# Format
sueldo = 609000
print("Sueldo: ${:,}".format(sueldo))

interes = 456486.5456123189489
print("Valor del interes: {:,.2f}".format(interes))

# f-string
print(f"Sueldo: ${sueldo:,}")
print(f"Valor del interes: {interes:,.2f}")