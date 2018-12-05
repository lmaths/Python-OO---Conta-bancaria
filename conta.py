class Conta:

    def __init__(self, cliente, saldo):

        self.cliente = cliente
        self.saldo = saldo


    def depositar (self, quant):
        if quant > 0:
            self.saldo += quant
            print("Foi depositado:", quant)
            print("Saldo total", self.saldo)
        else:
            print("Erro ao depositar, precisa ser maior que 0")

    def sacar(self, quant):
        if self.saldo - quant < 0:
            print("Saldo insuficiente")
        else:
            self.saldo -= quant
            print("Foi sacado:", quant)
            print("Seu saldo agora é de", self.saldo)


    def consulta_saldo(self):
        return self.saldo