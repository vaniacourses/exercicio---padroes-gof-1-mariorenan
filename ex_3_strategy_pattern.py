from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def execute_start_strategy(self):
        pass
    
    @abstractmethod
    def execute_end_strategy(self):
        pass

class Nuclear(Strategy):
    def execute_start_strategy(self):
        print("Recuar tropas e propor cooperação econômica.")

    def execute_end_strategy(self):
        print("Desarmar o inimigo e dividir benefício.")

class Army(Strategy):
    def execute_start_strategy(self):
        print("Atacar o inimigo pelo norte e pedir ajuda ao vizinho.")
        
    def execute_end_strategy(self):
        print("Dividir benefícios e estabelecer um governo amigo.")

class Fragile(Strategy):
    def execute_start_strategy(self):
        print("Plantar evidências falsas e lançar bombas no inimigo.")
    
    def execute_end_strategy(self):
        print("Estabelecer um governo amigo e dividir custo de reconstrução.")
    
class War:
    def __init__(self, enemy_type):
        if enemy_type == "Nuclear":
            self.strategy = Nuclear()
        elif enemy_type == "Grande exército":
            self.strategy = Army()
        elif enemy_type == "Frágil":
            self.strategy = Fragile()
        else:
            raise ValueError("Força inimiga inválida")

    def startWar(self):
        print("Guerra declarada")
        self.strategy.execute_start_strategy()

    def endWar(self):
        print("Guerra concluída")
        self.strategy.execute_end_strategy()

def main():
    simulation = War("Nuclear")

    simulation.startWar()

    simulation.endWar()

if __name__ == "__main__":
    main()
