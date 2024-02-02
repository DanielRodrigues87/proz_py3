def calculadora():
    while True:
        # Mostra as opções
        print("Escolha a operação:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        # Solicita a escolha do usuário
        escolha = int(input("Digite o número da operação desejada: "))

        # Verifica a escolha
        if escolha == 0:
            print("Saindo da calculadora.")
            break  # Sai do loop se a escolha for '0'
        elif escolha >= 1 and escolha <= 4:
            # Pede os dois valores
            num1 = float(input("Digite o primeiro valor: "))
            num2 = float(input("Digite o segundo valor: "))

            # Executa a operação
            if escolha == 1:
                resultado = num1 + num2
                print("Resultado da Soma:", resultado)
            elif escolha == 2:
                resultado = num1 - num2
                print("Resultado da Subtração:", resultado)
            elif escolha == 3:
                resultado = num1 * num2
                print("Resultado da Multiplicação:", resultado)
            elif escolha == 4:
                if num2 != 0:
                    resultado = num1 / num2
                    print("Resultado da Divisão:", resultado)
                else:
                    print("Erro: Divisão por zero.")
        else:
            print("Essa opção não existe. Por favor, escolha novamente.")

# Chama a função da calculadora
calculadora()
