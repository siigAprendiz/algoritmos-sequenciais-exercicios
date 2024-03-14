"""
Uma concessionária de veículos paga aos seus vendedores um salário base de R$ 2.500,00.
Além disso, uma comissão de R$ 200,00 por cada carro vendido e 2% do valor total das vendas.
Escreva um programa que solicite o nome do vendedor, a quantidade de carros vendidos
e o valor total de suas vendas. O programa deve calcular e exibir o salário final
do vendedor.
"""

nome = input("Digite seu nome: ")
qtdCarrosVendidos = int(input("Digite a quantidade de carros vendidos que você vendeu: "))
valorTotalVendas = float(input("Digite o valor total de suas vendas: "))

salario = 2500 + 200*qtdCarrosVendidos + 0.02*valorTotalVendas

input(f"Nome do vendedor: {nome}\n Quantidade de carros: {qtdCarrosVendidos}\n "
      f"Valor total das vendas: {valorTotalVendas}\n "
      f"O vendedor {nome} receberá um salário de R$: {salario}")
