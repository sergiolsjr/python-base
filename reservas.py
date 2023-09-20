#!/usr/bin/env python3

# hotel = [{"codigo": "1", "nome": "Master", "preco": 500},
#          {"codigo": "2", "nome": "Familia", "preco": 200},
#          {"codigo": "3", "nome": "Quarto Single", "preco": 100},
#          {"codigo": "4", "nome": "Simples", "preco": 50}]

print("QUARTOS DISPONÍVEIS")
print("#"*30)
print("N -", "   Nome  -", "  Preço  ")
print("")

for quarto in open("quartos.txt", "r"):
    hotel = [{"codigo": (quarto.split(",")[0])},
             {"nome": (quarto.split(",")[1])}, 
             {"preco": (quarto.split(",")[2])}]
    print(hotel[0]["codigo"], "-", hotel[1]["nome"], "-", hotel[2]["preco"])
    
    
    


# print("N Quarto - Nome - Preço")
# for quarto in hotel:









    


#nome_cliente = input("Informe seu nome: ")
    
    
# num_quarto = input("Informe o número do quarto: ")
# qtd_dias = input("Informe a quantidade de dias: ")


    
    