usuario = input("Insira o usuário: ")
senha = input("Insira a senha: ")

if usuario == "convidado" and senha == "":
    print("Acesso restrito.")

if usuario == "admin":
    if senha == str(1234):
        print("Bem-vindo admin!")
    else:
        print("Acesso bloqueado.")
else:
    if not (usuario == "convidado" and senha == ""):
        print("Acesso bloqueado.")