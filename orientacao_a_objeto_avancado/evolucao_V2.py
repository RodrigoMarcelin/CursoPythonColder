

class Humano:
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome
    
    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'
        return self


    @staticmethod
    def especies():
        adjetivos = ('Habilis', 'Erectus', 'Neandethalensis', 'Sapiens')
        return ('Australopiteco',) + tuple(f'Homo {adj}' for adj in adjetivos)

    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1]

class Neanderthal(Humano):
    especie = Humano.especies()[-2]


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]


if __name__ == '__main__':
    jose = HomoSapiens('José')
    grokn = Neanderthal('Grokn')

    
    print(f'jose.especie: {jose.especie}')
    print(f'grokn.especie: {grokn.especie}')
    print(f'Neandethal evoluido? {Neanderthal.is_evoluido()}')
        