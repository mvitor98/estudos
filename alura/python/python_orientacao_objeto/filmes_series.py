class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes}'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano) #pega todos os atributos construidos da classe mãe 
        self.duracao = duracao
    
    def __str__(self):
        return f'\n{self._nome} - {self.ano} - {self.duracao} min - {self._likes}'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano) 
        self.temporadas = temporadas 

    def __str__(self):
        return f'\n{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes}'


#  aplicando a heranca de uma fnção built in.
# ao herdar uma função built in, podemos acabar causando bugs no código, já que não conhecemos todos os métodos dessa classe.
# class Playlist(list):
#     def __init__(self, nome, programa):
#         self.nome = nome
#         super().__init__(programa)

#     def tamanho(self):
#         return len(self.programa)

class Playlist():
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    # Duck typing
    # para fazer o objeto se comportar como iterável (apenas características de lista. Não pode ser mensurado apenas com esse super metodo)
    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    # Duck typing
    # para fazer o objeto poder ser mensurado
    def __len__(self):
        return len(self._programas)


vingadores = Filme('vingadores - guerra infinita', 2017, 160)
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()

tmep = Filme('todo mundo em panico', 1999, 100)
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()

demolidor = Serie('demolidor', 2016, 2)
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()

atlanta = Serie('Atlanta', 2018, 2)
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()

filmes_e_series = [vingadores, atlanta, tmep, demolidor]
minha_playlist = Playlist('minha playlist', filmes_e_series)


# aplicando a herança da classe LIST, a playlist vai se comportar como uma lista e não é necessário declarar o objeto ao iterar
# também é possível aplicar os métodos da classe herdada

# for programa in playlist_fim_de_semana.programa:

# polimorfismo: quando há características específicas de uma classe e é necessário mesclá-las com as características comuns das outras classes
# Para acabar com as soluções abaixo e tornar o código mais legível, adicionou-se o método imprime(self) nas classes mãe e filhas.
    # detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporadas
    # print(f'{programa.nome} - {detalhes} - {programa.likes}')

# também há um metodo especial para imprimir os atributos do objeto, chamado __str__

# for programa in playlist_fim_de_semana:
#     print(programa)
#     print(f'o porgrama "{programa.nome}" tá na playlist? {programa in playlist_fim_de_semana}')

print(f'Tamanho da playlist: {len(minha_playlist.listagem)}')

for programa in minha_playlist:
    print(programa)

