#Escreva um programa que crie um dicionário com nomes de frutas 
#como chaves e seus respectivos preços como valores
#Solicite ao usuário o nome de uma fruta e exiba o preço correspondente.

dados = {'maça': 1.50,
         'banana': 2.75,
         'uva': 1.90,
         'pera': 1.25,
         'laranja':0.65,
         'limão': 1.25,
         'goiaba': 2.15,
         'abacaxi': 3.15,
         'jaca': 5.80}

fruta = input("Entre com a fruta desejada: ").lower()


if fruta in dados:
    print(f"O valor da fruta {fruta} é R${dados[fruta]}")
else:
    print("Fruta não disponível")