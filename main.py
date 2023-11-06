from src.func import *

inScreen = True

def main():
    while (inScreen):
        exibir_menu()
        entrada = int(input(">> "))
        if entrada == 1:
            G = criar_grafo_nao_direcionado()
            adicionar_nos(G)
            adicionar_arestas(G)
            visualizar_grafo(G)
        else:
            exit()
        
if __name__ == "__main__":
    main()