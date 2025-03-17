def dna_rna(dna):
    rna = ""
    for i in range (len(dna)):
        if dna[i] == "T":
            rna += "U"
        else:
            rna += dna[i]
    return rna

dna = ["A", "C", "G", "U"]
print(dna_rna(dna))