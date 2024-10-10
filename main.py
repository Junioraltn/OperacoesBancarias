interaveis = {}
AGENCIA = "0001"

contas = {}
clientes = {}

dadosConta = []
dadosCliente = ["cpf","nome","dataNascimento","endereco",contas]

def ValidacaoDoCliente():
    global dadosCliente
    while True:
        while True:
            dadosCliente[0] = input("Digite seu CPF para realizar operações! ")
            if len(dadosCliente[0]) != 11:
                print("CPF inválido")
            else:
                TriagemDeClientes(dadosCliente[0])
                break
        break

def TriagemDeClientes(cpf):
    global dadosCliente
    if (cpf in clientes):
        dadosCliente = [cpf if i == 0 else clientes[cpf][i-1] for i in range(0,3)]
        return EscolherConta(cpf)
    return CadastrarCliente(cpf)

def CadastrarCliente(cpf):
    nome = input("Qual o nome do cliente? ")
    dataNascimento = input("Qual a data de Nascimento? ")
    endereco = input("Qual é o endereço? ")
    clientes[cpf] = [nome,dataNascimento,endereco,[]]
    CriarConta(cpf)
    return EscolherConta(cpf)

def CriarConta(cpf):
    if len(clientes[cpf][3]) == 0:
        funcoesConta = {"saldo":0,"limite":500,"numero_saques":0,"extrato":"","LIMITE_SAQUES":3}
        clientes[cpf][3].append(1)
        contas[cpf] = {1:{"agencia":AGENCIA,"funcoesConta":funcoesConta}}
        return
    funcoesConta = {"saldo":0,"limite":500,"numero_saques":0,"extrato":"","LIMITE_SAQUES":3}
    conta = clientes[cpf][3][-1] +1
    clientes[cpf][3].append(conta)
    contas[cpf][conta] = {"agencia":AGENCIA,"funcoesConta":funcoesConta}

def EscolherConta(cpf):
    global dadosConta
    global interaveis
    global dadosCliente
    if len(clientes[cpf][3]) != 1:
        print(f"Em qual dessas contas {clientes[cpf][3]}, deseja entrar? ")
        entrada = int(input("Digite o número da conta: "))
        if entrada in clientes[cpf][3]:
            dadosConta = list(contas[cpf][entrada].values())
            dadosConta.insert(0,entrada)
            interaveis = dadosConta[2]
            dadosCliente = [cpf if i == 0 else clientes[cpf][i-1] for i in range(0,4)]
    else:
        dadosConta = list(contas[cpf][1].values())
        dadosConta.insert(0,1)
        interaveis.update(dadosConta[2])
        dadosCliente = [cpf if i == 0 else clientes[cpf][i-1] for i in range(0,4)]

def Menu():
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [n] Nova Conta
    [q] Sair

    => """
    return menu

def TriagemDeOperacoes(opcoes):
    global interaveis
    while True:
        if (interaveis["saldo"] > 0):
            opcao = str(input(Menu()))
            if (opcao in opcoes):
                return opcao

        elif (interaveis["saldo"] == 0):
            menu2 = Menu()[:18]+Menu()[32:]
            opcao = input(menu2)
            if (opcao in opcoes):
                return opcao
        else:
            print("Isso seria impresso se fosse possivel ter saldo negativo!!")

def Sacar(*,saldo,limite,numero_saques):
    while True:
        valor = float(input("Informe o valor do saque: "))
        
        if (numero_saques >= interaveis["LIMITE_SAQUES"]):
            print("Número máximo de saques alcançado!")
            return
        elif ((valor > saldo) and (valor<=limite)):
            print("Saldo Insuficiente!")
            escolha = input(f"Digite S caso queira sacar R$ {saldo:.2f}: ")
            if escolha.lower() == "s":
                valor = saldo
                break
            print(f"O Valor máximo para Saque é de R$ {saldo:.2f}.")
        elif (valor > limite):
            print("O valor excede o limite da operação!")
            escolha = input(f"Digite S caso queira sacar R$ {limite:.2f}: ")
            if escolha.lower() == "s":
                valor = saldo
                break
            print(f"O Valor máximo para Saque é de R$ {limite:.2f}.")
        else:
            break

    interaveis["saldo"] -= valor
    interaveis["extrato"] += f"Saque:    R$ "+f"{valor:.2f}".rjust(10)+"\n"
    interaveis["numero_saques"] += 1

def Depositar():

    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        interaveis["saldo"] += valor
        interaveis["extrato"] += "Depósito: R$ "+f"{valor:.2f}".rjust(10)+"\n"

    else:
        print("O valor informado é inválido.")

def Extrato(saldo,/,*,extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================\n")

def main():
    ValidacaoDoCliente()
    opcoes = ["d","s","e","n","q"]

    while True:
        print(f"\nConta: {dadosConta[0]}")
        opcao = TriagemDeOperacoes(opcoes)
        if ((opcao.lower() == "s") or (opcao.lower() == "sacar")):
            Sacar(saldo=interaveis["saldo"],limite=interaveis["limite"],numero_saques=interaveis["numero_saques"])

        elif ((opcao.lower() == "d") or (opcao.lower() == "depositar")):
            Depositar()

        elif ((opcao.lower() == "e") or (opcao.lower() == "extrato")):
            Extrato(interaveis["saldo"],extrato=interaveis["extrato"])
        
        elif ((opcao.lower() == "n") or (opcao.lower() in ["nova conta","nova","conta"])):
            contas[dadosCliente[0]][dadosConta[0]]["funcoesConta"] = interaveis
            CriarConta(dadosCliente[0])
            EscolherConta(dadosCliente[0])

        elif ((opcao.lower() == "q") or (opcao.lower() == "sair")):
            contas[dadosCliente[0]][dadosConta[0]]["funcoesConta"] = interaveis

            for iCliente in contas:
                print(f"Cliente {clientes[iCliente][0]} CPF: {iCliente}\n")
                for iConta in contas[iCliente]:
                    print(f"Conta: {iConta} Agência: {contas[iCliente][iConta]['agencia']}")
                    Extrato(contas[iCliente][iConta]["funcoesConta"]["saldo"],extrato=contas[iCliente][iConta]["funcoesConta"]["extrato"])
            break

        else:
            print("Operação inválida, por favor escolha uma operação entre as opções.")

main()
