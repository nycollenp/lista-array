def somar_valores(inteiros):
    soma = 0

    for i in range (len(inteiros)):
        soma += inteiros[i]
    return soma


inteiros = [1, 2, 3, 4, 5]
print(somar_valores(inteiros))