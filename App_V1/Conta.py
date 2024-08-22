from datetime import datetime

class ContaBancaria:
    def __init__(self):
        self.numero_conta = None
        self.saldo = 0
        self.historico = []
        self.saques_diarios = 0
        self.ultima_data_saque = None

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.registrar_transacao("Depósito", valor)
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if self.pode_realizar_saque():
            if 0 < valor <= self.saldo:
                self.saldo -= valor
                self.registrar_transacao("Saque", valor)
                self.saques_diarios += 1
                self.ultima_data_saque = datetime.now().strftime("%d-%m-%Y")
                print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
            else:
                print("Valor inválido para saque ou saldo insuficiente.")
        else:
            print("Limite diário de saques atingido. Tente novamente amanhã.")

    def pode_realizar_saque(self):
        hoje = datetime.now().strftime("%d-%m-%Y")
        return self.ultima_data_saque != hoje or self.saques_diarios < 3

    def registrar_transacao(self, tipo, valor):
        data_transacao = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.historico.append({"tipo": tipo, "valor": valor, "data": data_transacao})

    def exibir_extrato(self):
        print("\nExtrato Bancário:")
        for transacao in self.historico:
            print(f"{transacao['data']} - {transacao['tipo']}: R$ {transacao['valor']:.2f}")
        print(f"Saldo Atual: R$ {self.saldo:.2f}")


