def menor_elemento(inteiros):
    menor = inteiros[0]

    for i in range (len(inteiros)):
        if inteiros[i] < menor:
            menor = inteiros[i]
    return menor



inteiros = [15, 22, 5, 31, 67]
print(menor_elemento(inteiros))