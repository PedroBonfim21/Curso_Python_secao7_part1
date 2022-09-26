vetor=[]

for i in range(6):
    num=int(input(f"Digite um numero({i+1}/6)-> "))
    vetor.append(num)
vetor.reverse()
print(f"Vetor invertido-> {vetor}")