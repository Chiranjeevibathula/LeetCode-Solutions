class BinaryIndexedTree:
    """
    Binary Indexed Tree (Fenwick Tree) for efficient prefix sum queries and updates.
    Uses 1-based indexing internally.
    """
    __slots__ = ["n", "c"]

    def __init__(self, n: int) -> None:
        """
        Initialize a Binary Indexed Tree with size n.
      
        Args:
            n: The size of the array
        """
        self.n = n
        self.c = [0] * (n + 1)  # 1-indexed array for the tree

    def update(self, x: int, delta: int) -> None:
        """
        Add delta to the value at position x.
      
        Args:
            x: The 1-based index to update
            delta: The value to add to position x
        """
        while x <= self.n:
            self.c[x] += delta
            # Move to the next node that this position affects
            # x & -x gives the lowest set bit
            x += x & -x

    def query(self, x: int) -> int:
        """
        Get the prefix sum from index 1 to x (inclusive).
      
        Args:
            x: The 1-based index up to which to calculate the sum
          
        Returns:
            The prefix sum from 1 to x
        """
        total_sum = 0
        while x > 0:
            total_sum += self.c[x]
            # Move to the parent node by removing the lowest set bit
            x -= x & -x
        return total_sum


class NumArray:
    """
    Data structure that supports updating elements and calculating range sums efficiently.
    Uses a Binary Indexed Tree internally for O(log n) updates and queries.
    """
    __slots__ = ["tree"]

    def __init__(self, nums: list[int]) -> None:
        """
        Initialize the NumArray with the given array.
      
        Args:
            nums: The initial array of numbers
        """
        self.tree = BinaryIndexedTree(len(nums))
        # Build the tree by updating each position with its initial value
        # enumerate with start=1 for 1-based indexing
        for i, value in enumerate(nums, 1):
            self.tree.update(i, value)

    def update(self, index: int, val: int) -> None:
        """
        Update the value at the given index to val.
      
        Args:
            index: The 0-based index to update
            val: The new value to set at the index
        """
        # Get the current value at the index
        current_value = self.sumRange(index, index)
        # Update the tree with the difference (delta)
        # Add 1 to index for 1-based indexing in the tree
        self.tree.update(index + 1, val - current_value)

    def sumRange(self, left: int, right: int) -> int:
        """
        Calculate the sum of elements from left to right (inclusive).
      
        Args:
            left: The 0-based left boundary of the range
            right: The 0-based right boundary of the range
          
        Returns:
            The sum of elements in the range [left, right]
        """
        # Range sum = prefix_sum(right) - prefix_sum(left - 1)
        # Add 1 to convert from 0-based to 1-based indexing
        return self.tree.query(right + 1) - self.tree.query(left)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index, val)
# param_2 = obj.sumRange(left, right)

