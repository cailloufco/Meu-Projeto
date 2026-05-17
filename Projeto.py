lista1 = []
adms = [["higor", "123", True]]
clientes = [["caio", "123", False]]
user_logado = []
animais_cadastrados = []
produtos_cadastrados = [["OVO", 10, "VENDA"]]
ListaTipos = []
ListaStatus = []
index = 0
logado = False
agendamentos = []
estoque = []
while True:
    print("     *****MENU*****\n 1 - Cadastrar\n 2 - Login\n 0 - Encerrar")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        verif = int(
            input("Deseja criar um conta de ADM ou Cliente?(1 - ADM, 2 - Cliente)")
        )
        if verif == 1:
            login = input("Crie seu nome de usuario: ")
            senha = input("Crie sua senha: ")
            adms.append([login, senha, True])

        elif verif == 2:
            login = input("Crie seu nome de usuario: ")
            senha = input("Crie sua senha: ")
            clientes.append([login, senha, False])
        continue

    elif opcao == 2:
        verif = int(input("Deseja entrar como ADM ou Cliente?(1 - ADM, 2 - Cliente)"))

        if verif == 1:
            login = input("Digite seu nome de usuario: ")
            senha = input("Digite sua senha de acesso: ")
            for adm in adms:
                if login == adm[0] and senha == adm[1]:
                    logado = True
                    user_logado = [[adm[0], adm[2]]]
                    break

            if logado == False:
                print("Login ou senha incorretos...")
                continue

        elif verif == 2:
            login = input("Digite seu nome de usuario: ")
            senha = input("Digite sua senha de acesso: ")
            for cliente in clientes:
                if login == cliente[0] and senha == cliente[1]:
                    logado = True
                    user_logado = [[cliente[0], cliente[2]]]
                    break
            if logado == False:
                print("Login ou senha incorretos...")
                continue
    elif opcao == 0:
        break

    if logado == True:
        print("Login efetuado com sucesso")
    """-----------Requisitos Funcionais (ADM):

R1 - Login: Efetuar login com usuário e senha para acessar o menu de gestão da fazenda. Tanto ADM ou CLIENTE pode fazer login.

R2 - Gerenciar Rebanho: Cadastrar, buscar, atualizar e remover animais. O cadastro deve incluir o tipo do animal (Bovino de Leite, Caprino, Ovino, Suíno/Leitão), identificação (brinco/número) e status (ex: em lactação, para engorda, disponível para venda).

R3 - Gerenciar Produção e Derivados: Cadastrar a produção diária. O ADM deve poder registrar litros de leite ordenhados e adicionar ao estoque produtos fabricados (ex. Queijo Coalho, Queijo Manteiga), informando o peso (kg) e o valor de venda.

R4 - Tema Livre (ADM): Criar uma funcionalidade útil para o produtor rural.
    """
    if user_logado and user_logado[0][1] == True:
        while True:
            print(
                f'{"\n"*4}Bem-vindo, {user_logado[0][0]} \n     *****MENU*****\n 1 - Gerenciar Rebanho\n 2 - Gerenciar Produção e Derivados\n 0 - Menu de Cadastro\n'
            )
            opcao = int(input("Digite a opção desejada: "))

            if opcao == 1:
                while True:
                    print("""     *****MENU*****
1 - Cadastrar
2 - Buscar
3 - Atualizar
4 - Remover Animais
0 - Voltar""")
                    controle = int(input("Digite a opção desejada: "))
                    if controle == 0:
                        print("Voltando ao menu")
                        break

                    elif controle == 1:
                        Tipo = str(input("Qual o tipo de animal?\n")).upper()
                        indetificacao = int(input("Qual o número de indentificação?\n"))
                        status = input("Qual o status do animal?\n").upper()
                        animais_cadastrados.append([Tipo, indetificacao, status])

                        venda = input(
                            "Deseja colocar esse animal à venda? (S - Sim / N - Não) "
                        ).upper()
                        if venda == "S":
                            preco = float(input("Qual o preço do animal? R$ "))
                            estoque.append(["ANIMAL", indetificacao, Tipo, preco])

                    elif controle == 2:
                        while True:
                            print(
                                f'{"\n"*4}O que você deseja buscar, {user_logado[0][0]}? \n     *****MENU*****\n 1 - Busca por ID do animal\n 2 - Buscar por Tipo dos animais\n 3 - Buscar por status\n 0 - Sair da busca\n'
                            )
                            opcao = int(input("Digite a opção desejada: "))

                            if opcao == 1:
                                busca = input("Digite o número do animal: ")
                                for i in range(len(animais_cadastrados)):
                                    if busca == animais_cadastrados[i][1]:
                                        index = i
                                        break
                                print(f"O seu animal {animais_cadastrados[index]}")

                            elif opcao == 2:
                                busca = str(input("Digite o Tipo do animal: ")).upper()
                                for i in range(len(animais_cadastrados)):
                                    if busca == animais_cadastrados[i][0]:
                                        ListaTipos.append(animais_cadastrados[i])

                                print(f"Os seus {busca}s são:\n{ListaTipos}")
                                print(f"Você tem {len(ListaTipos)} {busca}s")
                                ListaTipos.clear()

                            elif opcao == 3:
                                busca = str(
                                    input(
                                        "Digite o Status do animal que deseja buscar: "
                                    )
                                ).upper()
                                for i in range(len(animais_cadastrados)):
                                    if busca == animais_cadastrados[i][2]:
                                        ListaStatus.append(animais_cadastrados[i])
                                print(
                                    f"Você tem {len(ListaStatus)} animais em: {busca}"
                                )
                                print(
                                    f"Os seus animais em {busca}s são:\n{ListaStatus}"
                                )
                                ListaStatus.clear()
                            elif opcao == 0:
                                print("Encerrando busca.")
                                break
                            else:
                                print("Opçao inválida")
                                continue

                    elif controle == 3:
                        busca = int(
                            input(
                                "Qual o número de identificação do animal que deseja atualizar?\n"
                            )
                        )
                        for i in range(len(animais_cadastrados)):
                            if busca == animais_cadastrados[i][1]:
                                index = i
                                break
                        a = input(
                            f"O status atual do animal é: {animais_cadastrados[index][2]}. Deseja Atulizar?(S - Sim N - Não)"
                        ).upper()
                        if a == "S":
                            b = input("Digite o status atual do animal: ").upper()
                            animais_cadastrados[index][2] = b
                        elif a == "N":
                            print("Retornando ao menu")
                            break

                    elif controle == 4:
                        busca = int(
                            input(
                                "Qual o número de identificação do animal que deseja remover?\n"
                            )
                        )
                        for i in range(len(animais_cadastrados)):
                            if busca == animais_cadastrados[i][1]:
                                index = i
                                break
                        a = input(
                            f"Os dados do animal é: {animais_cadastrados[index]}. Deseja Remover?(S - Sim N - Não)"
                        ).upper()
                        if a == "S":
                            animais_cadastrados.pop(index)
                            for i in range(len(estoque)):
                                if estoque[i][1] == busca:
                                    estoque.pop(i)
                                    break
                        elif a == "N":
                            print("Retornando ao menu")
                            break
                    elif controle == 0:
                        break
                    else:
                        print("Opção inválida!!!")
                        continue

            elif opcao == 2:
                while True:
                    print("""     *****MENU*****
1 - Cadastrar
2 - Buscar
3 - Atualizar Itens
4 - Remover Itens
0 - Voltar""")
                    controle = int(input("Digite a opção desejada: "))
                    if controle == 0:
                        print("Voltando ao menu")
                        break

                    elif controle == 1:
                        Tipo = str(input("Qual o tipo de Produto?\n")).upper()
                        Quantidade = int(
                            input("Qual a quantidade do Produto no estoque?\n")
                        )
                        status = input("Qual o status do produto?\n").upper()
                        produtos_cadastrados.append([Tipo, Quantidade, status])

                        venda = input(
                            "Deseja colocar esse produto à venda no estoque? (S - Sim / N - Não) "
                        ).upper()
                        if venda == "S":
                            preco = float(input("Qual o preço do produto? R$ "))
                            estoque.append(["PRODUTO", Tipo, Quantidade, preco])

                    elif controle == 2:
                        while True:
                            print(
                                f'{"\n"*4}O que você deseja buscar, {user_logado[0][0]}? \n     *****MENU*****\n 1 - Busca por Nome do Produto\n 2 - Buscar por status\n 0 - Sair da busca\n'
                            )
                            opcao = int(input("Digite a opção desejada: "))

                            if opcao == 1:
                                busca = input("Digite o nome do Produto: ")
                                for i in range(len(produtos_cadastrados)):
                                    if busca == produtos_cadastrados[i][0]:
                                        index = i
                                        break
                                print(
                                    f"O situação do seu produto: {produtos_cadastrados[index]}"
                                )

                            elif opcao == 2:
                                busca = str(
                                    input(
                                        "Digite o Status dos produtos que deseja buscar: "
                                    )
                                ).upper()
                                for i in range(len(produtos_cadastrados)):
                                    if busca == produtos_cadastrados[i][2]:
                                        ListaStatus.append([produtos_cadastrados[i]])
                                print(
                                    f"Você tem {len(ListaStatus)} produtos em: {busca}"
                                )
                                print(
                                    f"Os seus produtos em {busca}s são:\n{ListaStatus}"
                                )
                                ListaStatus.clear()
                            elif opcao == 0:
                                print("Encerrando busca.")
                                break
                            else:
                                print("Opçao inválida")
                                continue

                    elif controle == 3:
                        busca = input(
                            "Qual o nome do produto que deseja atualizar?\n"
                        ).upper()
                        for i in range(len(produtos_cadastrados)):
                            if busca == produtos_cadastrados[i][0]:
                                index = i
                                break
                        a = input(
                            f"O status atual do produto é: {produtos_cadastrados[index][2]}. Deseja Atulizar?(S - Sim N - Não)"
                        ).upper()
                        if a == "S":
                            b = input("Digite o novo status do produto: ").upper()
                            produtos_cadastrados[index][2] = b
                        elif a == "N":
                            print("Retornando ao menu")
                            break

                    elif controle == 4:
                        busca = input(
                            "Qual o nome do produto que deseja remover?\n"
                        ).upper()
                        for i in range(len(produtos_cadastrados)):
                            if busca == produtos_cadastrados[i][0]:
                                index = i
                                break
                        a = input(
                            f"Os dados do produto são: {produtos_cadastrados[index]}. Deseja Remover?(S - Sim N - Não)"
                        ).upper()
                        if a == "S":
                            produtos_cadastrados.pop(index)

                            for i in range(len(estoque)):
                                if estoque[i][1] == busca:
                                    estoque.pop(i)
                                    break
                        elif a == "N":
                            print("Retornando ao menu")
                            break
                    elif controle == 0:
                        break
                    else:
                        print("Opção inválida!!!")
                        continue

            elif opcao == 0:
                print("Retomando...")
                logado = False
                user_logado = []
                break

        """
        R5 - Efetuar Compra: O cliente logado pode visualizar o estoque e comprar produtos (ex: 10kg de Queijo Coalho ou 5 Leitões). A compra deve diminuir a quantidade disponível nas listas de estoque do administrador. Usuário ADM não pode fazer compras.

        R6 - Agendar Retirada/Transporte: O cliente deve agendar uma data e horário para o caminhão buscar o leite, os queijos ou os animais comprados na fazenda.
        """
    elif user_logado and user_logado[0][1] != True and logado == True:
        while True:
            print(
                f'{"\n"*4}Bem-vindo, {user_logado[0][0]} \n     *****MENU CLIENTE*****\n 1 - Comprar \n 2 - Visualizar Estoque\n 3 - Agendar Retirada/Transporte\n 4 - Ver Meus Agendamentos\n 0 - Sair\n'
            )
            opcao_cliente = int(input("Digite a opção desejada: "))

            if opcao_cliente == 1:
                if len(estoque) == 0:
                    print("Nenhum item disponível no momento.")
                    continue

                posicao_escolhida = int(
                    input("\nDigite o número do item que deseja comprar: ")
                )

                if posicao_escolhida < 0 or posicao_escolhida >= len(estoque):
                    print("Item inválido.")
                    continue

                confirmacao_compra = input(
                    f"Confirmar compra de {estoque[posicao_escolhida][2]}? (S - Sim / N - Não) "
                ).upper()

                if confirmacao_compra == "S":
                    print(
                        f"Compra realizada com sucesso! Você comprou {estoque[posicao_escolhida][2]}."
                    )
                    estoque.pop(posicao_escolhida)
                else:
                    print("Compra cancelada.")

            elif opcao_cliente == 2:
                print("\n===== ITENS DISPONÍVEIS =====")
                if len(estoque) == 0:
                    print("Nenhum item disponível no momento.")
                    continue
                for posicao_item in range(len(estoque)):
                    print(
                        f"[{posicao_item}] {estoque[posicao_item][0]} | {estoque[posicao_item][2]} | Preço: R$ {estoque[posicao_item][3]}"
                    )

            elif opcao_cliente == 3:

                print("\n===== AGENDAR RETIRADA/TRANSPORTE =====")

                item_para_retirar = input(
                    "O que deseja retirar? (ex: 10kg Queijo Coalho, 5 Leitões, Leite): "
                )
                data_retirada = input("Informe a data para retirada (ex: 25/06/2025): ")
                horario_retirada = input(
                    "Informe o horário para retirada (ex: 14:00): "
                )

                confirmacao_agendamento = input(
                    f"\nConfirmar agendamento?\n  Item: {item_para_retirar}\n  Data: {data_retirada}\n  Horário: {horario_retirada}\n(S - Sim / N - Não) "
                ).upper()

                if confirmacao_agendamento == "S":
                    agendamentos.append(
                        [
                            user_logado[0][0],
                            item_para_retirar,
                            data_retirada,
                            horario_retirada,
                        ]
                    )
                    print(
                        "Agendamento realizado com sucesso! O caminhão estará na fazenda na data e horário informados."
                    )
                else:
                    print("Agendamento cancelado.")

            elif opcao_cliente == 4:
                print("\n===== MEUS AGENDAMENTOS =====")
                agendamento_encontrado = False
                for agendamento_atual in agendamentos:
                    if agendamento_atual[0] == user_logado[0][0]:
                        print(
                            f"Item: {agendamento_atual[1]} | Data: {agendamento_atual[2]} | Horário: {agendamento_atual[3]}"
                        )
                        agendamento_encontrado = True
                if not agendamento_encontrado:
                    print("Você não possui agendamentos.")

            elif opcao_cliente == 0:
                print("Saindo...")
                logado = False
                user_logado = []
                break
            else:
                print("Opção inválida!")
                continue
