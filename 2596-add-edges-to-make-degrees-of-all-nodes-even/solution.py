class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        # Build adjacency list representation of the graph
        adjacency_list = defaultdict(set)
        for node_a, node_b in edges:
            adjacency_list[node_a].add(node_b)
            adjacency_list[node_b].add(node_a)
      
        # Find all vertices with odd degree
        odd_degree_vertices = [vertex for vertex, neighbors in adjacency_list.items() 
                               if len(neighbors) % 2 == 1]
      
        # If all vertices have even degree, graph is already Eulerian
        if len(odd_degree_vertices) == 0:
            return True
      
        # If exactly 2 vertices have odd degree
        if len(odd_degree_vertices) == 2:
            vertex_a, vertex_b = odd_degree_vertices
          
            # Check if we can directly connect these two vertices
            if vertex_a not in adjacency_list[vertex_b]:
                return True
          
            # Try to find an intermediate vertex to connect both odd-degree vertices
            for intermediate_vertex in range(1, n + 1):
                if (vertex_a not in adjacency_list[intermediate_vertex] and 
                    intermediate_vertex not in adjacency_list[vertex_b]):
                    return True
            return False
      
        # If exactly 4 vertices have odd degree
        if len(odd_degree_vertices) == 4:
            vertex_a, vertex_b, vertex_c, vertex_d = odd_degree_vertices
          
            # Try all three possible pairings to connect the 4 vertices
            # Pairing 1: (a,b) and (c,d)
            if (vertex_a not in adjacency_list[vertex_b] and 
                vertex_c not in adjacency_list[vertex_d]):
                return True
          
            # Pairing 2: (a,c) and (b,d)
            if (vertex_a not in adjacency_list[vertex_c] and 
                vertex_b not in adjacency_list[vertex_d]):
                return True
          
            # Pairing 3: (a,d) and (b,c)
            if (vertex_a not in adjacency_list[vertex_d] and 
                vertex_b not in adjacency_list[vertex_c]):
                return True
          
            return False
      
        # More than 4 vertices with odd degree cannot be fixed with at most 2 edges
        return False
        
