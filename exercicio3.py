A=[]
cont=0
B=[]
while (cont<10):
    cont+=1
    valor=float(input("Digite o valor a ser adicionado ao conjunto -> "))
    A.append(valor)

for quadrado in A:
    quadrado=quadrado**2
    B.append(quadrado)

print(f"Vetor dos conjuntos de numeros reais->{A}\n")
print(f"vetor de quadrado dos componentes->{B}\n")