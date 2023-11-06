import networkx as nx
import matplotlib.pyplot as plt

def criar_grafo_nao_direcionado():
    return nx.Graph()

def adicionar_nos(graph):
    while True:
        node = input("Digite o nome de um nó (ou pressione Enter para parar): ")
        if not node:
            break
        graph.add_node(node)

def adicionar_arestas(graph):
    while True:
        edge = input("Digite as arestas no formato 'nó1 nó2' (ou pressione Enter para parar): ")
        if not edge:
            break
        node1, node2 = edge.split()
        graph.add_edge(node1, node2)

def visualizar_grafo(graph):
    pos = nx.spring_layout(graph, seed=42)
    nx.draw(graph, pos, with_labels=True, node_size=800, node_color="lightblue", font_size=10, font_color="black", font_weight="bold")
    plt.title("Grafo Não Direcionado Personalizado")
    plt.show()
