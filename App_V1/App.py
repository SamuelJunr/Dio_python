from Conta import ContaBancaria

def menu():
    print("\n=============== MENU ===============")
    print("[d] Depositar")
    print("[s] Sacar")
    print("[e] Extrato")
    print("[q] Sair")
    return input("Escolha uma opção: ").lower()


def main():
    conta = ContaBancaria()

    while True:
        escolha = menu()

        if escolha == "d":
            valor_deposito = float(input("Digite o valor a ser depositado em Conta: "))
            conta.depositar(valor_deposito)

        elif escolha == "s":
            valor_saque = float(input("Digite o valor a ser sacado da Conta: "))
            conta.sacar(valor_saque)

        elif escolha == "e":
            conta.exibir_extrato()

        elif escolha == "q":
            print("Sessão encerrada. Obrigado!")
            break

        else:
            print("Opção inválida. Tente novamente com as opcoes do MENU.")


if __name__ == "__main__":
    main()