#Calcule a comissão e o salário final de um funcionário.
# Dados
salario_fixo = float(input("Informe o salário fixo do funcionário: "))
vendas = float(input("Informe o valor das vendas: "))
# Cálculo da comissão e salário final
comissao = vendas * 0.04
salario_final = salario_fixo + comissao
# Resultados
print("A comissão do funcionário é:", comissao)
print("O salário final do funcionário é:", salario_final)