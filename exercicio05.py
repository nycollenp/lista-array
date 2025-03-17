def verificar_palindromo(palavra1, palavra2):
    if len(palavra1) != len(palavra2):
        return False
    for i in range (len(palavra1)):
        if palavra1[i] != palavra2[len(palavra2) -1 -i]:
            return False
    return True


palavra1 = "amor"
palavra2 = "terra"
resultado = verificar_palindromo(palavra1, palavra2)

if resultado:
    resposta = "a palavra", palavra1, "e", palavra2, "sao palindromos"
else:
    resposta = "a palavra", palavra1, "e", palavra2, "nao sao palindromos"


print(resposta)