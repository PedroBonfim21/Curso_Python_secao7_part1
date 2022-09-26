vetor=[]
multiplo = []
for i in range(10):
    vetor.append(int(input("Digite um número: ")))

x = int(input("\nDigite um valor x: "))



for i in range(10):
    multiplo.append(x * vetor[i])

print(f"\nOs múltiplos de {x} de acordo com os valores digitados:")
print(*multiplo, sep=', ')
