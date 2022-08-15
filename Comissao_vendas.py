#Porcentagem de comissão de acordo com a quantia de vendas!

lista = []
item = 0
def comissao():
    for i in range(10):
        item = int(input("\n   %dº vendedor, insira a quantia de produtos vendidos: " % (i+1)))
        if item < 19:
            print("Sua comissão hj é de 10% das vendas")
        if item >= 20 and item <= 45:
            print ('Sua comissão hj é de 15% das vendas')
        if item > 46:
            print ("Sua comissão hj é de 20% das vendas")
    refazer = str(input("Gostaria de calcular novamente? s ou n? "))
    if refazer == "s":
        comissao()
    else:
        print("Volte sempre!")
comissao()