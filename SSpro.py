from lib.interface import *

class Repositorio():
    
    lista_funcionarios = list()
    lista_tenis = list()
    tenis_input = {} 

    def pesquisar_funcionario(self):
        cpf_funcionario = input('Insira CPF do funcionário: ')
        encontrou = False
        for busca in self.lista_funcionarios:
            if cpf_funcionario == busca.cpf:
                busca.print_usuario()
                encontrou = True
        if encontrou == False:
            print('Funcionário não encontrado!')
    
    def pesquisar_tenis(self):
        modelo_tenis = input('Insira o modelo do tênis: ')
        encontrou = False
        for busca in self.lista_tenis:
            if modelo_tenis.upper() == busca.modelo.upper():
                busca.print_tenis()
                encontrou = True
                print(linha())
        if encontrou == False:
            print('Modelo de tênis fora de estoque')
        
    def cadastrar_funcionario(self):
        nome = input('Informe o nome do funcionário: ')
        cpf = input('Informe o CPF do funcionário: ')
        sexo = input('Informe o sexo do funcionário(M ou F): ')
        codigo_funcionario = int(input('Informe o código do funcionário: '))
        cargo = input('Informe o cargo do funcionário: ')
        funcionario = Funcionario(nome, cpf, sexo, codigo_funcionario, cargo)
        funcionario.print_usuario(True)
        self.lista_funcionarios.append(funcionario)
    
    def cadastrar_tenis(self):
        marca = input('Informe a marca do tênis: ')
        modelo = input('Informe o modelo do tênis: ')
        codigo = int(input('Informe o código do tênis: '))
        preco = float(input('Informe o preço do tênis: '))
        numeracao = int(input('Informe a numeração do tênis: '))
        tenis = Tenis(marca, modelo, codigo, preco, numeracao)
        tenis.print_tenis(True)
        self.lista_tenis.append(tenis)
    
    def mostrar_funcionarios(self):
        print(linha())
        for i in self.lista_funcionarios:
            i.print_usuario()
            print(linha())

    def mostrar_tenis(self):
        print(linha())
        for i in self.lista_tenis:
            i.print_tenis()
            print(linha())

repositorio = Repositorio()

class Usuario():
    def __init__(self, nome, cpf, sexo):
        self.nome = nome
        self.cpf = cpf
        self.sexo = sexo

    def cria_dicionario(self):
        return {'nome':self.nome, 'cpf':self.cpf, 'sexo':self.sexo}

    def print_usuario(self):
        print(self.cria_dicionario())


class Funcionario(Usuario):
    def __init__(self, nome, cpf, sexo, codigo_funcionario, cargo):
        self.codigo_funcionario = codigo_funcionario
        self.cargo = cargo
        Usuario.__init__(self, nome, cpf, sexo)

    def cria_dicionario(self):
        return {'nome':self.nome, 'cpf':self.cpf, 'sexo':self.sexo, 'codigo':self.codigo_funcionario, 'cargo':self.cargo}

    def print_usuario(self, exibir_cabecalho=False):
        if exibir_cabecalho == True:
            cabecalho('FUNCIONÁRIO CADASTRADO')
        print(self.cria_dicionario())


class Tenis():
    def __init__(self, marca, modelo, codigo_tenis, preco, numeracao):
        self.marca = marca
        self.modelo = modelo
        self.codigo_tenis = codigo_tenis
        self.preco = preco
        self.numeracao = numeracao

    def print_tenis(self, exibir_cabecalho=False):
        if exibir_cabecalho == True:
            cabecalho('FUNCIONÁRIO CADASTRADO')
        print('MARCA:  {}'.format(self.marca))
        print('MODELO:  {}'.format(self.modelo))
        print('CÓDIGO DO TÊNIS:  {}'.format(self.codigo_tenis))
        print('PREÇO:  {:.2f}'.format(self.preco))
        print('NUMERAÇÃO DISPONÍVEL:  {}'.format(self.numeracao))


funcionario_1 = Funcionario('José Roberto', '148.479.449-03', 'M', 123, 'Atendente')
repositorio.lista_funcionarios.append(funcionario_1)

funcionario_2 = Funcionario('Júlia Fonseca', '208.933.549-01', 'F', 104, 'Gerente')
repositorio.lista_funcionarios.append(funcionario_2)

funcionario_3 = Funcionario('Roberto Carlos', '163.226.328-14', 'M', 201, 'Atendente')
repositorio.lista_funcionarios.append(funcionario_3)

funcionario_4 = Funcionario('Fabricia Silva', '188.397.123-45', 'F', 331, 'Atendente')
repositorio.lista_funcionarios.append(funcionario_4)

funcionario_5 = Funcionario('Rogério Cláudiano', '123.367.881-92', 'M', 215, 'Faxineiro')
repositorio.lista_funcionarios.append(funcionario_5)


tenis_1 = Tenis('Nike', 'Steffan Janoski', 192, 435.50, 42)
repositorio.lista_tenis.append(tenis_1)

tenis_2 = Tenis('Adidas', 'Ultraboost', 420, 600.75, 44)
repositorio.lista_tenis.append(tenis_2)

tenis_3 = Tenis('Adidas', 'NMD _X1_', 871, 998.50, 43)
repositorio.lista_tenis.append(tenis_3)

tenis_4 = Tenis('Nike', 'Air Force', 9076, 455.99, 42)
repositorio.lista_tenis.append(tenis_4)

tenis_5 = Tenis('Nike', 'Air Jordan Dunk', 9076, 798.99, 40)
repositorio.lista_tenis.append(tenis_5)


while True:
    resposta = menu(['Cadastar funcionário', 'Cadastrar tênis', 'Mostrar funcionários', 'Pesquisar funcionário', 'Mostrar tênis', 'Pesquisar tênis', 'Encerrar programa',])
    if resposta == 1:
        cabecalho('CADASTRO DE FUNCIONÁRIOS')
        repositorio.cadastrar_funcionario()
    elif resposta == 2:
        cabecalho('CADASTRO DE TÊNIS')
        repositorio.cadastrar_tenis()
    elif resposta == 3:
        cabecalho('MOSTRAR FUNCIONÁRIOS')
        repositorio.mostrar_funcionarios()
    elif resposta == 4:
        cabecalho('PESQUISAR FUNCIONARIO')
        repositorio.pesquisar_funcionario()
    elif resposta == 5:
        cabecalho('MOSTRAR TÊNIS')
        repositorio.mostrar_tenis()
    elif resposta ==6:
        cabecalho('PESQUISAR TÊNIS')
        repositorio.pesquisar_tenis()
    elif resposta == 7:
        cabecalho('SAINDO DO SISTEMA')
        break
    else:
        print('Digite uma opção válida!')