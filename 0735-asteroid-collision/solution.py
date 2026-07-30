class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        Simulate asteroid collisions where positive values move right and negative values move left.
        When asteroids collide, the smaller one explodes; if equal size, both explode.
      
        Args:
            asteroids: List of integers representing asteroid sizes and directions
      
        Returns:
            List of asteroids remaining after all collisions
        """
        stack = []
      
        for asteroid in asteroids:
            # Positive asteroid moves right, add to stack
            if asteroid > 0:
                stack.append(asteroid)
            else:
                # Negative asteroid moves left, check for collisions
                # Keep destroying smaller right-moving asteroids
                while stack and stack[-1] > 0 and stack[-1] < -asteroid:
                    stack.pop()
              
                # Equal size asteroids destroy each other
                if stack and stack[-1] == -asteroid:
                    stack.pop()
                # No collision occurs: either stack is empty or top asteroid also moves left
                elif not stack or stack[-1] < 0:
                    stack.append(asteroid)
                # Otherwise, the current left-moving asteroid is destroyed (implicit)
      
        return stack
