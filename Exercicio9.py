vetor=[]

for i in range(6):
    num=int(input(f"Digite um numero({i+1}/6)-> "))
    
    if num%2==0:
        vetor.append(num)
vetor.reverse()
print(f"O vetor de numeros pares em ordem reversa-> '{vetor}' ")