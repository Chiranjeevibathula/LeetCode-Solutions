from typing import List


class UnionFind:
    """Union-Find (Disjoint Set Union) data structure with path compression."""
  
    def __init__(self, n: int) -> None:
        """Initialize n disjoint sets, each containing one element."""
        self.parent = list(range(n))  # Each node is initially its own parent
        self.num_components = n  # Number of connected components
  
    def union(self, node_a: int, node_b: int) -> bool:
        """
        Union two sets containing node_a and node_b.
        Returns True if they were in different sets, False otherwise.
        """
        root_a = self.find(node_a)
        root_b = self.find(node_b)
      
        if root_a == root_b:
            return False  # Already in the same set
      
        # Merge the two sets by making one root point to the other
        self.parent[root_a] = root_b
        self.num_components -= 1
        return True
  
    def find(self, node: int) -> int:
        """
        Find the root of the set containing node.
        Applies path compression for optimization.
        """
        if self.parent[node] != node:
            # Path compression: make all nodes point directly to root
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]


class Solution:
    def findCriticalAndPseudoCriticalEdges(
        self, n: int, edges: List[List[int]]
    ) -> List[List[int]]:
        """
        Find critical and pseudo-critical edges in an MST.
      
        Critical edge: MST weight increases if this edge is removed
        Pseudo-critical edge: Can be in some MST but not critical
      
        Args:
            n: Number of vertices
            edges: List of edges [from, to, weight]
      
        Returns:
            List containing two lists: [critical_edges, pseudo_critical_edges]
        """
        # Add original index to each edge to track them after sorting
        for edge_idx, edge in enumerate(edges):
            edge.append(edge_idx)
      
        # Sort edges by weight for Kruskal's algorithm
        edges.sort(key=lambda edge: edge[2])
      
        # Find MST weight using standard Kruskal's algorithm
        uf_mst = UnionFind(n)
        mst_weight = 0
        for from_node, to_node, weight, _ in edges:
            if uf_mst.union(from_node, to_node):
                mst_weight += weight
      
        critical_edges = []
        pseudo_critical_edges = []
      
        # Check each edge to determine if it's critical or pseudo-critical
        for from_node, to_node, weight, original_idx in edges:
            # Test 1: Try building MST without this edge
            uf_without = UnionFind(n)
            weight_without = 0
          
            for curr_from, curr_to, curr_weight, curr_idx in edges:
                if curr_idx != original_idx:  # Skip current edge
                    if uf_without.union(curr_from, curr_to):
                        weight_without += curr_weight
          
            # If graph is disconnected or weight increases, edge is critical
            if uf_without.num_components > 1 or weight_without > mst_weight:
                critical_edges.append(original_idx)
                continue
          
            # Test 2: Force include this edge and build MST
            uf_with = UnionFind(n)
            uf_with.union(from_node, to_node)
            weight_with = weight  # Start with current edge weight
          
            for curr_from, curr_to, curr_weight, curr_idx in edges:
                if curr_idx != original_idx:  # Skip current edge (already included)
                    if uf_with.union(curr_from, curr_to):
                        weight_with += curr_weight
          
            # If MST weight remains same, edge is pseudo-critical
            if weight_with == mst_weight:
                pseudo_critical_edges.append(original_idx)
      
        return [critical_edges, pseudo_critical_edges]

        
