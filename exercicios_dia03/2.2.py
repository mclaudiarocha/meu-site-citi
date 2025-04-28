#Faça um programa que receba um número. Verifique se o número informado é par ou ímpar. Exiba o resultado da seguinte maneira:

#	O número x é impar
#ou
#	O número x é par

num = int(input("Entre com o número desejado: "))
if num % 2 == 0:
    print(f"O número {num} é par")
else:
    print(f"O número {num} é ímpar")