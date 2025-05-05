#Cálculo da quantidade total de litros de refrigerante comprados
qtd_latas = 20 # quantidade de latas compradas
qtd_garrafas_600ml = 15 # quantidade de garrafas de 600 ml compradas
qtd_garrafas_2l = 10 # quantidade de garrafas de 2 litros compradas
# Cálculo dos litros totais
litros_lata = qtd_latas * 0.350 # litros em latas
litros_garrafa_600ml = qtd_garrafas_600ml * 0.600  # litros em garrafas de 600ml
litros_garrafa_2l = qtd_garrafas_2l * 2.0  # litros em garrafas de 2 litros
total_litros = litros_lata + litros_garrafa_600ml + litros_garrafa_2l
print(f"Total de litros de refrigerante comprados: {total_litros:.2f} L")
