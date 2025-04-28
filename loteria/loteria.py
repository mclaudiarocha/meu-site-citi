numero_sorte = 7

for i in range(3):

    while True:
        try:
            numero = int(input("Entre com um número entre 1 e 15: "))
            break

        except ValueError:
            print("Não pode ser por extenso!!!")

    if numero == numero_sorte:
        print("Parabéns! Você acertou")
        break

    elif numero > numero_sorte:
        print("Você errou, tente com um número menor.")
    else:
        print("Você errou, tente com um número maior.")
        