class TV:
    def __init__(self, nome, marca, polegadas):
        self.power = False
        self.canal = 1
        self.volume = 0
        self._nome = nome
        self._marca = marca
        self._polegadas = polegadas

    @property
    def nome_tv(self):
        return self._nome.strip().split().title()
    
    @property
    def marca_tv(self):
        return self._marca.strip().split().title()

    @property
    def polegadas_tv(self):
        return (f'{self._polegadas}' + '"')


class ControleTV(TV):
    def __init__(self):
        super().__init__(self)
        
    def liga_tv(self):
        self.power = True
        print(f'\n' + '* '*5  + " TV ligada " + '* '*5)
        print(f'Canal: {self.canal}\nVolume: {self.volume}')
        print('* ' * 16 + f'\n')

    def aumenta_volume(self, volume):
        if self.power:
            self.volume += volume
            print(f'Aumentando volume...')
            self.seguranca_volume()
            return self.mostra_volume()
        else:
            pass
    
    def diminui_volume(self, volume):
        if self.power:
            self.volume -= volume
            print(f'Diminuindo volume...')
            return self.mostra_volume()
        else:
            pass

    def aumenta_canal(self, canal):
        if self.power:    
            self.canal += canal
            print('Trocando canal para: ')
            self.mostra_canal()
            return self.canal
        else:
            pass
    
    def diminui_canal(self, canal):
        if self.power:    
            self.canal -= canal
            print('Trocando canal para: ')
            self.mostra_canal()
            return self.canal
        else:
            pass

    def mostra_volume(self):
        self.volume = self.valida_volume()
        print(f'Volume: {self.volume}\n')

    def mostra_canal(self):
        self.canal = self.valida_canal()
        print(f'Canal {self.canal}\n')

    def valida_volume(self):
        if self.volume >= 100:
            self.volume = 100
            return self.volume

        elif self.volume == 0:
            return self.volume

        elif self.volume < 0:
            self.volume = 0
        
        else:
            return self.volume

    def valida_canal(self):
        if self.canal > 36:
            return (self.canal - 36)
        else:
            return self.canal


    def seguranca_volume(self):
        if self.volume >= 70 and self.volume < 100:
            print(f'O volume {self.volume} está alto demais! Isso pode afetar sua audição.')
        elif self.volume > 99:
            print(f'Volume máximo! É recomendável diminuir o volume da sua TV.')

    def desliga_tv(self):
        self.power = False
        print('* '* 5 + 'TV desligada' + '* '* 5)
        if not self.power:
            pass
