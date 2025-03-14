import os
os.system("clear")

renda_mensal = float(input("Informe a sua renda mensal: "))
valor_emprestimo = float(input("Informe o valor do empréstimo solicitado: "))
numero_de_prestacoes = int(input("Informe em quantas prestações você deseja pagar: "))

limite_de_prestacoes = renda_mensal *0.30
limite = renda_mensal * 10
valor_prestacao = valor_emprestimo / numero_de_prestacoes

if valor_emprestimo >= limite:
    print(f"\n  EMPRÉSTIMO APROVADO.")
elif  valor_prestacao > limite_de_prestacoes:
    print(f"\n  O EMPRÉSTIMO NÃO PODE SER REALIZADO.")
else:
    print(f"\n  EMPRÉSTIMO APROVADO.")

print(f"\nRenda mensal: {renda_mensal}")
print(f"\nValor do empréstimo: {valor_emprestimo}")
print(f"\nNúmero de prestações: {numero_de_prestacoes}")
print(f"\nValor das prestações: {valor_prestacao}")