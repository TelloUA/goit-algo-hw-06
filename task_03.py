import networkx as nx
import matplotlib.pyplot as plt
from dijkstra import dijkstra

G = nx.Graph()

# Ваги - коєфіцієнт укладнення комунікації, чим менше - тим краща комунікація між людьми
# 4 - середнє
edges = [
    # Група 1: 
    ("Іра", "Саша", 4), ("Іра", "Айдер", 2), ("Іра", "Марина", 4),
    ("Саша", "Айдер", 4), ("Саша", "Марина", 5),
    ("Айдер", "Марина", 4),

    # Група 2:
    ("Слава", "Андрій", 3), ("Слава", "Денис", 4), ("Слава", "Руслан", 4),
    ("Андрій", "Денис", 4), ("Андрій", "Руслан", 4),
    ("Денис", "Руслан", 5),

    # Додаткові звʼязки
    ("Слава", "Іра", 5), ("Слава", "Женя", 2), ("Іра", "Женя", 5),
    ("Маша", "Марина", 2), ("Маша", "Руслан", 5),
    ("Андрій", "Айдер", 2), ("Андрій", "Рома", 4), ("Айдер", "Юля", 4), ("Рома", "Юля", 6)
]

G.add_weighted_edges_from(edges)

shortest_path = nx.shortest_path(G, source="Женя", target="Юля", weight="weight")
print(f"Shortest path from Женя to Юля: {shortest_path}")

plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=3000, font_size=10, font_weight='bold', edge_color='gray')
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9)

plt.title("Мережа спілкування в компанії")
plt.show()

# Шукаємо інформація відносно Жені
result_dict, path_function = dijkstra(G, "Женя")
print(result_dict) # Відстані до усіх від Жені
# Шлях Жені до Юлі
print(path_function("Юля"))
