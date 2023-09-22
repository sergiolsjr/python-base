#!/usr/bin/env python3

quartos = {}
ocupados = {}

for line in open("reservas.txt", "r"):
        nome, num_quarto, p_total = line.strip().split(",")
        ocupados[int(num_quarto)] = {"nome": nome,
                                     "p_total": p_total
        }
print("Lista de Quartos")        
for line in open("quartos.txt", "r"):
    codigo, nome, preco = line.strip().split(",")
    quartos[int(codigo)] = {"nome": nome,
                       "preco": float(preco),
                       "disponivel": "Indisponível" if int(codigo) in ocupados else "Disponível"
    }
    #print(quartos[int(codigo)]["disponivel"])
    disponivel = quartos[int(codigo)]["disponivel"]
    print(f"{codigo} - {nome} - R$ {preco} - {disponivel}")
    
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
            arquivo.write("{},{},{}\n".format(nome_cliente, str(num_quarto), str(qtd_dias)))
            #arquivo.writelines(",".join([nome_cliente, str(num_quarto), str(preco_total)]))    
    