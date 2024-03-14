"""
Faça um programa que solicita ao usuário um único número inteiro com
três dígitos e exibe o número invertido.
Exemplo:
Informe um número com 3 dígitos: 136
Número invertido: 631
"""

numeroInfo = int(input("Informe um número com 3 dígitos: "))

centena = numeroInfo // 100
dezena = (numeroInfo % 100)//10
unidade = numeroInfo % 10

print(f"Número invertido: {unidade}{dezena}{centena}")