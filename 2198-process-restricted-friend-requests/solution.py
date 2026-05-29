class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        def find(node: int) -> int:
            """
            Find the root parent of a node with path compression.
          
            Args:
                node: The node to find the root for
              
            Returns:
                The root parent of the node
            """
            if parent[node] != node:
                # Path compression: make node point directly to root
                parent[node] = find(parent[node])
            return parent[node]
      
        # Initialize parent array where each person is their own parent initially
        parent = list(range(n))
      
        # Store results for each request
        result = []
      
        # Process each friend request
        for person_u, person_v in requests:
            # Find the root parents of both people
            parent_u = find(person_u)
            parent_v = find(person_v)
          
            if parent_u == parent_v:
                # Already in the same friend group, request automatically approved
                result.append(True)
            else:
                # Check if merging these groups would violate any restriction
                is_valid = True
              
                for restricted_x, restricted_y in restrictions:
                    # Find parents of the restricted pair
                    parent_x = find(restricted_x)
                    parent_y = find(restricted_y)
                  
                    # Check if merging would put restricted pair in same group
                    if (parent_u == parent_x and parent_v == parent_y) or \
                       (parent_u == parent_y and parent_v == parent_x):
                        is_valid = False
                        break
              
                result.append(is_valid)
              
                # If valid, perform the union operation
                if is_valid:
                    parent[parent_u] = parent_v
      
        return result

        
