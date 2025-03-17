def DNA_teste():
    string = input("digite uma letra: ")

    string = string.lower()

    for i in range (len(string)):
        if string[i] not in "acgt":
            return False
    return True

print(DNA_teste())