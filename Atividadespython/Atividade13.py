#Faça um algoritmo que receba duas notas e calcule a média ponderada.
# nota
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
# Cálculo da média ponderada
media_ponderada = (nota1 * 2 + nota2 * 3) / (2 + 3)
# Resultado
print("A média ponderada é:", media_ponderada)