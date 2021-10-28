
lista = [45, 56, 23, 67, 27, 89, 12, 76, 34, 61, 100]
lista2 = []
for h in range(len(lista)):
    minsta = lista[0]
    for i in range(len(lista)):
        if lista[i] < minsta:
            minsta = lista[i]
    lista2.append(minsta)
    lista.pop(lista.index(minsta))
print(lista2)
