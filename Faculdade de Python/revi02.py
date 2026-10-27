num1 = float(input("Insira a nota 1: "))
num2 = float(input("Insira a nota 2: "))
soma = num1 + num2
média = soma / 2
if média >= 7:
    print("Passou")
elif média < 7:
    print("Reprovou")
elif média <= 9:
    print("Otimo desempenho")
