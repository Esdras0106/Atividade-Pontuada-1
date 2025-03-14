import os
os.system("clear")

verde = ("10.00")
azul = ("20.00")
amarelo = ("30.00")
vermelho = ("40.00")

cd = str(input("Informe o cd (cor) desejado: "))

match cd:
    case "verde":
        print(f"\n O cd custa R$ 10,00")
    case "azul":
        print(f"\n O cd custa R$ 20,00")
    case "amarelo":
        print(f"\n O cd custa R$ 30,00")
    case "vermelho":
        print(f"\n O cd custa R$ 40,00")
    case _:
        print(f"\nOperação negada.")