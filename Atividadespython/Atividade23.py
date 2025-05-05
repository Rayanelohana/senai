#Calcule a idade em anos, meses, dias e semanas.

# Dados
ano_nascimento = int(input("Informe o ano de nascimento da pessoa: "))
ano_atual = int(input("Informe o ano atual: "))

# Cálculo da idade
idade_anos = ano_atual - ano_nascimento
idade_meses = idade_anos * 12
idade_dias = idade_anos * 365  # Aproximando, sem considerar anos bissextos
idade_semanas = idade_dias // 7

# Resultados
print("Idade em anos:", idade_anos)
print("Idade em meses:", idade_meses)
print("Idade em dias:", idade_dias)
print("Idade em semanas:", idade_semanas)
