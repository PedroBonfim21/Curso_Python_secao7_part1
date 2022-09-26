VetorA = []
VetorB = []
VetorC = []


for i in range(10):
    VetorA.append(int(input("Digite um valor A: ")))
    VetorB.append(int(input("Digite um valor B: ")))


for i in range(10):
    VetorC.append(VetorA[i] - VetorB[i])

print(f"\nDados do vetor C:")
print(*VetorC, sep=', ')