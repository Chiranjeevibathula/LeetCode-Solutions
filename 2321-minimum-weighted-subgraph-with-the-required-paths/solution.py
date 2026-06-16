class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        def dijkstra(graph: defaultdict, start_node: int) -> List[float]:
            """
            Compute shortest distances from start_node to all other nodes.
          
            Args:
                graph: Adjacency list representation of the graph
                start_node: Starting node for shortest path computation
              
            Returns:
                List of shortest distances from start_node to each node
            """
            # Initialize distances with infinity
            distances = [inf] * n
            distances[start_node] = 0
          
            # Priority queue: (distance, node)
            priority_queue = [(0, start_node)]
          
            while priority_queue:
                current_distance, current_node = heappop(priority_queue)
              
                # Skip if we've already found a better path to this node
                if current_distance > distances[current_node]:
                    continue
              
                # Explore neighbors
                for neighbor, edge_weight in graph[current_node]:
                    new_distance = distances[current_node] + edge_weight
                  
                    # Update distance if we found a shorter path
                    if distances[neighbor] > new_distance:
                        distances[neighbor] = new_distance
                        heappush(priority_queue, (new_distance, neighbor))
          
            return distances
      
        # Build forward graph and reverse graph
        forward_graph = defaultdict(list)
        reverse_graph = defaultdict(list)
      
        for from_node, to_node, weight in edges:
            forward_graph[from_node].append((to_node, weight))
            reverse_graph[to_node].append((from_node, weight))
      
        # Compute shortest distances from src1 to all nodes
        distances_from_src1 = dijkstra(forward_graph, src1)
      
        # Compute shortest distances from src2 to all nodes
        distances_from_src2 = dijkstra(forward_graph, src2)
      
        # Compute shortest distances from all nodes to dest (using reverse graph)
        distances_to_dest = dijkstra(reverse_graph, dest)
      
        # Find minimum total weight by considering each node as meeting point
        # Total weight = distance(src1 -> node) + distance(src2 -> node) + distance(node -> dest)
        min_total_weight = min(
            dist1 + dist2 + dist3 
            for dist1, dist2, dist3 in zip(distances_from_src1, distances_from_src2, distances_to_dest)
        )
      
        # Return -1 if no valid path exists, otherwise return the minimum weight
        return -1 if min_total_weight >= inf else min_total_weight

        
