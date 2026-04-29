
resp = "s"
aluno = 0

while resp == "s":
    aluno += 1
    print(f"Aluno {aluno}")
    nota1 = float(input("Nota da prova 1: "))
    nota2 = float(input("Nota da prova 2: "))
    nota3 = float(input("Nota da prova 3: "))
    media = (nota1 + nota2 + nota3) / 3

    print(f"Média: {media:.2f}")
    if media < 0:
        print("Revise o preenchimento das notas!!")
    elif media >= 7:
        print("Aprovado!!")
    elif media >= 5:
        print("Recuperação.")
    else:
        print("Reprovado!!")


    resp = input("Deseja continuar? (S/N): ").lower()
print("Consulta de Notas Encerrada!!")



