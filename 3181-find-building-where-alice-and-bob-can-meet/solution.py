from typing import List
from bisect import bisect_left

class BinaryIndexedTree:
    """
    A Binary Indexed Tree (Fenwick Tree) modified to support range minimum queries.
    Used to efficiently find the minimum index for heights greater than a threshold.
    """
    __slots__ = ["size", "tree"]

    def __init__(self, size: int):
        """
        Initialize the BIT with given size.

        Args:
            size: The size of the array to index
        """
        self.size = size
        self.tree = [float('inf')] * (size + 1)

    def update(self, index: int, value: int):
        """
        Update the BIT by setting minimum value at position index.

        Args:
            index: The position to update (1-indexed)
            value: The value to set as minimum
        """
        while index <= self.size:
            self.tree[index] = min(self.tree[index], value)
            # Move to next index affected by this position
            index += index & -index

    def query(self, index: int) -> int:
        """
        Query the minimum value from index 1 to the given index.

        Args:
            index: The right boundary of the query range (1-indexed)

        Returns:
            The minimum value in range [1, index], or -1 if no valid value exists
        """
        minimum = float('inf')
        while index > 0:
            minimum = min(minimum, self.tree[index])
            # Move to parent node in BIT
            index -= index & -index
        return -1 if minimum == float('inf') else minimum


class Solution:
    def leftmostBuildingQueries(
        self, heights: List[int], queries: List[List[int]]
    ) -> List[int]:
        """
        Find the leftmost building where pairs of people can meet.

        For each query [a, b], find the leftmost building c where:
        - c >= max(a, b)
        - heights[c] > max(heights[a], heights[b])

        Args:
            heights: List of building heights
            queries: List of pairs [a, b] representing people positions

        Returns:
            List of leftmost meeting positions for each query, -1 if impossible
        """
        num_buildings = len(heights)
        num_queries = len(queries)

        # Normalize queries so that first element is always smaller
        for i in range(num_queries):
            queries[i] = [min(queries[i]), max(queries[i])]

        # Create sorted unique heights for coordinate compression
        sorted_unique_heights = sorted(set(heights))

        # Initialize result array
        result = [-1] * num_queries

        # Initialize BIT for efficient range minimum queries
        fenwick_tree = BinaryIndexedTree(num_buildings)

        # Current building index being processed (right to left)
        current_building = num_buildings - 1

        # Process queries in descending order of right endpoint
        # This allows us to incrementally build the BIT as we go
        sorted_query_indices = sorted(range(num_queries),
                                     key=lambda i: -queries[i][1])

        for query_idx in sorted_query_indices:
            left_person, right_person = queries[query_idx]

            # Add all buildings to the right of current query's right endpoint
            while current_building > right_person:
                # Compress height coordinate (1-indexed for BIT)
                # Higher heights get lower compressed values for minimum queries
                compressed_height = num_buildings - bisect_left(sorted_unique_heights,
                                                               heights[current_building]) + 1
                fenwick_tree.update(compressed_height, current_building)
                current_building -= 1

            # Check if people can meet at the right person's position
            if left_person == right_person or heights[left_person] < heights[right_person]:
                result[query_idx] = right_person
            else:
                # Need to find a building taller than left person's building
                # Query for buildings strictly taller than left person's height
                compressed_threshold = num_buildings - bisect_left(sorted_unique_heights,
                                                                  heights[left_person])
                result[query_idx] = fenwick_tree.query(compressed_threshold)

        return result

