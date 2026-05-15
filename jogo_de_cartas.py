import random

monte_espera = []
gabarito = ["Nome", "Velocidade", "Tanque", "Ano"]
pontos_j1 = 0
pontos_j2 = 0

baralho = [
["Toyota Yaris Cross", 175, 36, 2024],
["Ferrari F40", 324, 120, 1987],
["Lamborghini Aventador", 350, 90, 2011],
["Bugatti Chiron", 420, 100, 2016],
["Porsche 911", 310, 64, 2023],
["McLaren P1", 350, 72, 2013],
["Audi R8", 330, 83, 2021],
["BYD Song Plus", 170, 60, 2023] 
]

while True:
    print("========== SUPER TRUNFO ==========")
    print("1.Single Player.")
    print("2.Multiplayer.")
    print("3.Ranking de Pontuação.")
    print("4.Sair")
    print()
    opcao = input("Escolha um opção: ")

    if opcao == "1" or opcao == "2":
        random.shuffle(baralho)
        meio = len(baralho) // 2

        mao_j1 = baralho[:meio]
        mao_j2 = baralho[meio:]
        turno = 1
        monte_espera =[]

        print("Iniciando o jogo...")
        print("="*40)
        print()

        while len(mao_j1) > 0 and len(mao_j2) > 0:
            if turno == 1:
                print("===== VEZ DO JOGADOR 1 =====")
                carta_topo = mao_j1[0]
                print(f"{gabarito[0]}: {carta_topo[0]}") # Nome
                print(f"1. {gabarito[1]}: {carta_topo[1]} km/h")
                print(f"2. {gabarito[2]}: {carta_topo[2]} litros")
                print(f"3. {gabarito[3]}: {carta_topo[3]}")
                print()

                escolha = int(input("Escolha um atributo da carta (1-3): "))
            else:
                if opcao == "1":
                    print("===== VEZ DO COMPUTADOR =====")
                    escolha = random.randint(1, 3)
                    print(f"O computador escolheu o atributo {escolha}")
                else:
                    print("===== VEZ DO JOGADOR 2 =====")
                    carta_topo = mao_j2[0]
                    print(f"Sua carta: {carta_topo[0]}") # Nome
                    print(f"1. Velocidade: {carta_topo[1]} km/h")
                    print(f"2. Tanque: {carta_topo[2]} litros")
                    print(f"3. Ano: {carta_topo[3]}")
                    print()
                    escolha = int(input("Escolha um atributo da carta (1-3): "))

            valor_j1 = mao_j1[0][escolha]
            valor_j2 = mao_j2[0][escolha]

            print()

            if valor_j1 > valor_j2:
                print("Jogador 1 venceu a Rodada!!!")
                turno = 1
                carta_j1 = mao_j1.pop(0)
                carta_j2 = mao_j2.pop(0)

                mao_j1.append(carta_j1)
                mao_j1.append(carta_j2)
                while len(monte_espera) > 0:
                    mao_j1.append(monte_espera.pop(0))

            elif valor_j2 > valor_j1:
                turno = 2
                print("Jogador 2 venceu a Rodada!!!")
                carta_j1 = mao_j1.pop(0)
                carta_j2 = mao_j2.pop(0)

                mao_j2.append(carta_j1)
                mao_j2.append(carta_j2)
                while len(monte_espera) > 0:
                    mao_j2.append(monte_espera.pop(0))

            elif valor_j1 == valor_j2:
                print("As cartas foram para o monte de espera.")
                monte_espera.append(mao_j1.pop(0))
                monte_espera.append(mao_j2.pop(0))
            print("=" * 40)

        if len(mao_j1) > 0:
            print("FIM DE JOGO!! JOGADOR 1 É O GRANDE CAMPEÃO!!!")
            pontos_j1 += 5
        else:
            print("FIM DE JOGO!! O JOGADOR 2 É O GRANDE CAMPEÃO!!!")
            print("="*40)
            pontos_j2 += 5
            print()
    
    elif opcao == "3":
        print()
        print("1 vitória = 5 pontos ")
        print()
        print(f"Jogador 1: {pontos_j1}")
        print(f"Jogador 2: {pontos_j2}")
        

    elif opcao == "4":
        print("Até logo.")
        break
        print()
    else:
        print("Opção inválida.")
        print()