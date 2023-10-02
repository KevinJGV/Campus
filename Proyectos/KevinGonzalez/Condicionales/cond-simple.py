# Condicional simple

Sueldo = 1_100_000
SueldoMin = 1_160_000

if Sueldo <= SueldoMin:
    AuxTrans = 140000
else:
    AuxTrans = 0

print(f"Auxilio de transporte: ${AuxTrans:,}")