# Valores das horas trabalhadas e as taxas
valor_hora_normal = 10.00
valor_hora_extra = 15.00
# Solicita as horas trabalhadas normais e extras
horas_normais = float(input("Digite o número de horas normais trabalhadas: "))
horas_extras = float(input("Digite o número de horas extras trabalhadas: "))
# Calcular o salário bruto e líquido
salario_bruto = (horas_normais * valor_hora_normal) + (horas_extras * valor_hora_extra)
salario_liquido = salario_bruto - (salario_bruto * 0.10)
#resultados
print(f"Salário Bruto: R${salario_bruto:.2f}")
print(f"Salário Líquido: R${salario_liquido:.2f}")