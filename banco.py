from re import L


menu ='''
    [d] depositar
    [s] sacar
    [e] extrato
    [q] sair

->'''
saldo = 0
numero_saque = 0
LIMITE_DE_SAQUE = 3
LIMITE_MÁXIMO = 500
extrato = ""

while True:

    opção = input(menu)

    if opção == "d":
        deposito = float(input("Qual valor você irá depositar?\n-> "))
        if deposito > 0:
            saldo = saldo + deposito
            extrato = extrato + f"Operação deposito de R$ {deposito:.2f}\n"
        else:
            print("deposito inválido")
    elif opção == "s":
        print("Saque")
        saque = float(input("informe seu saque\n-> "))
        if saque >= 0 and saque <= LIMITE_MÁXIMO:
            if (LIMITE_DE_SAQUE - numero_saque) > 0:
                if saque <= saldo:
                    saldo = saldo - saque
                    extrato = extrato + f"Operação saque de R$ {saque:.2f}\n"
                    numero_saque = numero_saque + 1
                else:
                    print("saldo insuficiente")
            else:
                print("limite de saque diario excedido")
        else:
            print("valor invalido")
    elif opção == "e":
        print(f"Operação extrato\n{extrato}\no valor em conta atual é de :\nR$ {saldo:.2f}")

    elif opção == "q":
        print("saindo")
        break
    else:
        print("erro, digite de novo")
