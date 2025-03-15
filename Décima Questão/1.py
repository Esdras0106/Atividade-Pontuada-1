import os
os.system("clear")

litros_vendidos = float(input("Informe quantos litros você comprou: "))
tipo_de_combstivel = str(input("""Informe o tipo de combustível escolhido
A - ÁCOOL
G - GASOLINA: """)) 

match tipo_de_combstivel:
    case "A":
        total = litros_vendidos * 3.79
    case "G":
        total = litros_vendidos * 6.59
if total >= 25:
    valor = total * 0.02 
else:
    print("Sem Desonto.")

print(f"Quantidade (litros): {litros_vendidos}")
print(f"Tipo de combustível escolhido: {tipo_de_combstivel}")
print(f"Total a ser pago: {total}")
print(f"Valor Final: {valor: .2f}")
