import os

class FilaNormal:
    #type indice
    codigo:int = 0
    fila = []
    clientesAtendidos = []
    #type indice
    senhaAtual:str = ""

    # "-> None" é utilizado quando o método apenas manipula um atributo da classe
    def geraSenhaAtual(self) -> None:
        self.senhaAtual = f"NM.{self.codigo}"

    def reseteFila(self) -> None:
        if self.codigo >= 100:
            self.codigo = 0
        else:
            self.codigo += 1

    def atualizaFila(self) -> None:
        self.reseteFila()
        self.geraSenhaAtual()
        self.fila.append(self.senhaAtual)

    def chamaCliente(self, caixa:int) -> str:
        os.system('cls')
        clienteAtual = self.fila.pop(0)
        self.clientesAtendidos.append(clienteAtual)
        return f'Cliente atual: {clienteAtual}\nDirija-se ao caixa: {caixa}\n'