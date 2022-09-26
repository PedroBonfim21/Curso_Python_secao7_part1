vetor=[]
negativo=[]
positivo=[]
for i in range(10):
    num=float(input(f"Digite um numero({i+1}/10)-> "))
    if num<0:
        negativo.append(num)
    else:
        positivo.append(num)

print(len(negativo))
print(sum(positivo))