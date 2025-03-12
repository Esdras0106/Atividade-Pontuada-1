import os
os.system("clear")

valor_a = int(input("Valor A: "))
valor_b = int(input("Valor B: "))
valor_c = ("Valor C: ")

if valor_a == valor_b:
   valor_c = valor_a + valor_b
else:
   valor_c = valor_a * valor_b

print(f"Valor A: {valor_a}")
print(f"Valor B: {valor_b}")
print(f"Resultado (C): {valor_c}")

        