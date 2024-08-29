#Sistema de Escola
    #Medias

nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
nota_3 = float(input("Digite a terceira nota: "))

media = (nota_1 + nota_2 + nota_3) / 3

print(f"Sua media no semestre: {media}")

if media >= 10:
    print("Aprovado com distição!")

elif media >= 7:
    print("Aprovado!")

else:
    print("reprovado!")
