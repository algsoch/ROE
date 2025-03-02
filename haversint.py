import heapq
from haversine import haversine

# Updated city connections (added more routes)
connections = [
    ("Accra", "Lagos"), ("Lagos", "Abuja"), ("Abuja", "Nairobi"), ("Nairobi", "Khartoum"),
    ("Khartoum", "Cairo"), ("Cairo", "Zurich"), ("Zurich", "Vienna")
]

# Coordinates of cities
city_coords = {
    "Accra": (5.6037, -0.187),
    "Lagos": (6.5244, 3.3792),
    "Abuja": (9.0579, 7.4951),
    "Nairobi": (-1.286389, 36.817223),
    "Khartoum": (15.5007, 32.5599),
    "Cairo": (30.0444, 31.2357),
    "Zurich": (47.3769, 8.5417),
    "Vienna": (48.2082, 16.3738)
}

def dijkstra(start, end):
    # Build graph
    graph = {city: [] for city in city_coords}
    for city1, city2 in connections:
        if city1 in city_coords and city2 in city_coords:
            distance = haversine(city_coords[city1], city_coords[city2])  # Use haversine module
            graph[city1].append((distance, city2))
            graph[city2].append((distance, city1))  # Bi-directional graph

    # Priority queue for Dijkstra’s algorithm
    queue = [(0, start, [])]  # (cost, current_node, path)
    seen = set()

    while queue:
        cost, node, path = heapq.heappop(queue)
        if node in seen:
            continue
        path = path + [node]
        if node == end:
            return path
        seen.add(node)
        for distance, neighbor in graph[node]:
            heapq.heappush(queue, (cost + distance, neighbor, path))
    
    return ["No path found"]

# Find and print the shortest path from Accra to Vienna
print(" -> ".join(dijkstra("Accra", "Vienna")))
