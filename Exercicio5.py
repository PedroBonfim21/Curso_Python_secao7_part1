vetor=[]

for i in range(10):
    valor=int(input("Digite um valor-> "))
    
    if valor%2==0:
        vetor.append(valor)
print(f"Numero de valores pares-> '{len(vetor)}'")
print(f"vetor de numeros pares-> '{vetor}'")