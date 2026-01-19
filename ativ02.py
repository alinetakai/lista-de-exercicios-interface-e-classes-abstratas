from abc import ABC, abstractmethod

class Pagamento(ABC):

    @abstractmethod
    def pagar(self, valor):
        pass

class PagamentoPix(Pagamento):
    def pagar(self, valor):
        return f"Pagamento de R$ {valor} realizado via PIX"

class PagamentoCartao(Pagamento):
    def pagar(self, valor):
        return f"Pagamento de R$ {valor} realizado via Cartão"

# testes
pag1 = PagamentoPix()
print(pag1.pagar(100))

pag2 = PagamentoCartao()
print(pag2.pagar(250))
