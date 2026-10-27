vendas = []
for dia in range(1, 6):
    valor = float(input(f"Digite a venda do dia {dia}: R$ "))
    vendas.append(valor)

total = 0
dias_acima = 0

for valor in vendas:
    total += valor
    if valor >500:
        dias_acima += 1
media = total / len(vendas)

print(f"Total vendido: R$ {total} :")
print(f"Vendas díarias: R$ {media}")
print(f"Dias com vendas acima de R$ 500,0")

if total >= 2000:
    print("Meta atingida")
else:
    print("Meta não atingida")