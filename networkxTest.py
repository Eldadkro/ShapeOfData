import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
for i in range(5):
    G.add_node(i)

for i in range(4):
    G.add_edge(*(i, i + 1))

options = {
    "font_size": 36,
    "node_size": 3000,
    "node_color": "white",
    "edgecolors": "black",
    "linewidths": 5,
    "width": 5,
}


nx.draw_networkx(G)
ax = plt.gca()
ax.margins(0.20)
plt.axis("off")
plt.show()
