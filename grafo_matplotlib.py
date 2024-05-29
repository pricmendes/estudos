import matplotlib.pylab as grafico
import networkx as bibliotecaNetworkx

grafo = bibliotecaNetworkx.Graph()


grafo.add_node("A")
grafo.add_node("B")
grafo.add_node("C")
grafo.add_node("D")
grafo.add_node("E")
grafo.add_node("F")

grafo.add_edge("A", "B")
grafo.add_edge("B", "C")
grafo.add_edge("C", "D")
grafo.add_edge("D", "E")
grafo.add_edge("E", "F")
grafo.add_edge("F", "A")

posicionamento = bibliotecaNetworkx.circular_layout(grafo)
bibliotecaNetworkx.draw_networkx_edge_labels(grafo, posicionamento, edge_labels = {
                                    ("A", "B"): "Aresta A-B",
                                    ("B", "C"): "Aresta B-C",
                                    ("C", "D"): "Aresta C-D",
                                    ("D", "E"): "Aresta D-E",
                                    ("E", "F"): "Aresta E-F",
                                    ("F", "A"): "Aresta F-A",
                                    },
                                font_color = "green", verticalalignment="bottom", label_pos=0.5)
bibliotecaNetworkx.draw(grafo, pos = posicionamento, with_labels = True,
                        node_color = "red",
                        edge_color = "blue")
grafico.show()

# Output:
# https://i.imgur.com/1zFpFPp.png


