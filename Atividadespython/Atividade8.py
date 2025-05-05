 #Cálculo da altura do prédio usando proporção
# Leitura das medidas
altura_usuario = float(input("Digite sua altura em metros: "))
sombra_usuario = float(input("Digite o comprimento da sua sombra em metros: "))
sombra_predio = float(input("Digite o comprimento da sombra do prédio em metros: "))
# Cálculo da altura do prédio
altura_predio = (altura_usuario * sombra_predio) / sombra_usuario
print(f"A altura do prédio é: {altura_predio:.2f} metros")
