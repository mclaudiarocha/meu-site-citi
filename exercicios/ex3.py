# %%
tipo_sorvete = input("Entre com o tipo de sorvete: [casquinha/cascão/cestinha]")
sabor = input("Entre com o sabor do sorvete: [morango/creme/chocolate]")
cobertura = input("Entre com o sabor da cobertura: [caramelo/morango/chocolate]")

valor = 0 

if tipo_sorvete == "casquinha":
    valor = valor + 1.00
elif tipo_sorvete == "cascão":
    valor = valor + 2.50
elif tipo_sorvete == "cestinha":
    valor = valor + 4.00

else:
    print("Não temos essa opção ;()")

if cobertura == "caramelo":
    valor = valor + 1.50
elif cobertura == "morango":
    valor = valor + 1.50
elif cobertura == "chocolate":
    valor = valor + 1.50
elif cobertura == "nenhuma":
    print("ok!")

else:
    print("Não temos essa opção ;()")

print("Seu sorvete", tipo_sorvete, "de", sabor, "com cobertura de", cobertura, "custa R$",valor)
     



# %%
