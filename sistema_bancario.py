print("Sistema bancario em python")

saldo = 100

while True:

    print("\n1 - Ver saldo ")
    print("2 - Depositar ")
    print("3 - Sacar ")
    print("4 - Sair ")

    opcao = input("Qual opção deseja escolher? ")

    if opcao == "1":
        print("Esse é o seu saldo: ", saldo)

    elif opcao == "2":
        valor = float(input("Qual o valor do deposito: "))
        saldo = saldo + valor 
        print("O seu novo saldo é de :", saldo)

    elif opcao == "3":
        valor = float(input("Qual o valor do saque: "))

        if valor <= saldo:
            saldo = saldo - valor 
            print("Saque realizado")
            print("Seu saldo restante é de :", saldo)

        else :
            print("Saldo insuficiente")

    elif opcao == "4":
        print("Sistema encerrado")
        break

    else:
        print("Opção invalida")





       



 

