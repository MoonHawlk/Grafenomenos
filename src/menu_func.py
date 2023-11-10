from src.func import *
import time

def adicionar_nos_wrapper(G, valorado = None, direcionado = None):
    adicionar_nos(G)

def adicionar_arestas_wrapper(G, valorado):
    adicionar_arestas(G, valorado)

def visualizar_grafo_wrapper(G, valorado):
    visualizar_grafo(G, valorado)

def ordem_e_tamanho_do_grafo_wrapper(G, valorado = None, direcionado = None):
    ordem_e_tamanho_do_grafo(G)
    time.sleep(2)

def listar_vertices_adjacentes_wrapper(G, valorado = None, direcionado = None):
    listar_vertices_adjacentes(G)
    time.sleep(2)

def obter_grau_do_vertice_wrapper(G, direcionado):
    obter_grau_do_vertice(G, direcionado)
    time.sleep(2)

def verificar_adjacencia_entre_vertices_wrapper(G, valorado = None, direcionado = None):
    verificar_adjacencia_entre_vertices(G)
    time.sleep(2)

def encontrar_caminho_mais_curto_wrapper(G, valorado):
    encontrar_caminho_mais_curto(G, valorado)
    time.sleep(2)

def sair():
    print("Encerrando o programa.")
    time.sleep(1)
    exit()
