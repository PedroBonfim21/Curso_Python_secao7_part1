vetor=[]

for i in range(5):
    num=int(input(f"digite um numero({i+1}/5)-> "))
    vetor.append(num)
print(f"vetor com todos os numeros-> '{vetor}'")
vetor.sort()
print(f"Menor valor do vetor-> '{vetor[0]}'\nMaior valor do vetor-> '{vetor[4]}'")

media=sum(vetor)/5
print(f"a média do vetor é-> '{media}' ")