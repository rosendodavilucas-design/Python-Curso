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


class Colaborador:
    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo


class Locacao:
    def __init__(self, cliente, veiculo, dias, seguro, desconto, total):
        self.cliente = cliente
        self.veiculo = veiculo
        self.dias = dias
        self.seguro = seguro
        self.desconto = desconto
        self.total = total
        self.ativa = True  # útil para a devolução


def ler_float(msg):
    while True:
        try:
            valor = float(input(msg).replace(",", "."))
            if valor > 0:
                return valor
            print("O valor deve ser maior que zero.")
        except ValueError:
            print("Digite um numero valido.")


def ler_int(msg, minimo, maximo):
    while True:
        try:
            valor = int(input(msg))
            if minimo <= valor <= maximo:
                return valor
            print(f"Digite um numero entre {minimo} e {maximo}.")
        except ValueError:
            print("Digite um numero inteiro valido.")


veiculos = []
clientes = []
colaboradores = []
locacoes = []

while True:
    print("\n==============================")
    print("     LOCADORA DE VEICULOS")
    print("==============================")
    print("1 - Cadastrar veiculo")
    print("2 - Cadastrar cliente")
    print("3 - Cadastrar colaborador")
    print("4 - Calcular aluguel")
    print("5 - Consultar locacoes")
    print("0 - Sair")
    print("==============================")

    opcao = input("Escolha uma opcao: ").strip()

    if opcao == "1":
        modelo = input("Modelo: ").strip()
        placa = input("Placa: ").strip().upper()

        if any(v.placa == placa for v in veiculos):
            print("Ja existe um veiculo com essa placa.")
        else:
            diaria = ler_float("Valor da diaria: ")
            veiculos.append(Veiculo(modelo, placa, diaria))
            print("Veiculo cadastrado!")

    elif opcao == "2":
        nome = input("Nome do cliente: ").strip()
        cpf = input("CPF: ").strip()

        if any(c.cpf == cpf for c in clientes):
            print("Ja existe um cliente com esse CPF.")
        else:
            clientes.append(Cliente(nome, cpf))
            print("Cliente cadastrado!")

    elif opcao == "3":
        nome = input("Nome do colaborador: ").strip()
        cargo = input("Cargo: ").strip()

        colaboradores.append(Colaborador(nome, cargo))
        print("Colaborador cadastrado!")

    elif opcao == "4":
        disponiveis = [v for v in veiculos if v.disponivel]

        if not clientes:
            print("Cadastre um cliente primeiro.")
        elif not disponiveis:
            print("Nao ha veiculos disponiveis no momento.")
        else:
            print("\n--- CLIENTES ---")
            for i, c in enumerate(clientes):
                print(i, "-", c.nome)
            cliente = clientes[ler_int("Escolha o cliente: ", 0, len(clientes) - 1)]

            print("\n--- VEICULOS DISPONIVEIS ---")
            for i, v in enumerate(disponiveis):
                print(i, "-", v.modelo, v.placa, f"(R$ {v.diaria:.2f}/dia)")
            veiculo = disponiveis[ler_int("Escolha o veiculo: ", 0, len(disponiveis) - 1)]

            dias = ler_int("Quantidade de dias: ", 1, 365)

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
            print("Cliente:", cliente.nome)
            print("Veiculo:", veiculo.modelo)
            print("Dias:", dias)
            print(f"Seguro: R$ {seguro:.2f}")
            print(f"Desconto: R$ {desconto:.2f}")
            print(f"Total: R$ {total:.2f}")

            veiculo.disponivel = False
            locacoes.append(Locacao(cliente, veiculo, dias, seguro, desconto, total))

    elif opcao == "5":
        print("\n--- LOCACOES REALIZADAS ---")
        if not locacoes:
            print("Nenhuma locacao registrada.")
        for l in locacoes:
            status = "Ativa" if l.ativa else "Encerrada"
            print(f"{l.cliente.nome} | {l.veiculo.modelo} ({l.veiculo.placa}) | "
                  f"{l.dias} dias | R$ {l.total:.2f} | {status}")

    elif opcao == "0":
        print("Sistema encerrado!")
        break

    else:
        print("Opcao invalida!")

# PROXIMA ETAPA: desenvolver a devolucao dos veiculos.