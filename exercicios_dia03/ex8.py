# %%
#Faça um programa que receba 4 alturas, armazene em uma lista e 
#depois mostre a soma dessas alturas.
altura = [int(input(f"Entre com a {1+i} altura: ")) for i in range(4)]

print(f'A soma das alturas é {sum(altura)}')

    
