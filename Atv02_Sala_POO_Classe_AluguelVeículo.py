
class veiculo:
    def __init__(self, modelo, cor, velocidade_maxima):
        self.modelo = modelo
        self.cor = cor
        self.velocidade_maxima = velocidade_maxima
        self.disponivel = True

    def alugar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"O veículo {self.modelo} foi alugado.")
        else:
            print(f"O veículo {self.modelo} não está disponível para aluguel.")

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print(f"O veículo {self.modelo} foi devolvido.")
        else:
            print(f"O veículo {self.modelo} já está disponível.")

veiculo1 = veiculo("Fusca", "Azul", 120)  
veiculo1.alugar()
veiculo1.alugar()
veiculo1.devolver()
veiculo1.alugar()

