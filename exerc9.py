"""
Escreva um programa que solicita ao usuário dois números inteiros e armazena nas
variáveis A e B.
Troque os seus conteúdos fazendo com que o valor que está em A passe para B e vice-versa.
Ao final exiba na tela os valores que ficaram armazenados nas variáveis A e B respectivamente
"""

A = int(input("Digite um número inteiro para a variável A: "))
B = int(input("Digite um número inteiro para a variável B: "))

primeiroValor = A
segundoValor = B

A = segundoValor
B = primeiroValor

print("Falha no Sistema! Os números foram trocados...")
print(f"Agora o valor de A é {A} e o valor de B é {B}")
