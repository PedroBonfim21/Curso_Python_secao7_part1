vetor=[]

for i in range(10):
    valor=int(input("Digite um numero-> "))
    vetor.append(valor)

print(f"vetor informado->{vetor}")
vetor.sort()
print()
print(f"O menor valor lido na lista-> '{vetor[0]}'")
print(f"O maior valor lido na lista-> '{vetor[9]}'")