import os
os.system("clear")

valor_a = int(input("Informe o valor A: "))
valor_b= int(input("Informe o valor B: "))
valor_c= int(input("Informe o valor C: "))

resultado = valor_a + valor_b

if resultado < valor_c:
    print("É menor que C")
else:
    print("Não é menor que C")

print(f"\nValor A: {valor_a}")
print(f"\nValor B: {valor_b}")
print(f"\nValor C: {valor_c}")

print(f"\nResultado: {resultado}")
