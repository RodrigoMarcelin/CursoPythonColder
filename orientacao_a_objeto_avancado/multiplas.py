
class Animal:
    @property
    def capacidades(self):
        return('dormir', 'comer', 'beber')


class Homem(Animal):
    @property
    def capacidades(self):
        return super().capacidades + ('amar', 'falar', 'estudadar')

class Aranha(Animal):
    @property
    def capacidades(self):
        return super().capacidades + ('fazer teia', 'andar pelas paredes')


class SpiderMan(Homem, Aranha):
    @property
    def capacidades(self):
        return super().capacidades + ('bater em bandidos', 'atirar teias entre prédios')

if __name__ == '__main__':
    john = Homem()
    print(f'John: {john.capacidades}')

    aranha = Aranha()
    print(f'aranha: {aranha.capacidades}')

    peter = SpiderMan()
    print(f'Peter: {peter.capacidades}')