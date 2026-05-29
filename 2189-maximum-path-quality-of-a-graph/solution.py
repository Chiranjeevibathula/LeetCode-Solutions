class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        def dfs(current_node: int, time_spent: int, current_value: int) -> None:
            """
            Depth-first search to explore all possible paths.
          
            Args:
                current_node: Current node in the traversal
                time_spent: Total time spent so far in the path
                current_value: Total value collected so far in the path
            """
            # If we're back at node 0, update the maximum answer
            if current_node == 0:
                nonlocal max_quality
                max_quality = max(max_quality, current_value)
          
            # Explore all neighboring nodes
            for neighbor, travel_time in adjacency_list[current_node]:
                # Only proceed if we have enough time remaining
                if time_spent + travel_time <= maxTime:
                    if visited[neighbor]:
                        # If neighbor is already visited, don't add its value again
                        dfs(neighbor, time_spent + travel_time, current_value)
                    else:
                        # Mark as visited, add value, explore, then backtrack
                        visited[neighbor] = True
                        dfs(neighbor, time_spent + travel_time, current_value + values[neighbor])
                        visited[neighbor] = False  # Backtrack: unmark visited

        # Initialize graph data structures
        num_nodes = len(values)
        adjacency_list = [[] for _ in range(num_nodes)]
      
        # Build adjacency list representation of the graph
        for node_u, node_v, travel_time in edges:
            adjacency_list[node_u].append((node_v, travel_time))
            adjacency_list[node_v].append((node_u, travel_time))
      
        # Track visited nodes to avoid counting their values multiple times
        visited = [False] * num_nodes
        visited[0] = True  # Start from node 0
      
        # Initialize the maximum quality answer
        max_quality = 0
      
        # Start DFS from node 0 with initial time 0 and initial value of node 0
        dfs(0, 0, values[0])
      
        return max_quality

        
