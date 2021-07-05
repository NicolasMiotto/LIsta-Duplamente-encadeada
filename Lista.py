from No import No

class Lista:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self.tamanho = 0

    def __len__(self):
        return self.tamanho

    def add_inicio(self, valor):
        if self.primeiro:
            aux = self.primeiro
            ant = None
            while (aux.proximo):
                ant = aux
                aux = aux.proximo
            aux.proximo = No(valor)
            aux.proximo.ant = aux
            aux.ant = ant
            if self.ultimo:
                self.ultimo = aux.proximo
        else:
            self.primeiro = No(valor)
            self.ultimo = No(valor)
        self.tamanho += 1

    def imprimir(self):
        if self.primeiro == None:
            print("Lista vazia!")

        aux = self.primeiro
        while (aux):
            print(aux.valor)
            aux = aux.proximo
        print("---->: " + str(self.tamanho))
        print("\n -----------------\n")

    def imprimir_invert(self):
        aux = self.ultimo
        print("Lista inversa: " + str(self.tamanho))
        while (aux):
            print(aux.valor)
            aux = aux.ant
        print("---->: " + str(self.tamanho))
        print("\n -----------------\n")