print("***MENU***")
print ("1 - somar")
print ("2 - subtrair")
print ("3 - Multiplicar")
print ("4 - Dividir")
operaçao = int(input("Digite a operação: "))
Var1 = int(input("Digite o  valor 1: "))
Var2 = int(input("Digite o valor 2: "))

if operaçao == 1:
    print(Var1 + Var2)
elif operaçao == 2:
    print(Var1 - Var2)
elif operaçao == 3:
    print (Var1 * Var2)
elif operaçao == 4:
    print(Var1 / Var2)
else:
    print ("Operação inválida")