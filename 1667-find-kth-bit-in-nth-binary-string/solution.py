class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def find_bit_recursive(level: int, position: int) -> int:
            """
            Recursively find the bit at given position in S_level.
          
            Args:
                level: Current level of the string S_level
                position: Position to find (1-indexed)
              
            Returns:
                The bit value (0 or 1) as an integer
            """
            # Base case: first bit is always 0
            if position == 1:
                return 0
          
            # Check if position is a power of 2 (middle positions are always 1)
            # Using bitwise AND: if k & (k-1) == 0, then k is a power of 2
            if (position & (position - 1)) == 0:
                return 1
          
            # Calculate the length of S_level (2^level - 1)
            string_length = 1 << level  # 2^level
          
            # If position is in the first half (before middle)
            if position * 2 < string_length - 1:
                # The bit is the same as in S_(level-1)
                return find_bit_recursive(level - 1, position)
          
            # If position is in the second half (after middle)
            # Find the corresponding position in S_(level-1) and invert
            # The second half is reverse(invert(S_(level-1)))
            mirrored_position = string_length - position
            return find_bit_recursive(level - 1, mirrored_position) ^ 1  # XOR 1 to invert
      
        # Convert the result from integer (0 or 1) to string
        return str(find_bit_recursive(n, k))
        
