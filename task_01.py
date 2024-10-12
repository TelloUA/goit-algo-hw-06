import networkx as nx
import matplotlib.pyplot as plt

# Створюємо неорієнтований граф
G = nx.Graph()

# Додаємо зв'язки між людьми
edges = [
    # Група 1:
    ("Іра", "Саша"), ("Іра", "Айдер"), ("Іра", "Марина"),
    ("Саша", "Айдер"), ("Саша", "Марина"),
    ("Айдер", "Марина"),

    # Група 2:
    ("Слава", "Андрій"), ("Слава", "Денис"), ("Слава", "Руслан"),
    ("Андрій", "Денис"), ("Андрій", "Руслан"),
    ("Денис", "Руслан"),

    # Додаткові звʼязки
    ("Слава", "Іра"), ("Слава", "Женя"), ("Іра", "Женя"),
    ("Маша", "Марина"), ("Маша", "Руслан"),
    ("Андрій", "Айдер"), ("Андрій", "Рома"), ("Айдер", "Юля"), ("Рома", "Юля")
]

# Додаємо ребра до графа
G.add_edges_from(edges)

# Аналіз характеристик графа
num_nodes = G.number_of_nodes()  # Кількість вершин
num_edges = G.number_of_edges()  # Кількість ребер
degrees = dict(G.degree())  # Ступінь кожної вершини (кількість зв'язків)

# Виведення результатів
print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print("Ступінь вершин:")
for node, degree in degrees.items():
    print(f"{node}: {degree}")

degree_centrality = nx.degree_centrality(G)
print(f"{degree_centrality}")
closeness_centrality = nx.closeness_centrality(G)
print(f"{closeness_centrality}")
betweenness_centrality = nx.betweenness_centrality(G)
print(f"{betweenness_centrality}")

# Додатково: діаметр графа (максимальна відстань між будь-якими двома вершинами)
if nx.is_connected(G):
    diameter = nx.diameter(G)
    print(f"Діаметр графа: {diameter}")

# Візуалізація графа
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=3000, font_size=10, font_weight='bold', edge_color='gray')
plt.title("Мережа спілкування в компанії")
plt.show()