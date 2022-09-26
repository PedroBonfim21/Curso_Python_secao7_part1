vetor=[]
repetidos=[]
for num in range(10):
    vetor.append(int(input(f"Digite um valor({num+1}/10)-> ")))
for v in vetor:
    rep=vetor.count(v)
    if rep>1:
        repetidos.append(v)
del(repetidos[::2])

print(f"VALORES REPETIDOS:\n{repetidos}")
