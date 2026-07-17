import heapq

def shortest_path(graph_data, start):
    size = len(graph_data)

    distance = [float('inf')] * size
    parent = [-1] * size
    processed = [False] * size

    distance[start] = 0
    heap = [(0, start)]

    while heap:
        current_dist, current = heapq.heappop(heap)

        if processed[current]:
            continue

        processed[current] = True

        for neighbor, weight in graph_data[current]:
            new_cost = current_dist + weight

            if new_cost < distance[neighbor]:
                distance[neighbor] = new_cost
                parent[neighbor] = current
                heapq.heappush(heap, (new_cost, neighbor))

    return distance, parent


def get_path(parent, source, destination):
    route = []

    while destination != -1:
        route.append(destination)
        destination = parent[destination]

    route.reverse()

    if route and route[0] == source:
        return route

    return []


# Graph (Adjacency List)
network = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: [(4, 3)],
    4: [(5, 2)],
    5: []
}

source = 0

distance, parent = shortest_path(network, source)

print(f"Shortest paths from vertex {source}:")
print(f"{'Vertex':<8}{'Distance':<10}{'Path':>30}")
print("-" * 55)

for vertex in range(len(network)):
    route = get_path(parent, source, vertex)
    route_str = " -> ".join(map(str, route)) if route else "No path"
    cost = distance[vertex] if distance[vertex] != float('inf') else "INF"

    print(f"{vertex:<8}{str(cost):<10}{route_str:>30}")