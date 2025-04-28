#Escreva um programa que solicite ao usuário uma 
#palavra e verifique se a palavra é um palíndromo 
#(ou seja, é a mesma palavra quando lida de trás para frente).

palavra = input("Entre com a palavra que você deseja saber se é palíndromo: ").lower()

palavra = palavra.replace(" ","")

if palavra == palavra[::-1]:
    print("Essa palavra é palíndromo!")
else: 
    print("Essa palavra não é palíndromo!")