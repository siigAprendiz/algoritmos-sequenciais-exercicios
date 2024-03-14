"""
O sistema de avaliação de determinada disciplina, é composto por três notas. Escreva um
programa que solicita as notas de um aluno, calcula e exibe a média aritmética deste aluno.
"""

primeiraNota = float(input("Digite sua primeira nota: "))
segundaNota = float(input("Digite sua segunda nota: "))
terceiraNota = float(input("Digite sua terceira nota: "))

mediaAritmetica = ((primeiraNota + segundaNota + terceiraNota)/3)

print(f"Sua média foi de {mediaAritmetica}")
