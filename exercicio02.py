def maior_elemento(inteiros):
    maior = inteiros[0]

    for i in range (len(inteiros)):
        if inteiros[i] > maior:
            maior = inteiros[i]
    return maior

inteiros = [10, 2, 47, 55, 12]
print(maior_elemento(inteiros))
