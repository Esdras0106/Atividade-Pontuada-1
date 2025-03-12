import os
os.system("clear")


operador = str (input("Informe a operação desejada (+ - / *): "))
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))

match operador:
    case "+":
        resultado = a + b
    case "-":
        resultado = a - b
    case "/":
        resultado = a / b
    case "*":
        resultado = a * b

print(f"\nValor de A: {a}")
print(f"\nValor de b: {b}")
print(f"\nOperação escolhida: {operador}")
print(f"\nResultado: {resultado}")
