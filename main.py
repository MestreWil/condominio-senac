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
    6- Remover torre cadastrada
    """
def menu_principal():
      while True:
            escolha = int(input(menu + "\nDigite aqui: "))
            if escolha == 0:
                  print("Até mais tarde!")
                  break
            elif escolha == 1:
                  if len(lista_de_apartamentos) == 0:
                        print("Desculpe, não podemos cadastrar essa Torre pois não tem nenhum apartamento cadastrado!\n")
                        input("Aperte qualquer tecla para continuar: ")
                  else:
                        nome = input("Digite o nome da Torre: ")
                        endereco = input("Digite o endereco: ")
                        torre = Torre(nome, endereco)
                        print(str(lista_de_apartamentos))
                        num = int(input("Digite o apartamento que você deseja essa Torre: "))
                        apto = lista_de_apartamentos[num]
                        apto.cadastrar(torre)
                  
            elif escolha == 2:
                  num = input("Digite o número do apartamento: ")
                  apto = Apartamento(num)
                  if len(lista_de_apartamentos) <= 10:
                        lista_de_apartamentos.inserir(0, apto)
                  else:
                        fila_de_espera.adicionar(apto)
            elif escolha == 3:
                  print(str(lista_de_apartamentos))
                  input("Aperte ENTER para continuar")                   
            elif escolha == 4:
                  pass
            elif escolha == 5:
                  pass
            elif escolha == 6:
                  pass
if __name__ == "__main__":
      menu_principal()