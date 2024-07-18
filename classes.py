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
      def __init__(self, numero, torre):
            self.id = 0
            self.numero = numero
            self.torre = torre
            self.vaga = None
            self.proximo = None

      def cadastrar(self):    
            pass
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

      def __init__(self):
            self.primeiro = None
            self.___quantidade = 0

      def __iter__(self):
            atual = self.primeiro
            while atual is not None:
                  yield atual
                  atual = atual.proximo

      def __str__(self):
        return  "\n".join([str(valor) for valor in self]) + "\n"
  
      def adicionar(self, apart):
            if self.primeiro is None:
                  self.primeiro = apart
            else:
                  atual = self.primeiro
                  while atual.primeiro:
                        atual = atual.proximo
                  atual.proximo = apart
                  
            self.___quantidade += 1

      def retirar(self):

            if len(self) is not None:
                  elem = self.primeiro
                  self.primeiro = self.primeiro.proximo
                  self.___quantidade -= 1
                  elem.proximo = None
                  return elem
            raise IndexError("A FILA está vazia.")

      def __len__(self):
            return self.___quantidade


class Lista:

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
                        fim = posicao.stop if posicao.stop is not None else -1

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
                  yield atual
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

      def inserir(self, valor):
            if self.__cabeca: 
                  cabeca = self.__cabeca
                  while cabeca.proximo:
                        cabeca = cabeca.proximo
                  cabeca.proximo = valor
            else:
                  self.__cabeca = valor
            self.__quantidade += 1
      
      def retirar(self, vaga):
        if self.__cabeca is None:
            raise IndexError("A lista está vazia.")
        
        if self.__cabeca.vaga == vaga: #verifica se o objeto no __cabeca corresponde ao parametro
            item_removido = self.__cabeca
            self.__cabeca = item_removido.proximo
            item_removido.proximo = None
            self.__quantidade -= 1
            return item_removido
        
        anterior = self.__cabeca
        atual = self.__cabeca.proximo
        while atual: #loop para percorrer a lista enquanto houver um proximo
            if atual.vaga == vaga:
                anterior.proximo = atual.proximo 
                atual.proximo = None
                self.__quantidade -= 1
                return atual
            anterior = atual
            atual = atual.proximo
        
        raise ValueError("Apartamento com a vaga especificada não encontrado.")

