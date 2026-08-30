class RoadGraph:
    """Road network graph with travel time as edge weight."""
    def __init__(self):
        self.nodes = set()
        self.edges = {}  # (u, v) -> {'length': meters, 'speed': km/h}
        self.adjacency = {}  # node -> list of neighbors
    
    def add_node(self, node_id):
        """Add intersection to graph."""
        self.nodes.add(node_id)
        if node_id not in self.adjacency:
            self.adjacency[node_id] = []
    
    def add_edge(self, u, v, length, speed, bidirectional=True):
        """Add road between two nodes."""
        # Add nodes if not exist
        self.add_node(u)
        self.add_node(v)
        
        # Forward edge
        self.edges[(u, v)] = {'length': length, 'speed': speed}
        self.adjacency[u].append(v)
        
        # Backward edge (roads usually bidirectional)
        if bidirectional:
            self.edges[(v, u)] = {'length': length, 'speed': speed}
            self.adjacency[v].append(u)
    
    def travel_time(self, u, v):
        """Travel time on edge in seconds."""
        edge = self.edges[(u, v)]
        # time = distance / speed
        # length in meters, speed in km/h -> convert to m/s
        speed_ms = edge['speed'] * 1000 / 3600
        return edge['length'] / speed_ms
    
    def neighbors(self, node_id):
        """Get neighbors of a node."""
        return self.adjacency.get(node_id, [])
    
    def edge_weight(self, u, v):
        """Weight for routing = travel time."""
        return self.travel_time(u, v)