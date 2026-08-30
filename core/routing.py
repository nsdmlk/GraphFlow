import heapq
import math
from .graph import RoadGraph

class Dijkstra:
    """Shortest path using Dijkstra's algorithm."""
    
    def __init__(self, graph):
        self.graph = graph
    
    def find_path(self, start, goal):
        """Find shortest path from start to goal."""
        # Distances from start to each node
        distances = {node: float('inf') for node in self.graph.nodes}
        distances[start] = 0
        
        # Previous node in optimal path
        previous = {node: None for node in self.graph.nodes}
        
        # Priority queue: (distance, node)
        pq = [(0, start)]
        visited = set()
        
        while pq:
            current_dist, current = heapq.heappop(pq)
            
            if current in visited:
                continue
            visited.add(current)
            
            # Found goal
            if current == goal:
                break
            
            # Check neighbors
            for neighbor in self.graph.neighbors(current):
                if neighbor in visited:
                    continue
                
                edge_time = self.graph.travel_time(current, neighbor)
                new_dist = current_dist + edge_time
                
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    previous[neighbor] = current
                    heapq.heappush(pq, (new_dist, neighbor))
        
        # Reconstruct path
        path = []
        node = goal
        while node is not None:
            path.append(node)
            node = previous[node]
        path.reverse()
        
        if distances[goal] == float('inf'):
            return [], float('inf')  # no path
        
        return path, distances[goal]

class AStar:
    """A* shortest path with heuristic."""
    
    def __init__(self, graph, positions=None):
        self.graph = graph
        self.positions = positions or {}  # node -> (x, y)
    
    def heuristic(self, node, goal):
        """Estimated remaining time to goal."""
        if node in self.positions and goal in self.positions:
            x1, y1 = self.positions[node]
            x2, y2 = self.positions[goal]
            # Euclidean distance in meters
            dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
            # Divide by max speed to get time
            max_speed = self._max_speed()
            return dist / (max_speed * 1000 / 3600)  # seconds
        return 0  # no heuristic = Dijkstra
    
    def _max_speed(self):
        """Maximum speed in graph (km/h)."""
        if not self.graph.edges:
            return 60  # default
        return max(edge['speed'] for edge in self.graph.edges.values())
    
    def find_path(self, start, goal):
        """Find shortest path using A*."""
        # g_score: actual cost from start to node
        g_score = {node: float('inf') for node in self.graph.nodes}
        g_score[start] = 0
        
        # f_score: estimated total cost
        f_score = {node: float('inf') for node in self.graph.nodes}
        f_score[start] = self.heuristic(start, goal)
        
        previous = {node: None for node in self.graph.nodes}
        
        pq = [(f_score[start], start)]
        visited = set()
        
        while pq:
            current_f, current = heapq.heappop(pq)
            
            if current in visited:
                continue
            visited.add(current)
            
            if current == goal:
                break
            
            for neighbor in self.graph.neighbors(current):
                if neighbor in visited:
                    continue
                
                edge_time = self.graph.travel_time(current, neighbor)
                g_new = g_score[current] + edge_time
                
                if g_new < g_score[neighbor]:
                    g_score[neighbor] = g_new
                    f_new = g_new + self.heuristic(neighbor, goal)
                    f_score[neighbor] = f_new
                    previous[neighbor] = current
                    heapq.heappush(pq, (f_new, neighbor))
        
        # Reconstruct path
        if g_score[goal] == float('inf'):
            return [], float('inf')
        
        path = []
        node = goal
        while node is not None:
            path.append(node)
            node = previous[node]
        path.reverse()
        
        return path, g_score[goal]