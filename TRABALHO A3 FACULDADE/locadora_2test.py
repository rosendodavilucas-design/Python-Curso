
class Veiculo:
    def __init__(self, modelo, placa, diaria):
        self.modelo = modelo
        self.placa = placa
        self.diaria = diaria
        self.disponivel = True


class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf


veiculos = []
clientes = []
colaboradores = []

while True:
    print("\n==============================")
    print("     LOCADORA DE VEICULOS")
    print("==============================")
    print("1 - Cadastrar veiculo")
    print("2 - Cadastrar cliente")
    print("3 - Cadastrar colaborador")
    print("4 - Calcular aluguel")
    print("0 - Sair")
    print("==============================")

    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        modelo = input("Modelo: ")
        placa = input("Placa: ")
        diaria = float(input("Valor da diaria: "))

        veiculos.append(Veiculo(modelo, placa, diaria))
        print("Veiculo cadastrado!")

    elif opcao == "2":
        nome = input("Nome do cliente: ")
        cpf = input("CPF: ")

        clientes.append(Cliente(nome, cpf))
        print("Cliente cadastrado!")

    elif opcao == "3":
        nome = input("Nome do colaborador: ")
        cargo = input("Cargo: ")

        colaboradores.append([nome, cargo])
        print("Colaborador cadastrado!")

    elif opcao == "4":
        if len(veiculos) == 0 or len(clientes) == 0:
            print("Cadastre um veiculo e um cliente primeiro.")

        else:
            print("\n--- CLIENTES ---")
            for i, c in enumerate(clientes):
                print(i, "-", c.nome)

            cliente = int(input("Escolha o cliente: "))

            print("\n--- VEICULOS ---")
            for i, v in enumerate(veiculos):
                if v.disponivel:
                    print(i, "-", v.modelo, v.placa)

            numero = int(input("Escolha o veiculo: "))
            dias = int(input("Quantidade de dias: "))

            veiculo = veiculos[numero]

            if veiculo.disponivel and dias > 0:
                valor = veiculo.diaria * dias
                seguro = valor * 0.25

                if dias >= 10:
                    desconto = valor * 0.20
                elif dias >= 6:
                    desconto = valor * 0.10
                elif dias >= 3:
                    desconto = valor * 0.05
                else:
                    desconto = 0

                total = valor + seguro - desconto

                print("\n--- RESUMO DO ALUGUEL ---")
                print("Cliente:", clientes[cliente].nome)
                print("Veiculo:", veiculo.modelo)
                print("Dias:", dias)
                print("Seguro: R$", seguro)
                print("Desconto: R$", desconto)
                print("Total: R$", total)

            else:
                print("Veiculo indisponivel ou dias invalidos.")

    elif opcao == "0":
        print("Sistema encerrado!")
        break

    else:
        print("Opcao invalida!")
