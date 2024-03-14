"""
Escreva um algoritmo que solicite o peso e a altura de uma pessoa e calcule o seu IMC (Índice de
Massa Corpórea). Utilize a fórmula abaixo:
IMC = Peso / Altura²
"""

peso = int(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura ** 2)

print(f"Seu IMC é de {imc}")
