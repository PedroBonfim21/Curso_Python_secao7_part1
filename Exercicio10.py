vetor=[]
for i in range(15):
    num=float(input(f"Digite a nota do aluno({i+1}/15)-> "))
    vetor.append(num)
media=sum(vetor)/15
print(f"O valor da media e-> {media}")