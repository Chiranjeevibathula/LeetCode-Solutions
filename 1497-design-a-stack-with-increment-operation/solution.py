class CustomStack:
    def __init__(self, maxSize: int):
        """
        Initialize the custom stack with a maximum size.
      
        Args:
            maxSize: Maximum number of elements the stack can hold
        """
        # Pre-allocate arrays for stack elements and increment values
        self.stack = [0] * maxSize
        # Lazy propagation array to store pending increments
        self.increment_values = [0] * maxSize
        # Current size of the stack (points to next empty position)
        self.current_size = 0

    def push(self, x: int) -> None:
        """
        Push an element onto the stack if not full.
      
        Args:
            x: Element to push onto the stack
        """
        # Only push if stack is not full
        if self.current_size < len(self.stack):
            self.stack[self.current_size] = x
            self.current_size += 1

    def pop(self) -> int:
        """
        Pop and return the top element from the stack.
      
        Returns:
            The top element value (with accumulated increments), or -1 if stack is empty
        """
        # Return -1 if stack is empty
        if self.current_size <= 0:
            return -1
      
        # Move pointer to the top element
        self.current_size -= 1
      
        # Calculate the actual value including any pending increments
        result = self.stack[self.current_size] + self.increment_values[self.current_size]
      
        # Propagate the increment value to the element below (if exists)
        if self.current_size > 0:
            self.increment_values[self.current_size - 1] += self.increment_values[self.current_size]
      
        # Clear the increment value for this position
        self.increment_values[self.current_size] = 0
      
        return result

    def increment(self, k: int, val: int) -> None:
        """
        Increment the bottom k elements of the stack by val.
        Uses lazy propagation for O(1) time complexity.
      
        Args:
            k: Number of bottom elements to increment
            val: Value to add to each element
        """
        # Find the index of the k-th element (or top if stack has fewer than k elements)
        target_index = min(k, self.current_size) - 1
      
        # Apply increment only if there are elements to increment
        if target_index >= 0:
            # Add to the increment array at the topmost affected position
            # This value will propagate down during pop operations
            self.increment_values[target_index] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
