#!/usr/bin/env python3

quartos = {}
for line in open("quartos.txt", "r"):
    codigo, nome, preco = line.strip().split(",")
    quartos[int(codigo)] = {"nome": nome,
                       "preco": float(preco),
                       "disponivel": True
    }
    print(quartos.items(codigo["disponivel"]))
    # print(f"{codigo} - {nome} - R$ {preco} - {disponivel}")
    
print("#"*35)
nome_cliente = input("Informe seu nome: ")
num_quarto = int(input("Informe o número do quarto: "))
qtd_dias = input("Informe a quantidade de dias: ")

for codigo, dados in quartos.items():
    if num_quarto == codigo:
        preco_total = dados["preco"] * int(qtd_dias)
        print("#"*35)
        print(f"{nome_cliente} - {num_quarto} - R$ {preco_total:.2f}") 
        with open("reservas.txt", "a") as arquivo:
            arquivo.write("{},{},{}\n".format(nome_cliente, str(num_quarto), str(preco_total)))
            #arquivo.writelines(",".join([nome_cliente, str(num_quarto), str(preco_total)]))
            
            
    
        

    
    # preco_total = dados["preco"] * int(qtd_dias)
    
    # print(f"{nome_cliente} - {num_quarto} - R$ {preco_total}")    


    
    