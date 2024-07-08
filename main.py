from classes import *
lista_de_apartamentos = Lista()
fila_de_espera = Fila()

menu = """
=========================================
  Sistema de Cadastro de Condomínio
=========================================
    0- Sair
    1- Cadastrar Torre
    2- Cadastrar Apartamento
    3- Visualizar apartamentos com vagas de garagem
    4- Visulaizar Fila de espera
    5- Remover apartamento cadastrado
    """
    
def cadastrar_torre():
      if len(lista_de_apartamentos) == 0:
            print("Desculpe, não podemos cadastrar essa Torre pois não tem nenhum apartamento cadastrado!\n")
            input("Aperte qualquer tecla para continuar: ")
      else:
            nome = input("Digite o nome da Torre: ")
            endereco = input("Digite o endereco: ")
            torre = Torre(nome, endereco)
            if len(lista_de_apartamentos) != 10:
                  print(str(lista_de_apartamentos))
                  num = int(input("Digite o apartamento que você deseja essa Torre: "))
                  apto = lista_de_apartamentos[num]
                  apto.cadastrar(torre)
            else:
                  print(str(fila_de_espera))
                  num = int(input("Digite o apartamento que você deseja essa Torre: "))
                  apto = fila_de_espera[num]
                  apto.cadastrar(torre)
def cadastrar_apto():
      num = input("Digite o número do apartamento: ")
      apto = Apartamento(num)
      if len(lista_de_apartamentos) <= 10:
            garagem = 0
            garagem += len(lista_de_apartamentos) + 1
            apto.vaga = garagem 
            lista_de_apartamentos.inserir_no_fim(apto)
      else:
            fila_de_espera.adicionar(apto)
            
def menu_principal():
      while True:
            escolha = int(input(menu + "\nDigite aqui: "))
            if escolha == 0:
                  print("Até mais tarde!")
                  break
            elif escolha == 1:
                  cadastrar_torre()      
                  
            elif escolha == 2:
                 cadastrar_apto() 
                 
            elif escolha == 3:
                  print(str(lista_de_apartamentos))
                  input("Aperte ENTER para continuar")                   
            elif escolha == 4:
                  print(str(fila_de_espera))
                  input("Aperte ENTER para continuar")
            elif escolha == 5:
                  escolha = int(input('\nDigite 1 se quiser remover da lista.\nDigite 2 se quiser remover da fila.\n'))
                  if escolha == 1:
                        print(str(lista_de_apartamentos))
                        num = int(input("Digite o indice que deseja remover: "))
                        del lista_de_apartamentos[num]
                  elif escolha == 2:
                        input('Essa função removera o elemento do topo da fila')
                        print(str(fila_de_espera))
                        fila_de_espera.retirar()
                                        
if __name__ == "__main__":
      menu_principal()