while True:
    print("Menu de opções")
    print("1 - soma")
    print("2 - subtração")
    print("3 - divisão")
    print("4 - multiplicação")
    operacao = input("Digite uma opção: ")

    n1 = float(input("Digite o numero 1: "))
    n2 = float(input("Digite o numero 2: "))

    if operacao == "1":
        resultado = n1 + n2
        print(resultado)
    elif operacao == "2":
        resultado = n2 - n1
        print(resultado)
    elif operacao == "3":
        resultado = n1 / n2
        print(resultado)
    elif operacao == "4":
        resultado = n1 * n2
        print(resultado)
    continuar = input("quer continuar? s = sim / n = não")
    if continuar == "n":
        break