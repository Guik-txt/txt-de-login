def painel(arq):
    with open(arq, "r") as doc:
        print(doc.read())


def add(arq):
    with open(arq, "a") as doc:
        doc.write(f'{input("Site: ").title():<15}{input("Email: "):<15}{input("Senha: "):>15}\n')


def rem(arq):
    with open(arq, "r") as doc:
        original = doc.readlines()
        modificado = original
        x = input('Site: ').title()
        for c in original:
            if x in c:
                modificado.remove(c)

    with open(arq, "w") as novo:
        novo.writelines(modificado)

def sub(arq):
    rem(arq)
    add(arq)
