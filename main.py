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
      escolha = input(menu + "\nDigite aqui: ")
      while True:
            match escolha:
                  case 0:
                        print("Até mais tarde!")
                        break
                  case 1:
                        pass
                  case 2:
                        pass
                  case 3:
                        pass
                  case 4:
                        pass
                  case 5:
                        pass
                  case 6:
                        pass
if __name__ == "__main__":
  pass