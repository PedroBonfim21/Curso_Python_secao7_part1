vetor=[]
mai=0
men=0
for i in range(5):
    vetor.append(int(input("Digite um número: ")))
    if i==0:
        mai=men=vetor[i]
    else:
        if vetor[i]>mai:
            mai=vetor[i]
        if vetor[i]<men:
            men=vetor[i]
print(f"\nO maior valor digitado foi->{mai}\nEle aparece nas posições->", end='')
for c,v in enumerate(vetor):
    if v==mai:
        print(f"'{i}',")
print(f"\nO menor valor digitado foi->{men}\nEle aparece nas posições->", end='')
for c,v in enumerate(vetor):
    if v==men:
        print(f"'{i}',")
print()
