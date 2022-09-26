vetor=[]

for i in range(10):
    num=int(input(f"Digite um numero({i+1}/10)-> "))
    vetor.append(num)
print(f"Vetor inserido-> {vetor}\n")
print(f"Maior valor encontrado no vetor-> '{max(vetor)}'")
print(f"O indice do maior valor-> '{vetor.index(max(vetor))}'")