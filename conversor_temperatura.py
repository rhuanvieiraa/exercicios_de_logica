def verifica_opcao():
    while True:
        print("Digite: \nF - Fahrenheit para celsius \nC- Celsius para Fahrenheit")
        print()
        escolha = input("Qual a sua escolha: F ou C?: ").lower()
        print()

        if escolha == "f" or escolha == "c":
            return escolha
    print("Digite uma opção válida!!")
    print()


def verifica_intervalo():
    while True:
        inicio = int(input("Digite o início do intervalo: "))
        fim = int(input("Digite o fim do intervalo: "))

        if inicio > fim:
            return "Valores incorretos, o valor inicial deve ser menor que o final!!\nDigite novamente: "
        else:
            return inicio, fim


conversao = verifica_opcao()
inicio, fim = verifica_intervalo()

if conversao == "c":
    for i in range(inicio, fim + 1):
        cel_fah = i *1.8 + 32
        print(f"{i:.2f}°C = {cel_fah:.2f}°F")

if conversao == "f":
    for i in range(inicio, fim + 1):
        fah_cel = (i - 32) / 1.8
        print(f"{i:.2f}°F = {fah_cel:.2f}°C")
