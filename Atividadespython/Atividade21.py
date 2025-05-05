#Calcule quantos salários mínimos ganha um funcionário.
# Dados
salario_minimo = float(input("Informe o valor do salário mínimo: "))
salario_funcionario = float(input("Informe o valor do salário do funcionário: "))
# Cálculo da quantidade de salários mínimos
quantidade_salarios_minimos = salario_funcionario / salario_minimo
# Resultado
print("O funcionário ganha o equivalente a:", quantidade_salarios_minimos, "salários mínimos")
