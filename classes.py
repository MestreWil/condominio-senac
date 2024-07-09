class Torre:

      def __init__(self, nome, endereco):
            self.id = 0
            self.nome = nome
            self.endereco = endereco
      def __str__(self): 
            return f"Nome: {self.nome}\nEndereco: {self.endereco}\n"
      
      def cadastrar(self):
            pass
      

      def imprimir(self):
            return str(self)


class Apartamento:
      def __init__(self, numero):
            self.id = 0
            self.numero = numero
            self.torre = None
            self.vaga = None

      def cadastrar(self, torre):    
            self.torre = torre
            print("Torre cadastrada.")
            return 
      def __str__(self):
            vaga = ""
            if self.vaga == None:
                  vaga = "Esta apartamento está na fila de espera"
            else:
                  vaga = f"{self.vaga}"
            return f"Numero: {self.numero}\nTorre: {str(self.torre)}\nVaga: {vaga}\n"

      def imprimir(self):
            return str(self)


class Fila:
      class No:
            def __init__(self, valor, proximo=None):
                  self.valor = valor
                  self.proximo = None

      def __init__(self):
            self.primeiro = None
            self.ultimo = None
            self._tamanho = 0

      def __iter__(self):
            atual = self.primeiro
            while atual is not None:
                  yield atual.valor
                  atual = atual.proximo
      def __str__(self):
        return  "\n".join([str(valor) for valor in self]) + "\n"
  
      def adicionar(self, elem):
            nodo = self.No(elem)
            if self.ultimo is None:
                  self.ultimo = nodo
            else:
                  self.ultimo.proximo = nodo
                  self.ultimo = nodo
            if self.primeiro is None:
                  self.primeiro = nodo

            self._tamanho += 1

      def retirar(self):

            if len(self) is not None:
                  elem = self.primeiro.valor
                  self.primeiro = self.primeiro.proximo
                  self._tamanho -= 1
                  return elem
            raise IndexError("A FILA está vazia.")

      def __len__(self):
            return self._tamanho


class Lista:
      class No:
            def __init__(self, valor, proximo=None):
                  self.valor = valor
                  self.proximo = None

            def __str__(self):
                  return str(self.valor)

      def __init__(self):
            self.__cabeca = None
            self.__cauda = None
            self.__quantidade = 0

      def __getitem__(self, posicao):

            if isinstance(posicao, slice):
                  passo = posicao.step if posicao.step is not None else 1

                  if passo == 0:
                        raise ValueError("Passo não pode ser zero.")
                  if passo > 0:
                        inicio = posicao.start if posicao.start is not None else 0
                        fim = posicao.stop if posicao.stop is not None else len(self)
                  else:
                        inicio = posicao.start if posicao.start is not None else len(self) - 1
                        fim = posicao.stop if psoicao.stop is not None else -1

            if posicao < 0:
                  posicao = len(self) + posicao

            if posicao < 0 or posicao >= self.__quantidade:
                  raise IndexError("Posição invélida")

            atual = self.__cabeca
            for i in range(posicao):
                  atual = atual.proximo

            return atual.valor

      def __iter__(self):
            atual = self.__cabeca
            while atual is not None:
                  yield atual.valor
                  atual = atual.proximo
                  
      def __delitem__(self, posicao):
            if posicao < 0:
                  posicao = len(posicao) + posicao
            if posicao < 0 or posicao >= self.__quantidade:
                  raise IndexError("Posicao invalida")
            self.__quantidade -= 1
            
            if posicao == 0:
                  self.__cabeca = self.__cabeca.proximo
                  if self.__cabeca is None:
                        self.__cauda = None
                  return
            i = 0
            atual = self.__cabeca
            while atual.proximo is not None and i < posicao -1:
                  atual = atual.proximo
                  i += 1
                  
            if atual.proximo == self.__cauda:
                  self.__cauda = atual
                  
            atual.proximo = atual.proximo.proximo
            
            
            
      def __str__(self):
            return  "\n".join([str(valor) for valor in self]) + "\n"

      def inserir_no_fim(self, valor):
            novo = self.No(valor)
            self.__quantidade += 1
            
            if self.__cabeca is None:
                  self.__cabeca = novo
                  self.__cauda = novo
                  return
            
            self.__cauda.proximo = novo
            self.__cauda = novo
            

      def __len__(self):
            return self.__quantidade

      def inserir(self, posicao, valor):
            novo = self.No(valor)
            self.__quantidade += 1
        # Quando a lista é vazia
            if self.__cabeca is None:
                  self.__cabeca = novo
                  self.__cauda = novo
                  return

        # Inserir na cabeca (primeira posicao)
            if posicao <= 0:
                  novo.proximo = self.__cabeca
                  self.__cabeca = novo
                  return

            i = 0
            atual = self.__cabeca
            while atual.proximo is not None and i < posicao - 1:
                  atual = atual.proximo
                  i += 1

            if atual.proximo is None:
                  self.__cauda = novo

            novo.proximo = atual.proximo
            atual.proximo = novo


