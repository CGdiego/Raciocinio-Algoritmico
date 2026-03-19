idade = (int(input("Qual é a sua idade? ")))
ingresso = (input("Você tem ingresso? (S/N) ")).upper()

if ingresso == "S":
    ingresso = True
elif ingresso == "N":
    ingresso = False
else:
    print("Inválido")

if idade >= 18:
    if ingresso:
        print("Bom filme! :)")
    else:
        print("Não tem ingresso. >:(")
else:
    print("Menor de idade. >:(")