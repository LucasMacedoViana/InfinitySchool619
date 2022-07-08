class BichinhoVirtual:
    def __init__(self):
        self.__nome = ''
        self.__fome = 0
        self.__saude = 0
        self.__idade = 0

    def setNome(self, nome):
        self.__nome = nome
    def getNome(self):
        return self.__nome
    def setFome(self, fome):
        self.__fome = fome
    def getfome(self):
        return self.__fome
    def setSaude(self,saude):
        self.__saude = saude
    def getSaude(self):
        return self.__saude
    def setIdade(self,idade):
        self.__idade = idade
    def getIdade(self):
        return self.__idade

    def humor(self, fome, saude):
        if (self.__fome + self.__saude)/2 >=80:
            return print(f'o {self.__nome} está FELIZ')
        elif(self.__fome + self.__saude)/2 < 80 and (self.__fome + self.__saude)/2 <= 50:
            return print(f'o {self.__nome} está BEM')
        elif (self.__fome + self.__saude) / 2 < 50 and (self.__fome + self.__saude) / 2 <= 30:
            return print(f'o {self.__nome} está MAL')
        elif (self.__fome + self.__saude) / 2 < 30:
            return print(f'o {self.__nome} está morrendo')

bichinho1 = BichinhoVirtual()
bichinho1.setNome(input('Bigite o nome do seu Tamagoshi: '))
bichinho1.setIdade(int(input(f'Digite a idade do {bichinho1.getNome()}: ')))
bichinho1.setFome(int(input(f'De 0 a 100 digite a Fome do {bichinho1.getNome()}: ')))
bichinho1.setSaude(int(input(f'De 0 a 100 digite a saáude do {bichinho1.getNome()}: ')))
bichinho1.humor(bichinho1.getfome, bichinho1.getSaude)
