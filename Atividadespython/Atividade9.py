 #Cálculo da quantidade de água e suco para fazer X litros de refresco
litros_refresco = float(input("Quantidade total de refresco desejada em litros: "))
parte_total = 10  
litros_agua = (8 / parte_total) * litros_refresco
litros_suco = (2 / parte_total) * litros_refresco
print(f"Para fazer {litros_refresco} litros de refresco, são necessários:")
print(f"{litros_agua:.2f} litros de água")
print(f"{litros_suco:.2f} litros de suco")