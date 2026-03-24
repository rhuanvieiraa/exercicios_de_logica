def calcular_media(p1,p2):
    return (p1 + p2) / 2

def verificar_status(media):
    if media >= 6:
        return "aprovado"
    elif media >= 4 and media <= 5.9:
        return "recuperação"
    else:
        return "reprovadooo"
        
print("=" * 75)
print("---------- VAMOS CALCULAR SUA MÉDIA!! ----------")

p1 = float(input("Digite sua nota na P1: "))
p2 = float(input("Digite sua nota na P2: "))

media = calcular_media(p1,p2)
print(f"Sua media foi: {calcular_media(p1,p2)}")
print(verificar_status(media))
