lista1 =[]
adms = []
clientes = []
user_logado = []
animais_cadastrados = []
ListaTipos = []
ListaStatus = []
logado = False
while True:
    print('     *****MENU*****\n 1 - Cadastrar\n 2 - Login\n 0 - Encerrar')
    opcao = int(input('Digite a opção desejada: '))

    if opcao == 1:
        verif = int(input('Deseja criar um conta de ADM ou Cliente?(1 - ADM, 2 - Cliente)'))
        if verif == 1:
            login = input('Crie seu nome de usuario: ')
            senha = input('Crie sua senha: ')
            adms.append([login,senha,True])
        
        elif verif == 2:
            login = input('Crie seu nome de usuario: ')
            senha = input('Crie sua senha: ')
            clientes.append([login,senha,False])
        continue

    elif opcao == 2:
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
                continue

        elif verif == 2:
            login = input('Digite seu nome de usuario: ')
            senha = input('Digite sua senha de acesso: ')
            for cliente in clientes:
                if login == cliente[0] and senha == cliente[1]:
                    logado = True
                    user_logado = [cliente[0] ,cliente[2]]
                    break
            if logado == False:
                print('Login ou senha incorretos...')    
                continue
    elif verif == 0:
        break
        
    if logado == True:
        print('Login efetuado com sucesso')
    
    '''-----------Requisitos Funcionais (ADM):

R1 - Login: Efetuar login com usuário e senha para acessar o menu de gestão da fazenda. Tanto ADM ou CLIENTE pode fazer login.

R2 - Gerenciar Rebanho: Cadastrar, buscar, atualizar e remover animais. O cadastro deve incluir o tipo do animal (Bovino de Leite, Caprino, Ovino, Suíno/Leitão), identificação (brinco/número) e status (ex: em lactação, para engorda, disponível para venda).

R3 - Gerenciar Produção e Derivados: Cadastrar a produção diária. O ADM deve poder registrar litros de leite ordenhados e adicionar ao estoque produtos fabricados (ex. Queijo Coalho, Queijo Manteiga), informando o peso (kg) e o valor de venda.

R4 - Tema Livre (ADM): Criar uma funcionalidade útil para o produtor rural.
    '''
    if user_logado and user_logado[0][1] == True:
        while True:
            print(f'{"\n"*4}Bem-vindo, {user_logado[0][0]} \n     *****MENU*****\n 1 - Gerenciar Rebanho\n 2 - Gerenciar Produção e Derivados\n 0 - Menu de Cadastro\n')
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
                        print('Voltando ao meu')
                        break
                    
                    elif controle == 1:
                        Tipo = str(input("Qual o tipo de animal?\n")).upper()                        
                        indetificacao = int(input('Qual o número de indentificação?\n'))
                        status = input('Qual o status do animal?\n').upper()                     
                        animais_cadastrados.append([Tipo,indetificacao,status])
                    
                    elif controle == 2:
                        while True:
                            print(f'{"\n"*4}O que você deseja buscar, {user_logado[0][0]}? \n     *****MENU*****\n 1 - Busca por ID do animal\n 2 - Buscar por Tipo dos animais\n 3 - Buscar por status\n 0 - Sair da busca\n')
                            opcao = int(input('Digite a opção desejada: '))
                            
                            if opcao == 1:
                                busca = input('Digite o número do animal: ')
                                for i in range(len(animais_cadastrados)):
                                    if busca == animais_cadastrados[i][1]:
                                        index = i
                                        break
                                print(f'O seu animal {animais_cadastrados[index]}')
                            
                            elif opcao == 2:
                                busca = str(input('Digite o Tipo do animal: ')).upper()
                                for i in range(len(animais_cadastrados)):                              
                                    if busca == animais_cadastrados[i][0]:
                                        ListaTipos.append = animais_cadastrados[i]
                                        
                                print(f'Os seus {busca}s são:\n{ListaTipos}')
                                print(f'Você tem {len(ListaTipos)} {busca}s')
                            
                            elif opcao == 3:                                
                                busca = str(input('Digite o Status do animal que deseja buscar: ')).upper()
                                for i in range(len(animais_cadastrados)):                              
                                    if busca == animais_cadastrados[i][2]:
                                        ListaStatus.append = animais_cadastrados[i]
                                print(f'Você tem {len(ListaStatus)} animais em: {busca}')
                                print(f'Os seus animais em {busca}s são:\n{ListaStatus}')
                            
                            elif opcao == 0:
                                print('Encerrando busca.')
                                break
                            else:
                                print('Opçao inválida')
                                continue
                    
                    elif controle == 3:
                        busca = int(input('Qual o número de identificação do animal que deseja atualizar?\n'))
                        for i in range(len(animais_cadastrados)):
                                    if busca == animais_cadastrados[i][1]:
                                        index = i
                                        break
                        a = input(f'O status atual do animal é: {animais_cadastrados[index][2]}. Deseja Atulizar?(S - Sim N - Não)').upper()
                        if a == 'S':
                            b = input('Digite o status atual do animal: ').upper()
                            animais_cadastrados[index][2] = b
                        elif a == 'N':
                            print('Retornando ao menu')
                            break
                    
                    elif controle == 4:
                        busca = int(input('Qual o número de identificação do animal que deseja remover?\n'))
                        for i in range(len(animais_cadastrados)):
                                    if busca == animais_cadastrados[i][1]:
                                        index = i
                                        break
                        a = input(f'Os dados do animal é: {animais_cadastrados[index]}. Deseja Remover?(S - Sim N - Não)').upper()
                        if a == 'S':
                            animais_cadastrados.pop[index]
                        elif a == 'N':
                            print('Retornando ao menu')
                            break

                                #Lembrar de zerar a ListaA ao voltar pro menu
            elif opcao == 2:
                while True:
                    print('''     *****MENU*****
1 - Registrar Litros de Leite Ordenhados
2 - adicionar ao Estoque Produtos Fabricados            login = input('Crie seu nome de usuario: ')

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
