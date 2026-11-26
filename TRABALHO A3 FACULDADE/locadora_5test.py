
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
locacoes = []

faturamento = 0

while True:
    print("\n==============================")
    print("     LOCADORA DE VEICULOS")
    print("==============================")
    print("1 - Cadastrar veiculo")
    print("2 - Cadastrar cliente")
    print("3 - Cadastrar colaborador")
    print("4 - Calcular aluguel")
    print("5 - Consultar locacoes")
    print("6 - Devolver veiculo")
    print("7 - Consultar faturamento")
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

                # Registra o aluguel e atualiza o faturamento
                veiculo.disponivel = False
                locacoes.append([clientes[cliente].nome,
                                 veiculo.modelo, dias, total, veiculo])

                faturamento += total

            else:
                print("Veiculo indisponivel ou dias invalidos.")

    elif opcao == "5":
        print("\n--- LOCACOES REALIZADAS ---")

        for i, aluguel in enumerate(locacoes):
            print(i, "-", aluguel[0], "-", aluguel[1])

    elif opcao == "6":
        print("\n--- VEICULOS ALUGADOS ---")

        ativos = []

        for i, aluguel in enumerate(locacoes):
            if not aluguel[4].disponivel:
                print(i, "-", aluguel[0], "-", aluguel[1])
                ativos.append(i)

        if len(ativos) > 0:
            numero = int(input("Numero da locacao devolvida: "))

            if numero in ativos:
                locacoes[numero][4].disponivel = True
                print("Veiculo devolvido com sucesso!")
            else:
                print("Locacao invalida ou ja devolvida.")
        else:
            print("Nenhum veiculo alugado.")

    elif opcao == "7":
        print("\n--- FATURAMENTO ---")
        print("Total acumulado: R$", round(faturamento, 2))

    elif opcao == "0":
        print("Sistema encerrado!")
        break

    else:
        print("Opcao invalida!")

# PROXIMA ETAPA: melhorar a organizacao das classes e metodos.
