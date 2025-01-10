def menu():
    print('')
    print('¬'*60)
    print('GERENCIADOR DE LOGINS'.center(60))
    print('¬'*60)
    print('''[0] -> Mostrar bloco de Login
[1] -> Criar Registro de Login
[2] -> Substituir Login
[3] -> Apagar Login
[4] -> Sair do programa''', end='                             ')
    
def inteiro(valor):
    try:
        int(valor)
    except ValueError:
        print('Digite um numero...')
        return False
    else:
        return True
    
def entre(valor):
    if int(valor) <= 4 and int(valor) >= 0: return True
    else: return False