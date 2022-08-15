#escreva um programa capaz de receber 5 notas calcular a media, se a media for <= 5 escrever reprovado. Se a media for maior que 5, menor que 7 escrever recuperação. Se a media for maior que 7, escrever aprovado.
nota1 = float (input("Insira uma nota: "))
nota2 = float (input("Insira uma nota: "))
nota3 = float (input("Insira uma nota: "))
nota4 = float (input("Insira uma nota: "))
nota5 = float (input("Insira uma nota: "))

media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

print(f'Sua media é {media}')

if media <= 5.0:
    print("reprovado")
if media > 5.0 and media <= 7.0:
    print("recuperação")
if media > 7.0:
    print("aprovado")
