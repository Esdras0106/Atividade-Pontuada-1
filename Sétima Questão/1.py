import os 
os.system("clear")


produto = str(input("Informe o produto desejado: "))
quantidade = int(input("Quantidade adiquirida: "))
preco_unitario = float(input("Informe o valor do produto: "))

if quantidade <=5:
    desconto = (preco_unitario * 0.2) 
elif quantidade >5 <=10:
    desconto = (preco_unitario * 0.3)
elif quantidade >10: 
    desconto = (preco_unitario * 0.5)

total = preco_unitario - desconto

print(f"\nNome do produto: {produto}")
print(f"\nQuantidade adiquirida: {quantidade}")
print(f"\nPreço do produto: {preco_unitario}")
print(f"Desconto: {desconto}")
print(f"\nTOTAL: {total}")