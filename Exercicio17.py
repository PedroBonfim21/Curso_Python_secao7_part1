vetor=[]

for value in range(5):
    num=int(input(f"Digite um numero({value+1}/5)-> "))
    if num < 0:
        vetor.append(0)
    else:
        vetor.append(num)

print(f"Vetor completo-> {vetor}")