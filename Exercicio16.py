vetor=[]

for num in range(5):
    vetor.append(int(input(f"Digite um numero ({num+1}/5)-> ")))

print('-'*30)
print("Escolha uma das opcoes a baixo:\n")
print("1-Vetor em ordem;\n2-Vetor invertido;\n")

seletor=int(input('Digite sua escolha aqui-> '))
print('-'*40)
if seletor == 1:
    vetor.sort()
    print(f"\nVetor em ordem-> '{vetor}' ")

elif seletor == 2:
    vetor.sort()
    vetor.reverse()
    print(f"\nVetor em ordem inversa-> '{vetor}' ")
else:
    print("Opcao invalida!")