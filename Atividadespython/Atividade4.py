#Cálculo do gasto total da granja Frangotech
 # quantidade de frangos
num_frangos = 1000
# custo do anel com chip
custo_anel_chip = 4.00 
# custo do anel de alimento 
custo_anel_alimento = 3.50  
# Cálculo do gasto total
total_gasto = num_frangos * (custo_anel_chip + 2 * custo_anel_alimento)
print(f"Gasto total da granja para marcar {num_frangos} frangos: R$ {total_gasto:.2f}")