#Faça um programa com uma função que recebe uma frase. 
#Para cada palavra nesta frase, inverta a ordem das letras.
#Exiba o resultado:

frase = input("Entre com a frase que você deseja inverter:  ")

palavras = frase.split()

frase_invertida = [palavra[::-1] for palavra in palavras]

print(f"O resultado é: {' '.join(frase_invertida)}")