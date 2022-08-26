def leaiInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Digite um número inteiro válido.')
            continue
        except KeyboardInterrupt:
            print('Usuário não digitou esse número.')
            return 0
        else:
            return n

def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leaiInt('Escolha uma Opção: ')
    return opc