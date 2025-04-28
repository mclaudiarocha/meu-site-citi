#Escreva um programa que receba uma lista de números do 
#usuário e conte quantas vezes um número específico 
#aparece na lista. Solicite ao usuário um número e exiba a contagem.

num = list(map(int, input("Enttre com números separados por espaço: ").split()))

ask = int(input("Qual número você deseja saber quantas vezes aparece: "))

quantidade = num.count(ask)

print(f"O número {ask} aparece {quantidade} vezes")