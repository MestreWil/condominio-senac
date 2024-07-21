from classes import *
lista_de_apartamentos = Lista()
fila_de_espera = Fila()

menu = """
=========================================
  Sistema de Cadastro de Condomínio
=========================================
    0- Sair
    1- Cadastrar Apartamento
    2- Visualizar apartamentos com vagas de garagem
    3- Visulaizar Fila de espera
    4- Desapropriar Vaga
    """
    
torre1 = Torre("Terra Nova", "Parternon, 1515")
torre2 = Torre("Atlandida", "Tristeza, 9087")
torre3 = Torre("Sans Serif", "Centro Historico, 1406")
torre4 =  Torre("Arial", "Moinhos, 1321")

def novo_apartamento():
    num = input("Digite o número do apartamento: ")
    print('\n')
    print(f"{str(torre1)}\n{str(torre2)}\n{str(torre3)}\n{str(torre4)}")
    torre = int(input("\nDigite o número da torre deste apartamento: "))
    
    if torre == 1:
        torre = torre1
    elif torre == 2:
        torre = torre2
    elif torre == 3:
        torre = torre3
    elif torre == 4:
        torre = torre4
    
    apto = Apartamento(num, torre)
    
    if len(lista_de_apartamentos) < 2:
            garagem = 0
            garagem += len(lista_de_apartamentos) + 1
            apto.vaga = garagem
            lista_de_apartamentos.inserir(apto)
    else:
            fila_de_espera.adicionar(apto)

def cadastrar_apto():
      num = input("Digite o número do apartamento: ")
      apto = Apartamento(num)
      if len(lista_de_apartamentos) < 2:
             
            lista_de_apartamentos.inserir_no_fim(apto)
      else:
            fila_de_espera.adicionar(apto)

def liberar_vaga():
    vaga = int(input("Digite o número da vaga a ser liberada: "))
    apto_removido = lista_de_apartamentos.retirar(vaga)
    print(f"Apartamento {apto_removido.numero} da {apto_removido.torre.nome} foi removido da vaga {vaga}.")

    if len(fila_de_espera) > 0:
        apto_fila = fila_de_espera.retirar()
        apto_fila.vaga = vaga
        lista_de_apartamentos.inserir(apto_fila)
        print(f"Apartamento {apto_fila.numero} da {apto_fila.torre.nome} foi movido para a vaga {vaga}.")
    apto_removido.vaga = None
    fila_de_espera.adicionar(apto_removido)
            
def menu_principal():
      while True:
            escolha = int(input(menu + "\nDigite aqui: "))
            if escolha == 0:
                  print("Até mais tarde!")
                  break
            elif escolha == 1:
                  novo_apartamento()    
                  
            elif escolha == 2:
                  print(str(lista_de_apartamentos))
                  input("Aperte ENTER para continuar")
                 
            elif escolha == 3:
                  print(str(fila_de_espera))
                  input("Aperte ENTER para continuar")                  
            elif escolha == 4:
                  liberar_vaga()
                  
                                        
if __name__ == "__main__":
      menu_principal()