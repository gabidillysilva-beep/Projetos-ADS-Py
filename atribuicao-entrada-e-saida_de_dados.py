#Exercíco: Simulação para Supermercado
#Atribuição de variáveis

arroz = 30.00
feijao = 8.99
macarrao = 6.99

#Entrada de dados no caixa

quantidade_arroz = int(input("Digite a quantidade de Arroz: "))
quantidade_feijao = int(input("Digite a quantidade de Feijaõ: "))
quantidade_macarrao = int(input("Digite a quantidade de Macarrão: "))

#Digite a quantidade de Arroz: 2 unidades
#Digite a quantidade de Feijão: 4 unidades
#Digite a quantidade de Macarrão: 3 unidades

#Cáuculo Total

preco_total = (arroz * quantidade_arroz) + (feijao * quantidade_feijao) + (macarrao * quantidade_macarrao)

#Saída de dados

print("Tota do pedido é: R$", preco_total)

