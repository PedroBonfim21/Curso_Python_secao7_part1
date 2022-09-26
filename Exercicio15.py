lista = []
no_repeat=[]

for i in range(20):
    lista.append(int(input(f"Digite um valor {i+1}/20)->: ")))
for value in lista:
    if value not in no_repeat:
        no_repeat.append(value)
print(no_repeat)
