 #Cálculo da quantidade de água e suco para fazer X litros de refresco
# Leitura da quantidade total de refresco desejada
litros_refresco = float(input("Digite a quantidade total de refresco desejada em litros: "))
# Cálculo das partes necessárias
parte_total = 10  # Total das partes (8 partes água + 2 partes suco)
litros_agua = (8 / parte_total) * litros_refresco
litros_suco = (2 / parte_total) * litros_refresco

print(f"Para fazer {litros_refresco} litros de refresco, são necessários:")
print(f"{litros_agua:.2f} litros de água")
print(f"{litros_suco:.2f} litros de suco")