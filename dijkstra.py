import networkx as nx

def dijkstra(graph, start):
    # Ініціалізація відстаней та попередників
    distances = {vertex: float('infinity') for vertex in graph.nodes}
    distances[start] = 0
    previous_vertices = {vertex: None for vertex in graph.nodes}
    unvisited = list(graph.nodes)

    while unvisited:
        # Знаходження вершини з найменшою відстанню серед невідвіданих
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        # Якщо поточна відстань є нескінченністю, то ми завершили роботу
        if distances[current_vertex] == float('infinity'):
            break

        # Переглядаємо всіх сусідів поточної вершини
        for neighbor in graph.neighbors(current_vertex):
            weight = graph[current_vertex][neighbor].get('weight', 1)  # отримуємо вагу ребра
            distance = distances[current_vertex] + weight

            # Якщо нова відстань коротша, оновлюємо її і попередника
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_vertices[neighbor] = current_vertex

        # Видаляємо поточну вершину з множини невідвіданих
        unvisited.remove(current_vertex)

    # Функція для відновлення шляху
    def get_path(vertex):
        path = []
        current = vertex
        while current is not None:
            path.append(current)
            current = previous_vertices[current]
        return path[::-1]  # шлях у зворотньому порядку

    return distances, get_path
