nomes = [""] * 5
nomesVogal = 0

for i in range(len(nomes)):
    nomes[i] = input(f"Insira o {i+1}º nome: ").lower()

    if nomes[i][0] in ["a", "e", "i", "o", "u"]:
        nomesVogal += 1

print(f"{nomesVogal} nome(s) começa(m) com vogal.")