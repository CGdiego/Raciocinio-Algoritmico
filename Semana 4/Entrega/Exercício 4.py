usuario = input("Insira o usuário: ")
senha = input("Insira a senha: ")

if usuario == "admin":
    if senha == 1234:
        print("Bem-vindo admin!")
    else:
        print("Acesso bloqueado.")
else:
    print("Acesso bloqueado.")