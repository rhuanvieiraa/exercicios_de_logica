import random

print("========== ALUGUEL DE CARRO ==========")
nome = input("Nome e Sobrenome: ")
carro = input("Modelo do Veículo: ")
dias = int(input("Quantidade de dias: "))
contrato = random.randint(500,1000)

def valor_aluguel(dias):
    if dias < 0:
        return "Digite um número válido!!"
    elif dias <= 3:
        return dias * 150
    elif dias <= 7:
        return dias * 120
    else:
        return dias * 100
        
print("========== ORÇAMENTO ==========")
print(f"Nome:", nome)
print(f"Número do contrato:", contrato)
print(f"Modelo do veículo:", carro)
print(f"Total:R$", valor_aluguel(dias))
