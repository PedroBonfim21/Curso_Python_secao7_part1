Vetor1=[]
for i in range (8):
    valor=int(input("Digite um valor-> "))
    Vetor1.append(valor)
    
x=int(input("Digite o valor da posicao do vetor-> "))
y=int(input("Digite o valor da posicao do vetor-> "))

soma=Vetor1[x]+Vetor1[y]
print(f"O valor da soma do Vetor1{x} e do vetor 1{y} e igual a -> {soma}")