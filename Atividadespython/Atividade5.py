#quantidade de novelos de lã necessários para produzir blusas
num_blusas = 50  
metros_por_blusa = 120 
metros_por_novelo = 125  
# Cálculo
total_metros = num_blusas * metros_por_blusa
novelos_necessarios = total_metros / metros_por_novelo
print(f"Novelos de lã necessários para produzir {num_blusas} blusas: {novelos_necessarios:.2f}")