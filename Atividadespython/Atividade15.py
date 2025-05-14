#comissão e o salário final de um funcionário.
salario_fixo = float(input("Informe o salário fixo do funcionário: "))
vendas = float(input("Informe o valor das vendas: "))
#comissão e salário final
comissao = vendas * 0.04
salario_final = salario_fixo + comissao
# Resultado
print("A comissão do funcionário é:", comissao)
print("O salário final do funcionário é:", salario_final)