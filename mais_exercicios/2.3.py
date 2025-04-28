#Escreva um programa que solicite ao usuário um nome e uma idade, 
#e crie um dicionário com essas informações. Em seguida, exiba o dicionário.

nome = input("Entre com o seu nome: ")
idade = int(input("Entre com sua idade: "))

dicionario = {'nome': nome,
              'idade': idade}

print(dicionario)
