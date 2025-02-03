class Veiculos():
    def __init__(self):
        self.cor = None
        self.modelo = None
    
    def definir_modelo(self, modelo):
        self.modelo = modelo
        return self
    
    def definir_cor(self, cor):
        self.cor = cor
        return self
    
    def obter_informacoes(self):
        print(f'Veiculo: {self.__class__.__name__}, Modelo: {self.modelo}, Cor: {self.cor}')

class Carro(Veiculos):
    def __init__(self):
        super().__init__()
        self.motor_ligado = False
    
    def ligar_motor(self):
        self.motor_ligado = True
        print(f"O carro {self.modelo} está com motor ligado")
        return self

class Bicicleta(Veiculos):
    def __init__(self):
        super().__init__()
        self.tem_cestinha = False
    
    def adicionar_cestinha(self):
        self.tem_cestinha = True
        print(f"A bicicleta {self.modelo} agora tem uma cestinha")
        return self
    
carro1 = Carro().definir_modelo("Ferrari").definir_cor("Vermelho").ligar_motor()
carro1.obter_informacoes()

bike1 = Bicicleta().definir_modelo("Caloi").definir_cor("Azul").adicionar_cestinha()
bike1.obter_informacoes()




    
    

        
