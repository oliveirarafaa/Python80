# -*- coding: utf-8 -*-
"""aula 11

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13hFOfhYQoUDb7kjsOY9EkzRezdqpuHLU

Aula 11
"""

#Lista de frutas
frutas = ['maçã', 'banana', 'laranja', 'uva']

#Iterando sobre a lista de frutas com enumerate
for indice, fruta in enumerate(frutas):
    print(f'Índice: {indice}, Fruta: {fruta}')

print('---------------------------')

lista = ["Caio", "Fernando", 'Julio', 'Maria']

for i, alunos in enumerate(lista, start=1):
    print('chamada', i , 'Nomes', alunos)

cores = {'vermelho': '#FF0000', 'verde': '#00FF00', 'azul': '#0000FF'}
for indice, (cor, codigo) in enumerate(cores.items()):
    print(f'Índice: {indice}, Cor: {cor}, Código: {codigo}')

print('--------------------------------------')

nomes = ['José', 'Maci', 'Tamires', 'Cassyele', 'Rafael']
print('Lista de Alunos:')
for index, nome in enumerate(nomes, start = 1):
    print('nome', nome, 'número:', index)

lista = []
print(lista)
lista.append(7)
lista.append(13)
lista.append(154)

print(lista)

lista.remove(13)
del lista[0]
print('removeu', lista)

# Exercício 1: Crie uma lista chamada pessoas que contenha os números inteiros de pessoa1 a pessoa5 e imprima-a na tela.

nomes = ['João', 'Pietro', 'Maria', 'Jaira', 'Marley']
print('Lista de Nomes:')
for index, nome in enumerate(nomes, start = 1):
    print('Nome:', nome, index)

# Exercício 2: Acesse e imprima o terceiro elemento da lista numeros.

lista  = ['Maracuja', 'Morango', 'Melancia', 'Maçâ', 'Banana']
print(lista[2])

# Exercício 3: Adicione o número 9 à lista `numeros` e imprima a lista atualizada.

numeros = [1, 2, 3, 4, 5, 6, 7]
print(numeros)
print('-------------------------------')

numeros.append(9)

print(numeros)

# Exercício 4: Remova o número 5 da lista numeros e imprima a lista resultante.

numeros = [1, 2, 3, 4, 5, 6, 7]
numeros.remove(5)

print(numeros)

# **Exercício 5:** Crie uma lista chamada carros contendo três nomes de carros diferentes. Em seguida, concatene essa lista com a lista `numeros` e imprima o resultado.

carros = ['Lancer', 'Polo', 'L200']
print('Lista de carros')
for index, carro in enumerate(carros, start = 1):
    print('Carro:', carro, index)