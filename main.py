from src.func import *
import time

inScreen = True

def main():
    while inScreen:
        limpar_terminal()
        exibir_menu()
        entrada = input(">> ")
        
        try:
            entrada = int(entrada)
            if entrada == 1:
                G = criar_grafo_nao_direcionado()
                adicionar_nos(G)
                adicionar_arestas(G)
                visualizar_grafo(G)
            elif entrada == 0:
                exit()
            else:
                print(f"Valor de entrada {entrada} incorreto, favor digite uma opção válida.")
                time.sleep(2)
                
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")
            time.sleep(2)

if __name__ == "__main__":
    main()
