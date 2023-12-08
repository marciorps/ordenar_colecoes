from operator import itemgetter

# #Ordenar por propriedades
# nomes = ['Zack', 'Camilla', 'Julius', 'Romer']
# valores = [31, 23, 6, 36, 21, 33, 37, 7, 20, 23]
# # nomes.sort()
# # valores.sort()
# # print(nomes)
# # print(valores)
# pessoas = [{'nome': 'john', 'idade': 32, 'nivel_acesso': 2}, {'nome': 'carol', 'idade': 18, 'nivel_acesso': 3}, 
# {'nome': 'Thomas', 'idade': 45, 'nivel_acesso': 5}, {'nome': 'Amanda', 'idade': 23, 'nivel_acesso': 1}]
# pessoas.sort(key=itemgetter('nivel_acesso'))
# print(pessoas)


# produtos = [('celular', 750), ('bicicleta', 1500), ('microfone', 500)]
# produtos.sort(key=itemgetter(0), reverse=True)
# print(produtos)


# matriz = [[5, 10], [15,21], [1, 5]]
# matriz.sort(key=itemgetter(1))
# print(matriz)

#Desafio 1
##Ordene a lista de produtos abaixo pelo preço em ordem crescente
produtos = [{'nome': 'celular', 'preco': 1500}, {'nome': 'monitor', 'preco': 500}, {'nome': 'microfone', 'preco': 300},]
produtos.sort(key=itemgetter('preco'))
print(produtos)

#Desafio 2
##Ordene em ordem decrescente a lista de equipamento_filmagem por valor do equipamento

equipamento_filmagem = [('tripé', 300), ('câmera', 1700), ('iluminação', 200),]
equipamento_filmagem.sort(key=itemgetter(1), reverse=True)
print(equipamento_filmagem)

#Desafio 3
##Ordene em ordem crescente a cotacao_moedas com base no valor da moeda
cotacao_moedas = [['usd', 5.25], ['brl', 1.56], ['eur', 6.47]]
cotacao_moedas.sort(key=itemgetter(1))
print(cotacao_moedas)