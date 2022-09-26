lista = []
impares = []

for i in range(10):
    num = int(input("Digite um número no intervalo [0,50]: "))

    if (num >= 0) and (num <= 50):
        lista.append(num)

        if num % 2 == 1:
            impares.append(num)

print(f"\nPrimeiro vetor: ")
for i in range(0, len(lista), 2):
    print(f"{lista[i]}   ", end='')

    if len(lista) > i+1:
        print(lista[i+1])

print(f"\nSegundo vetor: ")
for i in range(0, len(impares), 2):
    print(f"{impares[i]}   ", end='')

    if len(impares) > i+1:
        print(impares[i+1])
