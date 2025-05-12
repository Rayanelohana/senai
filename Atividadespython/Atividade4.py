#gasto total da granja Frangotech
num_frangos = 1000
custo_anel_chip = 4.00 
custo_anel_alimento = 3.50  
#cálculo do gasto total
total_gasto = num_frangos * (custo_anel_chip + 2 * custo_anel_alimento)
print(f"Gasto total da granja para marcar {num_frangos} frangos: R$ {total_gasto:.2f}")