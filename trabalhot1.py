#2324290083 - Jayme Matheus da Silva Pinto

valor = float(input("Digite o valor do investimento: "))
dias = int(input("Digite a quantidade de dias da aplicação: "))

taxaanual = 0.1415  

taxadiaria = (1 + taxaanual) ** (1 / 365) - 1


montantebruto = valor * ((1 + taxadiaria) ** dias)
rendimentobruto = montantebruto - valor


tabelaiof = {
    1: 0.96, 2: 0.93, 3: 0.90, 4: 0.86, 5: 0.83, 6: 0.80, 7: 0.76,
    8: 0.73, 9: 0.70, 10: 0.66, 11: 0.63, 12: 0.60, 13: 0.56, 14: 0.53,
    15: 0.50, 16: 0.46, 17: 0.43, 18: 0.40, 19: 0.36, 20: 0.33, 21: 0.30,
    22: 0.26, 23: 0.23, 24: 0.20, 25: 0.16, 26: 0.13, 27: 0.10, 28: 0.06,
    29: 0.03, 30: 0.00
}


if dias <= 30:
    diasiof = dias
else:
    diasiof = 30
percentual_iof = tabelaiof[diasiof]
descontoiof = rendimentobruto * percentual_iof          
rendimentoaposiof = rendimentobruto - descontoiof


if dias <= 180:
    irpercentual = 0.225
elif dias <= 360:
    irpercentual = 0.20
elif dias <= 720:                    
    irpercentual = 0.175
else:
    irpercentual = 0.15


desconto_ir = rendimentoaposiof * irpercentual

valorliquido = valor + rendimentoaposiof - desconto_ir


print("\n  -- Valores da Aplicação --")
print(f"Montante Bruto: R$ {montantebruto:.2f}")
print(f"Rendimento Bruto: R$ {rendimentobruto:.2f}")
print(f"Desconto IOF: R$ {descontoiof:.2f}")
print(f"Desconto IR: R$ {desconto_ir:.2f}")
print(f"Resultado Líquido Final: R$ {valorliquido:.2f}")
