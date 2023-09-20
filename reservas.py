#!/usr/bin/env python3

print("QUARTOS DISPONÍVEIS")
print("#"*30)
print("N -", "   Nome  -", "  Preço  ")
print("")

quartos = {}
for line in open("quartos.txt", "r"):
    codigo, nome, preco = line.strip().split(",")
    quartos[int(codigo)] = {"nome": nome,
                       "preco": float(preco)}
print(quartos)
    
   
    
    
    


#nome_cliente = input("Informe seu nome: ")
    
    
# num_quarto = input("Informe o número do quarto: ")
# qtd_dias = input("Informe a quantidade de dias: ")


    
    