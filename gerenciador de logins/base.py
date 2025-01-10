from func import *

#criando arquivo
import os
login = os.getlogin()
arq = rf"C:\Users\{str(login)}\Documents\Gerenciador_De_Logins.txt"
try:
    open(arq, "r").close()
except FileNotFoundError:
    with open(arq, "w") as doc:
        doc.write(f'\n{"URL":<15}{"EMAIL":<30}{"SENHA":>15}\n')

#pontinhos
import time
for _ in range (3):
    print('-',  end='', flush=True)
    time.sleep(1)


while True:
    menu()

    while True:
        press = input('press: ')
        print('¬'*60)

        if inteiro(press) == True and entre(press) == True: break
        else: continue

    from texto import *
    match int(press):
        case 0:
            painel(arq)
        case 1:
            add(arq)
        case 2:
            sub(arq)
        case 3:
            rem(arq)
        case 4:
            print('Ate mais')
            break