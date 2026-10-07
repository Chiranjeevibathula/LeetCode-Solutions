class MyCircularDeque:
    def __init__(self, k: int):
        """
        Initialize the circular deque with a fixed capacity.
      
        Args:
            k: Maximum capacity of the deque
        """
        # Pre-allocate array with fixed size for O(1) operations
        self.buffer = [0] * k
        # Index pointing to the front element
        self.front_index = 0
        # Current number of elements in the deque
        self.current_size = 0
        # Maximum capacity of the deque
        self.max_capacity = k

    def insertFront(self, value: int) -> bool:
        """
        Insert an element at the front of the deque.
      
        Args:
            value: The value to insert
          
        Returns:
            True if insertion was successful, False if deque is full
        """
        # Check if deque has space for new element
        if self.isFull():
            return False
      
        # Move front pointer backward circularly only if deque is not empty
        # If empty, we insert at current front_index position
        if not self.isEmpty():
            self.front_index = (self.front_index - 1 + self.max_capacity) % self.max_capacity
      
        # Place the new value at the front position
        self.buffer[self.front_index] = value
        # Increment the size counter
        self.current_size += 1
        return True

    def insertLast(self, value: int) -> bool:
        """
        Insert an element at the rear of the deque.
      
        Args:
            value: The value to insert
          
        Returns:
            True if insertion was successful, False if deque is full
        """
        # Check if deque has space for new element
        if self.isFull():
            return False
      
        # Calculate the rear position using front_index and size
        rear_index = (self.front_index + self.current_size) % self.max_capacity
        # Place the new value at the rear position
        self.buffer[rear_index] = value
        # Increment the size counter
        self.current_size += 1
        return True

    def deleteFront(self) -> bool:
        """
        Remove the front element from the deque.
      
        Returns:
            True if deletion was successful, False if deque is empty
        """
        # Cannot delete from empty deque
        if self.isEmpty():
            return False
      
        # Move front pointer forward circularly
        self.front_index = (self.front_index + 1) % self.max_capacity
        # Decrement the size counter
        self.current_size -= 1
        return True

    def deleteLast(self) -> bool:
        """
        Remove the rear element from the deque.
      
        Returns:
            True if deletion was successful, False if deque is empty
        """
        # Cannot delete from empty deque
        if self.isEmpty():
            return False
      
        # Simply decrement size; the rear position is calculated dynamically
        self.current_size -= 1
        return True

    def getFront(self) -> int:
        """
        Get the value of the front element without removing it.
      
        Returns:
            The front element value, or -1 if deque is empty
        """
        # Return -1 for empty deque as per problem specification
        if self.isEmpty():
            return -1
      
        # Return the element at front_index
        return self.buffer[self.front_index]

    def getRear(self) -> int:
        """
        Get the value of the rear element without removing it.
      
        Returns:
            The rear element value, or -1 if deque is empty
        """
        # Return -1 for empty deque as per problem specification
        if self.isEmpty():
            return -1
      
        # Calculate rear position: front + size - 1 (wrapped around)
        rear_index = (self.front_index + self.current_size - 1) % self.max_capacity
        return self.buffer[rear_index]

    def isEmpty(self) -> bool:
        """
        Check if the deque is empty.
      
        Returns:
            True if deque contains no elements, False otherwise
        """
        return self.current_size == 0

    def isFull(self) -> bool:
        """
        Check if the deque is at maximum capacity.
      
        Returns:
            True if deque cannot accept more elements, False otherwise
        """
        return self.current_size == self.max_capacity


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
