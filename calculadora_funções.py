def soma(n1,n2):
    return n1 + n2
        
def subtracao(n1,n2):
    return n1 - n2

def multiplicacao(n1,n2):
    return n1 * n2
        
def divisao(n1,n2):
    if n2 == 0:
        print("não é possivel fazer essa divisão.")
    return n1 / n2
    
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

print("Qual a operação desejada? \1-soma \2-subtração \3-multiplicação \4-divisão")
operacao = input("Operação desejada: ")

if operacao == "1":
    resultado = soma(n1,n2)
    print(f"Esse é o resultado: {resultado}")
    
elif operacao == "2":
    print(f"Esse é o seu resultado: {subtracao(n1,n2)}")
    
elif operacao == "3":
    print(f"Esse é o seu resultado: {multiplicacao(n1,n2)}")
    
elif operacao == "4":
    print(f"Esse é o seu resultado: {divisao(n1,n2)}")

else:
    print("Opção Inválida!!!")
