lista1 =[]
adms = []
clientes = []
logado = False
while True:
    print('     *****MENU*****\n 1 - Login\n 2 - Cadastrar')
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
                    
                else:
                    print('Login ou senha incorretos...')
                    continue
            print(logado , 'logado ou não')    
        elif verif == 2:
            login = input('Digite seu nome de usuario: ')
            senha = input('Digite sua senha de acesso: ')
        
while True:
    print('     *****MENU*****\n 1 - Adicionar na lista\n 2 - Adicionar numa posição especifica\n 3 - Exibir Lista\n 4 - Buscar na lista \n 5 - Remover da Lista\n 0 - Encerrar\n')
    opcao = int(input('Digite a opção desejada: '))
    if opcao == 1:
        nome = input('Digite o nome do aluno: ').lower()
        lista1.append(nome)
        print('Adicionado com Sucesso!')
    elif opcao == 2:
        nome = str(input('Digite o nome do aluno: ')).lower()
        pos = int(input('Em qual posição você deseja inserir?\n'))
        lista1.insert(pos,nome)
        print('Adicionado com Sucesso!')
    elif opcao == 3:
        print(lista1)
    elif opcao == 4:
        busca = input('Quem você deseja buscar?\n').lower()
        for i in range(len(lista1)):
            if busca == lista1[i]:
                index = i
                print(f'A pessoa está na lista na posição {index}.')
                break
    elif opcao == 5:
        remov = int(input('Digite qual a posição da lista deseja remover: '))
        lista1.pop(remov)
        print('Removido com Sucesso!')
    elif opcao == 6:
        index = int(input('Qual item da lista deseja atualizar?'))
        novo = input('Pelo o que você deseja substituir?\n')
        lista1[index] = novo
        print('Elemento atualizado com Sucesso!')               
    elif opcao == 0:
        print('Encerrado.')
        break