import os
os.system("clear")

nome = str(input("Nome: "))
sexo = str(input("""Informe o Sexo
F (feminino)
M (masculino): """))
estado_civil = str(input("Estado Civil: "))

match sexo:
    case "F":
         print(input("Tempo de casada (anos): "))
    case _:
         print("Aprovado.")

print(f"\nNome: {nome}")
print(f"\nSexo: {sexo}")
print(f"Tempo de Casado(a): ")

