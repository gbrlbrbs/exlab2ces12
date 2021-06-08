from abc import ABC, abstractmethod

class Comando(ABC):
    @abstractmethod
    def execute(self):
        pass


class Conta:
    def __init__(self, saldo_inicial: float, id: str, extrato = []) -> None:
        self.saldo = saldo_inicial
        self.id = id
        self.extrato = extrato
    

class VerificarSaldo(Comando):
    def __init__(self, conta: Conta) -> None:
        super().__init__()
        self.conta = conta

    def execute(self):
        print("Seu saldo é R$", self.conta.saldo)


class TransferirDinheiro(Comando):
    
    def __init__(self, conta_saida: Conta, conta_destino: Conta, dinheiro) -> None:
        super().__init__()
        self.conta_saida = conta_saida
        self.conta_destino = conta_destino
        self.dinheiro = dinheiro

    def execute(self):
        print("Transferindo R$", self.dinheiro, "à conta", self.conta_destino.id)
        self.conta_saida.saldo = self.conta_saida.saldo - self.dinheiro
        self.conta_destino.saldo = self.conta_destino.saldo + self.dinheiro
        self.conta.extrato.append("TRANSFERÊNCIA: R$ " + str(self.dinheiro) + " - CONTA FAVORECIDA: " + self.conta_destino.id)
        print("Transferência concluída")
        

class VerificarExtrato(Comando):
    def __init__(self, conta: Conta) -> None:
        super().__init__()
        self.conta = conta

    def execute(self):
        print("EXTRATO")
        print("--------------------------------------")
        for movimentacao in self.conta.extrato:
            print(movimentacao)
        print("--------------------------------------")
        print("SALDO FINAL: R$", self.conta.saldo)


class Invoker:
    def __init__(self) -> None:
        self.comando = None

    def set_comando(self, comando: Comando):
        self.comando = comando
    
    def executar_comando(self):
        self.comando.execute