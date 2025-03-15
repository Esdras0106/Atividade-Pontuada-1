import os
os.system("clear")

preco_morango_ate_5kg = 2.50
preco_morango_acima_5kg = 2.20
preco_maca_ate_5kg = 1.80
preco_maca_acima_5kg = 1.50

# Leitura da quantidade de morangos e maçãs comprados
kg_morango = float(input("Digite a quantidade de morangos em kg: "))
kg_maca = float(input("Digite a quantidade de maçãs em kg: "))

# Calculando o valor dos morangos
if kg_morango > 5:
    valor_morango = kg_morango * preco_morango_acima_5kg
else:
    valor_morango = kg_morango * preco_morango_ate_5kg

# Calculando o valor das maçãs
if kg_maca > 5:
    valor_maca = kg_maca * preco_maca_acima_5kg
else:
    valor_maca = kg_maca * preco_maca_ate_5kg

# Calculando o valor total da compra
valor_total = valor_morango + valor_maca

# Verificando se aplica o desconto de 10%
if kg_morango + kg_maca >= 10 or valor_total > 15.00:
    valor_total_com_desconto = valor_total * 0.90  # Desconto de 10%
    print(f"Você recebeu um desconto de 10%. O valor com desconto é R$ {valor_total_com_desconto:.2f}.")
else:
    print(f"O valor total a ser pago é R$ {valor_total:.2f}.")

