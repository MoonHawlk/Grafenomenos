from src.func import *
import time

inScreen = True

def main():

    direcionado = input("O grafo é direcionado? (s/n): ") == 's'
    valorado = input("O grafo é valorado? (s/n): ") == 's'

    G = criar_grafo(direcionado)

    while inScreen:
        limpar_terminal()
        exibir_menu()
        
        opcao = input("Escolha uma opção: ")
        
        try:
            if opcao == '1':
                adicionar_nos(G)
            elif opcao == '2':
                adicionar_arestas(G, valorado)
            elif opcao == '3':
                visualizar_grafo(G, valorado)
            elif opcao == '4':
                ordem_e_tamanho_do_grafo(G)
                time.sleep(2)
            elif opcao == '5':
                listar_vertices_adjacentes(G)
                time.sleep(2)
            elif opcao == '6':
                obter_grau_do_vertice(G, direcionado)
                time.sleep(2)
            elif opcao == '7':
                verificar_adjacencia_entre_vertices(G)
                time.sleep(2)
            elif opcao == '8':
                encontrar_caminho_mais_curto(G, valorado)
                time.sleep(2)
            elif opcao == '0':
                exit()
            else:
                print(f"Valor de entrada {opcao} incorreto, favor digite uma opção válida.")
                time.sleep(2)
                
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")
            time.sleep(2)

if __name__ == "__main__":
    main()