#!/usr/bin/env python3

import sys

quartos = {}
ocupados = {}

try:
    for line in open("reservas.txt", "r"):
            nome, num_quarto, qtd_dias = line.strip().split(",")
            ocupados[int(num_quarto)] = {"nome": nome,
                                        "qtd_dias": qtd_dias
            }
except FileNotFoundError as error:
    print(error)
    sys.exit(1)
    
print("Lista de Quartos")
print("#"*45)

try:
    
    for line in open("quartos.txt", "r"):
        codigo, nome, preco = line.strip().split(",")
        quartos[int(codigo)] = {
            "nome": nome,
            "preco": float(preco),
            "disponivel": "Indisponível" if int(codigo) in ocupados else "Disponível"
        }
        disponivel = quartos[int(codigo)]["disponivel"]
        print(f"{codigo} - {nome} - R$ {preco} - {disponivel}")

except FileNotFoundError as error:
    print(error)
    sys.exit(1)
    
    

print("#"*45)
    
if len(ocupados) == len(quartos):
    print("HOTEL LOTADO!!!")
    sys.exit(1)

nome_cliente = input("Informe seu nome: ")
    
try:
    num_quarto = int(input("Informe o número do quarto: ").strip())
    if num_quarto in ocupados:
        print("Quarto Indisponível")
        sys.exit(0)
except KeyError:
    print(f"O quarto {num_quarto} não existe.")
    sys.exit(0)
except ValueError:
    print("Número inválido, digite apenas digitos.")
    sys.exit(0)
    
try:
    qtd_dias = int(input("Informe a quantidade de dias: ").strip())
except ValueError:
    print("Número inválido, digite apenas dígitos.")
    sys.exit(0)
    
print("#"*45)

nome_quarto = quartos[num_quarto]["nome"]
preco_quarto = quartos[num_quarto]["preco"]
total = preco_quarto * qtd_dias
print(f"{nome_cliente} você escolheo o(a) {nome_quarto} e pagará R$ {total}") 

with open("reservas.txt", "a") as file_:
    file_.write(f"{nome_cliente},{num_quarto},{qtd_dias}\n")

    