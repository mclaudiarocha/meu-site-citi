#Faça um programa que receba 4 notas de um aluno. Retorne a média dessas notas, a menor e a maior nota:

#Média: x
#Menor: y
#Maior: z

notas =  [int(input(f"Entre com as suas notas da AV{i+1}:")) for i in range(4)]

print(f"Média:{sum(notas)/4}")
print(f"Menor nota:{min(notas)}")
print(f"Mior nota:{max(notas)}")