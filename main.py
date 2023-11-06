import networkx as nx
import matplotlib.pyplot as plt

class MeuGrafo:
    def __init__(self, direcionado=False, valorado=False):
        self.grafo = nx.DiGraph() if direcionado else nx.Graph()
        self.valorado = valorado

    def adicionar_vertice(self, vertice):
        self.grafo.add_node(vertice)

    def adicionar_aresta(self, origem, destino, peso=None):
        if self.valorado:
            self.grafo.add_edge(origem, destino, peso=peso)
        else:
            self.grafo.add_edge(origem, destino)

    def imprimir_grafo(self):
        print("Lista de Adjacência:")
        for vertice in self.grafo.nodes():
            vizinhos = list(self.grafo.neighbors(vertice))
            print(f"{vertice}: {vizinhos}")

    def tamanho_do_grafo(self):
        return len(self.grafo.nodes())

    def ordem_do_grafo(self):
        return len(self.grafo.edges())

    def vertices_adjacentes(self, vertice):
        return list(self.grafo.neighbors(vertice))

    def grau_do_vertice(self, vertice):
        if self.grafo.is_directed():
            grau_entrada = self.grafo.in_degree(vertice)
            grau_saida = self.grafo.out_degree(vertice)
            return grau_entrada, grau_saida
        else:
            return self.grafo.degree(vertice)

    def sao_adjacentes(self, vertice1, vertice2):
        return vertice2 in self.grafo[vertice1]

    def menor_caminho(self, origem, destino):
        try:
            caminho, custo = nx.shortest_path(self.grafo, origem, destino, weight='peso' if self.valorado else None), nx.shortest_path_length(self.grafo, origem, destino, weight='peso' if self.valorado else None)
            return caminho, custo
        except nx.NetworkXNoPath:
            return None, float('inf')

    def visualizar_grafo(self):
        pos = nx.spring_layout(self.grafo)
        labels = nx.get_edge_attributes(self.grafo, 'peso' if self.valorado else None)
        
        nx.draw(self.grafo, pos, with_labels=True, node_size=500, font_size=10)
        nx.draw_networkx_edge_labels(self.grafo, pos, edge_labels=labels)
        plt.show()

if __name__ == "__main__":
    while(1): 
        print("===============================================")
        print("1- Adicionar valores de maneira ")
        print("2-")
        print("3-")
        print("4-")
        print("5- Passar arquivo")
        print("===============================================")
    grafo = MeuGrafo(direcionado=True, valorado=True)

    grafo.adicionar_vertice("A")
    grafo.adicionar_vertice("B")
    grafo.adicionar_vertice("C")
    grafo.adicionar_vertice("D")

    grafo.adicionar_aresta("A", "B", peso=3)
    grafo.adicionar_aresta("A", "C", peso=2)
    grafo.adicionar_aresta("B", "C", peso=1)
    grafo.adicionar_aresta("C", "D", peso=4)

    grafo.imprimir_grafo()
    print(f"Tamanho do Grafo: {grafo.tamanho_do_grafo()}")
    print(f"Ordem do Grafo: {grafo.ordem_do_grafo()}")
    print(f"Vertices Adjacentes a 'A': {grafo.vertices_adjacentes('A')}")
    print(f"Grau do Vertice 'A': {grafo.grau_do_vertice('A')}")
    print(f"Sao adjacentes 'A' e 'B'? {grafo.sao_adjacentes('A', 'B')}")
    caminho, custo = grafo.menor_caminho("A", "D")
    print(f"Menor Caminho de 'A' para 'D': {caminho}, Custo: {custo}")

    grafo.visualizar_grafo()
