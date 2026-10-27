print("1 - +")
print("2 - -")
print("3 - *")
print("4 - /")
print("Escolha uma operação")
operaçao = int(input("Digite a operação: "))
Var1 = int(input("Digite o  valor 1: "))
Var2 = int(input("Digite o valor 2: "))

#SÓ CONSEGUE FAZER TODo COM A AJUDA DO PROFESSOR PARTE DE BAIXO

if operaçao == 1:
    print(Var1 + Var2)
elif operaçao == 2:
    print(Var1 - Var2)
elif operaçao == 3:
    print (Var1 * Var2)
elif operaçao == 4:
    print(Var1 / Var2)
else:
    print ("Operação falhou")