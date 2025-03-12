import os 
os.system("clear")

morango = 2.50
maca = 1.80

quantidade_de_morangos = float(input("Digite quantos morangos você deseja (kg): "))
quantidade_de_macas = float(input("Digite quantas maçãs você deseja (kg): "))
valor_base = morango + maca

if quantidade_de_morangos >5:
    morango = 2.20
elif quantidade_de_macas >5:
    maca = 1.50
else:
    valor_final = valor_base
    
if valor_base >15:
   valor_final = (valor_base * 0.10) 
   print("Foi aplicado um desconto.")
else:
   print("Não será Aplicado desconto.")

print(f"\nQuantidade de morangos comprada: {quantidade_de_morangos}")
print(f"\nQuantidade de maçãs comprada: {quantidade_de_macas}")
print(f"\nValor: {valor_base}")
print(f"\nValor com desconto: {valor_final}")



