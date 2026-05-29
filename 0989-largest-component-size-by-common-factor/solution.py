from typing import List
from collections import Counter


class UnionFind:
    """Union-Find (Disjoint Set Union) data structure with path compression."""
  
    def __init__(self, n: int) -> None:
        """Initialize n disjoint sets, each element is its own parent initially."""
        self.parent = list(range(n))
  
    def union(self, a: int, b: int) -> None:
        """Unite the sets containing elements a and b."""
        root_a = self.find(a)
        root_b = self.find(b)
      
        # Only unite if they belong to different sets
        if root_a != root_b:
            self.parent[root_a] = root_b
  
    def find(self, x: int) -> int:
        """Find the root of the set containing x with path compression."""
        if self.parent[x] != x:
            # Path compression: make every node point directly to the root
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        """
        Find the size of the largest connected component where two numbers 
        are connected if they share a common factor greater than 1.
      
        Args:
            nums: List of positive integers
          
        Returns:
            Size of the largest connected component
        """
        # Create UnionFind structure with size equal to max value + 1
        max_value = max(nums)
        union_find = UnionFind(max_value + 1)
      
        # For each number, connect it with all its factors
        for num in nums:
            # Find all factors by iterating up to sqrt(num)
            factor = 2
            while factor * factor <= num:
                if num % factor == 0:
                    # Connect num with its factor
                    union_find.union(num, factor)
                    # Connect num with its complementary factor (num // factor)
                    union_find.union(num, num // factor)
                factor += 1
      
        # Count the size of each connected component
        # by finding the root of each number and counting occurrences
        component_sizes = Counter(union_find.find(num) for num in nums)
      
        # Return the size of the largest component
        return max(component_sizes.values())
