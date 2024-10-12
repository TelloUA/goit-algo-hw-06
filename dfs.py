def dfs_path(graph, start, goal):
    # Стек для зберігання шляхів
    stack = [[start]]
    # Множина для відстеження відвіданих вершин
    visited = set()
    paths = []

    # Поки стек не порожній
    while stack:
        # Візьмемо останній шлях зі стеку
        path = stack.pop()
        # Останній вузол на шляху
        node = path[-1]

        # Якщо знайшли цільову вершину, повертаємо шлях
        if node == goal:
            paths.append(path)

        # Якщо вершина не була відвідана
        if node not in visited:
            # Відзначаємо її як відвідану
            visited.add(node)
            # Додаємо сусідів до стеку з новими шляхами
            for neighbor in graph.neighbors(node):
                new_path = list(path)
                new_path.append(neighbor)
                stack.append(new_path)

    if not paths:
        return None
    else:
        result = paths[0]
        for path in paths:
            if len(path) < len(result):
                result = path
        return result

    # Якщо не знайдено шляху