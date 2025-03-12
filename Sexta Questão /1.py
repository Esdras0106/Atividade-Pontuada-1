import os
os.system("clear")

primeira_nota = float(input("Informe a primeira nota: "))
segunda_nota = float(input("Informe a segunda nota: "))
media = primeira_nota + segunda_nota / 2 

if media == 4:
      print("Aluno em recuperação!")
elif media >=6:
      print("Parabéns aluno aprovado!") 
elif media <4:
      print("Aluno reprovado.")     
else:       
      print("==FIM==")

print(f"\nPrimeira nota: {primeira_nota}")
print(f"Segunda nota: {segunda_nota}")
print(f"\nMédia: {media}")
