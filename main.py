from src.func import *
from src.menu_func import *
import time

inScreen = True

def main():
    direcionado = input("O grafo é direcionado? (s/n): ") == 's'
    valorado = input("O grafo é valorado? (s/n): ") == 's'

    G = criar_grafo(direcionado)

    opcoes = {
        '1': adicionar_nos_wrapper,
        '2': adicionar_arestas_wrapper,
        '3': visualizar_grafo_wrapper,
        '4': ordem_e_tamanho_do_grafo_wrapper,
        '5': listar_vertices_adjacentes_wrapper,
        '6': obter_grau_do_vertice_wrapper,
        '7': verificar_adjacencia_entre_vertices_wrapper,
        '8': encontrar_caminho_mais_curto_wrapper,
        '9': calcular_excentricidade_do_vertice,
        '10': apagar_grafo_wrapper,
        'L': entrada_lote_wrapper,
        '0': exit
    }

    while inScreen:
       # limpar_terminal()
        exibir_menu()
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '0':
            sair()
        
        elif opcao == 'L':
            entrada_lote(G, valorado, direcionado)

        elif opcao == '9':
            calcular_excentricidade_do_vertice(G, valorado)

        elif opcao in opcoes:
            if opcao == '2':
                adicionar_arestas_wrapper(G, valorado, direcionado)
            else:
                opcoes[opcao](G, valorado if opcao in ('3', '8') else (direcionado if opcao in ('6', '2') else None))
        else:
            print(f"Valor de entrada {opcao} incorreto, favor digitar uma opção válida.")
            time.sleep(2)

if __name__ == "__main__":
    main()