"""
Escreva um programa que receba a base e a altura de um triângulo e
calcule a sua área.
"""

baseEmMetros = float(input("Digite a medida da base do triãngulo (em metros): "))
alturaEmMetros = float(input("Digite a medida da altura do triãngulo (em metros): "))

areaEmMetros = ((baseEmMetros * alturaEmMetros) / 2)

print(f"A área desse triãngulo é de {areaEmMetros} metros")
