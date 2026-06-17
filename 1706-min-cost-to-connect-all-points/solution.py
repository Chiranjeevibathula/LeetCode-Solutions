class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        Find minimum cost to connect all points using Manhattan distance.
        Uses Prim's algorithm to find the Minimum Spanning Tree (MST).
      
        Args:
            points: List of coordinates [x, y]
      
        Returns:
            Minimum cost to connect all points
        """
        n = len(points)
      
        # Build adjacency matrix with Manhattan distances between all pairs
        graph = [[0] * n for _ in range(n)]
        for i, (x1, y1) in enumerate(points):
            for j in range(i + 1, n):
                x2, y2 = points[j]
                manhattan_distance = abs(x1 - x2) + abs(y1 - y2)
                graph[i][j] = graph[j][i] = manhattan_distance
      
        # Initialize arrays for Prim's algorithm
        min_distance = [float('inf')] * n  # Minimum distance to connect each node to MST
        visited = [False] * n  # Track which nodes are already in MST
      
        # Start from node 0
        min_distance[0] = 0
        total_cost = 0
      
        # Add all n nodes to MST one by one
        for _ in range(n):
            # Find unvisited node with minimum distance to MST
            current_node = -1
            for node in range(n):
                if not visited[node] and (current_node == -1 or min_distance[node] < min_distance[current_node]):
                    current_node = node
          
            # Add selected node to MST
            visited[current_node] = True
            total_cost += min_distance[current_node]
          
            # Update minimum distances for remaining unvisited nodes
            for neighbor in range(n):
                if not visited[neighbor]:
                    min_distance[neighbor] = min(min_distance[neighbor], graph[current_node][neighbor])
      
        return total_cost

        
