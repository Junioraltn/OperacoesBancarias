menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    if saldo > 0:
        opcao = str(input(menu))

        if ((opcao.lower() == "s") or (opcao.lower() == "sacar")):
            valor = float(input("Informe o valor do saque: "))

            if (valor > saldo):
                print("Saldo Insuficiente.")

            elif (valor > limite):
                print("O valor excede o limite da operação.")

            elif (numero_saques >= LIMITE_SAQUES):
                print("Número máximo de saques alcançado.")

            elif valor > 0:
                saldo -= valor
                extrato += f"Saque:    R$ "+f"{valor:.2f}".rjust(10)+"\n"
                numero_saques += 1

            else:
                print("O valor informado é inválido.")

    else:
        menu2 = menu[:16]+menu[26:]
        opcao = input(menu2)

    if ((opcao.lower() == "d") or (opcao.lower() == "depositar")):
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += "Depósito: R$ "+f"{valor:.2f}".rjust(10)+"\n"

        else:
            print("O valor informado é inválido.")

    elif ((opcao.lower() == "e") or (opcao.lower() == "extrato")):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif ((opcao.lower() == "q") or (opcao.lower() == "sair")):
        break

    else:
        print("Operação inválida, por favor escolha uma operação entre as opções.")
