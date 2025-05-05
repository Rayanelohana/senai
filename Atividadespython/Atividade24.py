# Calcule quanto restará do salário de João após pagar as contas com multa.
# informacoes
salario = 1200.00
conta1 = 200.00
conta2 = 120.00
# Cálculo da multa
multa1 = conta1 * 0.02
multa2 = conta2 * 0.02
# Total a pagar com as multas
total_contas = (conta1 + multa1) + (conta2 + multa2)
# Saldo restante do salário
saldo_restante = salario - total_contas
# Resultado
print("Restará do salário de João: R$", saldo_restante)