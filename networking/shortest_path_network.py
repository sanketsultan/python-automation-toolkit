#Given a network topology and link costs, find the shortest path between two routers (Dijkstra).

import heapq
def dijkstra(graph, start, end):
    queue = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))
    
    # Reconstruct the shortest path
    path = []
    while end is not None:
        path.append(end)
        end = previous_nodes[end]
    path.reverse()
    
    return path, distances[path[-1]] if path else ([], float('inf'))
# Example usage:
if __name__ == "__main__":
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'D': 2, 'E': 5},
        'C': {'A': 4, 'F': 3},
        'D': {'B': 2},
        'E': {'B': 5, 'F': 1},
        'F': {'C': 3, 'E': 1}
    }
    path, cost = dijkstra(graph, 'A', 'F')
    print(f"Shortest path from A to F: {path} with cost {cost}")