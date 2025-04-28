# %%
agua = input("Você prefere água natural ou com gás? [natural/gas]")
quantidade = int(input("Quantas águas você deseja?"))

total = 0

if agua == "natural":
    total = 1.5 * quantidade

elif agua == "gas":
    total = 2.5 * quantidade    
    
else:
    print("Faça uma escolha válida")


print("Seu total é R$",+total)


