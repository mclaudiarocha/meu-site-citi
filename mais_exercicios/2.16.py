#Escreva um programa que solicite ao usuário um número e 
#exiba a tabuada desse número de 1 a 10.

num = int(input("Entre com o número que você deseja saber a tabuada:  "))

for i in range(1,11):
    print(f"{i}x{num}={i*num}")
    
