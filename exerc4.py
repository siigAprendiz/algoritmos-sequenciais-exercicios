"""
 Escreva um algoritmo que solicite a temperatura em graus Celsius e a converta para Fahrenheit.
Utilize a fórmula abaixo:
𝐹 = 𝐶 ∗ 1.8 + 32
"""

tempCelsius = int(input("Digite a temperatura em Celsius: "))

tempFahrenheit = tempCelsius * 1.8 + 32

print(f"Esta temperatura equivale a {tempFahrenheit}°F")
