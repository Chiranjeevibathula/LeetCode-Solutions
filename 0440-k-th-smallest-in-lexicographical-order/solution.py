class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        """
        Find the k-th smallest number in lexicographical order from 1 to n.
      
        Args:
            n: The upper bound of the range [1, n]
            k: The position of the number to find (1-indexed)
          
        Returns:
            The k-th smallest number in lexicographical order
        """
      
        def count_steps_between_prefixes(current_prefix: int) -> int:
            """
            Count how many numbers exist in the lexicographical range 
            starting with current_prefix up to the next prefix.
          
            For example, if current_prefix = 1, this counts all numbers
            starting with 1 (like 1, 10, 11, ..., 19, 100, 101, ...) 
            up to but not including those starting with 2.
          
            Args:
                current_prefix: The current prefix to count from
              
            Returns:
                Number of valid numbers with this prefix within range [1, n]
            """
            next_prefix = current_prefix + 1
            steps_count = 0
          
            # Count numbers at each level of the tree
            # Level 1: single digits (1-9)
            # Level 2: double digits (10-99)
            # Level 3: triple digits (100-999), etc.
            while current_prefix <= n:
                # Count valid numbers at this level
                # Either count all numbers between current_prefix and next_prefix-1
                # Or stop at n if it's smaller
                steps_count += min(n - current_prefix + 1, next_prefix - current_prefix)
              
                # Move to next level (add a digit)
                next_prefix *= 10
                current_prefix *= 10
              
            return steps_count
      
        # Start with number 1
        current_number = 1
      
        # We've already counted the first number (1), so decrement k
        k -= 1
      
        # Find the k-th number by navigating the lexicographical tree
        while k > 0:
            # Count how many numbers are under the current prefix
            steps_to_next_prefix = count_steps_between_prefixes(current_number)
          
            if k >= steps_to_next_prefix:
                # Skip entire subtree and move to next sibling
                k -= steps_to_next_prefix
                current_number += 1  # Move to next prefix at same level
            else:
                # The target is within current subtree, go deeper
                k -= 1  # Count current number
                current_number *= 10  # Go to first child (append 0)
              
        return current_number
