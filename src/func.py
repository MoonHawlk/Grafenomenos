import networkx as nx
import matplotlib.pyplot as plt
import subprocess
import os

def exibir_menu():
    print("\nMenu:")
    print("1. Inserir Nós")
    print("2. Inserir Arestas")
    print("3. Visualizar Grafo")
    print("4. Ordem e Tamanho do Grafo")
    print("5. Listar Vértices Adjacentes")
    print("6. Obter Grau do Vértice")
    print("7. Verificar Adjacência entre Vértices")
    print("8. Encontrar Caminho Mais Curto")
    print("9. Apagar Grafo Atual")
    print("0. Sair")

def limpar_terminal():
    if subprocess.call("clear" if os.name != 'nt' else 'cls', shell=True) != 0:
        print("Limpeza do terminal não suportada no seu sistema.")

def criar_grafo(direcionado):
    if direcionado:
        return nx.DiGraph()
    else:
        return nx.Graph()

def adicionar_nos(graph):
    while True:
        node = input("Digite o nome de um nó (ou pressione Enter para parar): ")
        if not node:
            break
        graph.add_node(node)

def adicionar_arestas(graph, valorado):
    while True:
        edge = input("Digite as arestas no formato 'nó1 nó2' (ou pressione Enter para parar): ")
        if not edge:
            break
        node1, node2 = edge.split()
        if valorado:
            weight = float(input("Digite o peso da aresta: "))
            graph.add_edge(node1, node2, weight=weight)
        else:
            graph.add_edge(node1, node2)

def visualizar_grafo(graph, valorado):
    pos = nx.spring_layout(graph, seed=42)
    nx.draw(graph, pos, with_labels=True, node_size=800, node_color="lightblue", font_size=10, font_color="black", font_weight="bold")
    
    if valorado:
        labels = nx.get_edge_attributes(graph, 'weight')
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    
    plt.title("Grafo Personalizado")
    plt.show()

def ordem_e_tamanho_do_grafo(graph):
    ordem = len(graph.nodes)
    tamanho = len(graph.edges)
    print(f"Ordem do grafo: {ordem}")
    print(f"Tamanho do grafo: {tamanho}")

def listar_vertices_adjacentes(graph):
    node = input("Digite o vértice para listar os vértices adjacentes: ")
    if node in graph.nodes:
        adjacentes = list(graph.neighbors(node))
        print(f"Vértices adjacentes a {node}: {', '.join(adjacentes)}")
    else:
        print(f"O vértice {node} não existe no grafo.")

def obter_grau_do_vertice(graph, direcionado):
    node = input("Digite o vértice para obter o grau: ")
    if node in graph.nodes:
        grau = len(list(graph.neighbors(node)))
        grau_entrada = len(list(graph.predecessors(node))) if direcionado else grau
        grau_saida = len(list(graph.successors(node))) if direcionado else grau
        print(f"Grau do vértice {node}: {grau}")
        if direcionado:
            print(f"Grau de entrada do vértice {node}: {grau_entrada}")
            print(f"Grau de saída do vértice {node}: {grau_saida}")
    else:
        print(f"O vértice {node} não existe no grafo.")

def verificar_adjacencia_entre_vertices(graph):
    v1 = input("Digite o primeiro vértice: ")
    v2 = input("Digite o segundo vértice: ")
    if graph.has_edge(v1, v2):
        print(f"{v1} e {v2} são adjacentes.")
    else:
        print(f"{v1} e {v2} não são adjacentes.")

def encontrar_caminho_mais_curto(graph, valorado):
    source = input("Digite o vértice de origem: ")
    target = input("Digite o vértice de destino: ")
    if source in graph.nodes and target in graph.nodes:
        try:
            if valorado:
                shortest_path, shortest_distance = nx.single_source_dijkstra(graph, source=source, target=target)
                print(f"Caminho mais curto de {source} para {target}: {shortest_path}")
                print(f"Custo do caminho mais curto: {shortest_distance}")
            else:
                shortest_path = nx.shortest_path(graph, source=source, target=target)
                print(f"Caminho mais curto de {source} para {target}: {shortest_path}")
        except nx.NetworkXNoPath:
            print(f"Não há caminho entre {source} e {target}.")
    else:
        print("Os vértices de origem e/ou destino não existem no grafo.")

def apagar_grafo(graph):
    graph.clear()
