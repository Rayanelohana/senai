#Cálculo da quantidade de novelos de lã necessários para produzir blusas
num_blusas = 50  # quantidade de blusas a serem produzidas
metros_por_blusa = 120  # metros de fio necessários por blusa
metros_por_novelo = 125  # metros de fio em cada novelo
# Cálculo dos novelos necessários
total_metros = num_blusas * metros_por_blusa
novelos_necessarios = total_metros / metros_por_novelo
print(f"Novelos de lã necessários para produzir {num_blusas} blusas: {novelos_necessarios:.2f}")