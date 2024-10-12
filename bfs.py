from collections import deque

def bfs_path(graph, start, final):
    # Черга для зберігання шляхів
    queue = deque([[start]])
    # Множина для відстеження відвіданих вершин
    visited = set()

    while queue:
        # Візьмемо перший шлях з черги
        path = queue.popleft()
        # Останній вузол на шляху
        node = path[-1]

        # Якщо знайшли цільову вершину, повертаємо шлях
        if node == final:
            return path

        # Якщо вершина не була відвідана
        if node not in visited:
            # Відзначаємо її як відвідану
            visited.add(node)
            # Додаємо сусідів до черги з новими шляхами
            for neighbor in graph.neighbors(node):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    # Якщо не знайдено шляху
    return None