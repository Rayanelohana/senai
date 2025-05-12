#quantidade total de litros de refrigerante comprados
qtd_latas = 20 
qtd_garrafas_600ml = 15 
qtd_garrafas_2l = 10 
# Cálculo dos litros totais
litros_lata = qtd_latas * 0.350 
litros_garrafa_600ml = qtd_garrafas_600ml * 0.600  
litros_garrafa_2l = qtd_garrafas_2l * 2.0  
total_litros = litros_lata + litros_garrafa_600ml + litros_garrafa_2l
print(f"Total de litros de refrigerante comprados: {total_litros:.2f} L")
