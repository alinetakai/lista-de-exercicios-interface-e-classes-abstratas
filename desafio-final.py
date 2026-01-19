from abc import ABC, abstractmethod

class Entrega(ABC):

    @abstractmethod
    def calcular_prazo(self):
        pass

    @abstractmethod
    def calcular_valor(self):
        pass

class EntregaMotoboy(Entrega):

    def calcular_prazo(self):
        return 2  # dias

    def calcular_valor(self):
        return 15.00

class EntregaDrone(Entrega):

    def calcular_prazo(self):
        return 1  # dia

    def calcular_valor(self):
        return 30.00

class EntregaCorreios(Entrega):

    def calcular_prazo(self):
        return 5  # dias

    def calcular_valor(self):
        return 20.00


# testes
def testar_entrega(entrega):
    print("Prazo:", entrega.calcular_prazo(), "dias")
    print("Valor: R$", entrega.calcular_valor())
    print("-" * 30)

motoboy = EntregaMotoboy()
drone = EntregaDrone()
correios = EntregaCorreios()

testar_entrega(motoboy)
testar_entrega(drone)
testar_entrega(correios)
