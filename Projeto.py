lista1 =[]
adms = []
clientes = []
user_logado = []
logado = False
while True:
    print('     *****MENU*****\n 1 - Login\n 2 - Cadastrar\n 0 - Encerrar')
    opcao = int(input('Digite a opção desejada: '))

    if opcao == 2:
        verif = int(input('Deseja criar um login de ADM ou Cliente?(1 - ADM, 2 - Cliente)'))
        if verif == 1:
            login = input('Crie seu nome de usuario: ')
            senha = input('Crie sua senha: ')
            adms.append([login,senha,True])

        elif verif == 2:
            login = input('Crie seu nome de usuario: ')
            senha = input('Crie sua senha: ')
            clientes.append([login,senha,False])
        continue

    elif opcao == 1:
        verif = int(input('Deseja entrar como ADM ou Cliente?(1 - ADM, 2 - Cliente)'))

        if verif == 1:
            login = input('Digite seu nome de usuario: ')
            senha = input('Digite sua senha de acesso: ')
            for adm in adms:
                if login == adm[0] and senha == adm[1]:
                    logado = True
                    user_logado = [[adm[0],adm[2]]]
                    break

            if logado == False:
                print('Login ou senha incorretos...')    
            

        elif verif == 2:
            login = input('Digite seu nome de usuario: ')
            senha = input('Digite sua senha de acesso: ')
            for cliente in clientes:
                if login == cliente[0] and senha == cliente[1]:
                    logado = True
                    user_logado = [[cliente[0] ,cliente[2]]]
                    break
            if logado == False:
                print('Login ou senha incorretos...')    

        elif verif == 0:
            break
        
    if logado == True:
        print('Login efetuado com sucesso')
    
    # isso daqui é temporario
    elif logado == False:
        print('algo está errado')
    # ----------------------------

    '''-----------Requisitos Funcionais (ADM):

R1 - Login: Efetuar login com usuário e senha para acessar o menu de gestão da fazenda. Tanto ADM ou CLIENTE pode fazer login.

R2 - Gerenciar Rebanho: Cadastrar, buscar, atualizar e remover animais. O cadastro deve incluir o tipo do animal (Bovino de Leite, Caprino, Ovino, Suíno/Leitão), identificação (brinco/número) e status (ex: em lactação, para engorda, disponível para venda).

R3 - Gerenciar Produção e Derivados: Cadastrar a produção diária. O ADM deve poder registrar litros de leite ordenhados e adicionar ao estoque produtos fabricados (ex. Queijo Coalho, Queijo Manteiga), informando o peso (kg) e o valor de venda.

R4 - Tema Livre (ADM): Criar uma funcionalidade útil para o produtor rural.
    '''
    animais_cadastrados = []
    if user_logado and user_logado[0][1] == True:
        while True:
            print(f'\n\n\n\nBem-vindo, {user_logado[0][0]} \n     *****MENU*****\n 1 - Gerenciar Rebanho\n 2 - Gerenciar Produção e Derivados\n 0 - Menu de Cadastro\n')
            opcao = int(input('Digite a opção desejada: '))
            if opcao == 1:
                while True:
                    print('''     *****MENU*****
        1 - Cadastrar
        2 - Buscar
        3 - Atualizar
        4 - Remover Animais
        0 - Voltar''')
                    controle = int(input('Digite a opção desejada: '))
                    if controle == 0:
                        break
            if opcao == 2:
                while True:
                    print('''     *****MENU*****
        1 - Cadastrar Produção Diária
        2 - Registrar Litros de Leite Ordenhados
        3 - adicionar ao Estoque Produtos Fabricados
        0 - Voltar''')
                    controle = int(input('Digite a opção desejada: '))
                    if controle == 0:
                        break
                
                    
            elif opcao == 0:
                print('Retomando...')
                logado = False
                user_logado = []
                continue
    
    elif user_logado and user_logado[0][1] != True and logado == True:
    # menu do cliente
    
        print()
