from abc import ABC, abstractmethod

class Personagem(ABC):

    @abstractmethod
    def atacar(self):
        pass

    @abstractmethod
    def defender(self):
        pass

class Guerreiro(Personagem):
    def atacar(self):
        return "Guerreiro atacou com espada!"

    def defender(self):
        return "Guerreiro defendeu com escudo!"

class Mago(Personagem):
    def atacar(self):
        return "Mago lançou uma magia!"

    def defender(self):
        return "Mago criou um escudo mágico!"

# testes
g = Guerreiro()
m = Mago()

print(g.atacar())
print(g.defender())
print(m.atacar())
print(m.defender())
