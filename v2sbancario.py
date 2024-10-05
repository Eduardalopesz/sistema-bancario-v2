menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Cadastrar Usuário
[5] Cadastrar Conta Corrente
[6] Sair
=> """

usuarios = []
contas = []
numero_conta = 1
limite = 500
LIMITE_SAQUES = 3

def cadastrar_usuario(cpf):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("Usuário já cadastrado!")
            return False
    nome = input("Nome: ")
    data_nascimento = input("Data de nascimento (dd/mm/yyyy): ")
    endereco = input("Endereço (logradouro, nro - bairro - cidade/estado): ")
    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})
    print("Usuário cadastrado com sucesso!")
    return True

def criar_conta(usuario_cpf):
    global numero_conta
    for usuario in usuarios:
        if usuario['cpf'] == usuario_cpf:
            for conta in contas:
                if conta['usuario']['cpf'] == usuario_cpf:
                    print(f"Conta já existente! Agência: {conta['agencia']}, Conta: {conta['numero_conta']}")
                    return
            contas.append({'agencia': "0001", 'numero_conta': numero_conta, 'usuario': usuario})
            numero_conta += 1
            print("Conta corrente cadastrada com sucesso!")
            return
    print("Usuário não encontrado!")

def depositar(saldo, valor, extrato):
    saldo += valor
    extrato += f"Depósito: R$ {valor:.2f}\n"
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques):
    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif numero_saques >= LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saques excedido.")
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Operação realizada com sucesso!")
    return saldo, extrato, numero_saques

def extrato(saldo, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f}")
    print("==========================================")

saldo = 0
extrato = ""
numero_saques = 0

while True:
    opcao = input("Digite o número da operação desejada: " + menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo, extrato = depositar(saldo, valor, extrato)
            print("Operação realizada com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato, numero_saques = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques)

    elif opcao == "3":
        extrato(saldo, extrato=extrato)

    elif opcao == "4":
        cpf = input("Informe o CPF do usuário: ")
        cadastrar_usuario(cpf)

    elif opcao == "5":
        cpf = input("Informe o CPF do usuário: ")
        criar_conta(cpf)

    elif opcao == "6":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
