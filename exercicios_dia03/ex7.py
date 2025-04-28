#Faça um programa que conte quantas vezes a 
# letra “a” aparece em uma palavra

palavra = input("Qual palavra você deseja saber a quantidade de letras 'a' contida?")

qntd = 0
for i in palavra.lower():
    if i == "a":
        qntd += 1
        
print("A palavra",'"', palavra ,'"', "possui", qntd, "letras 'a'")