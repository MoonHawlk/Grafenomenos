import networkx as nx
import matplotlib.pyplot as plt

# Crie um grafo não direcionado
G = nx.Graph()

# Solicite ao usuário para adicionar nós
while True:
    node = input("Digite o nome de um nó (ou pressione Enter para parar): ")
    if not node:
        break
    G.add_node(node)

# Solicite ao usuário para adicionar arestas
while True:
    edge = input("Digite as arestas no formato 'nó1 nó2' (ou pressione Enter para parar): ")
    if not edge:
        break
    node1, node2 = edge.split()
    G.add_edge(node1, node2)

# Visualize o grafo
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_size=800, node_color="lightblue", font_size=10, font_color="black", font_weight="bold")
plt.title("Grafo Não Direcionado Personalizado")
plt.show()