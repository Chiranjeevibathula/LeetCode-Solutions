class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows, cols = len(isWater), len(isWater[0])
      
        # Initialize result matrix with -1 (unvisited cells)
        heights = [[-1] * cols for _ in range(rows)]
      
        # Queue for BFS traversal
        queue = deque()
      
        # Find all water cells and mark them as height 0
        for row in range(rows):
            for col in range(cols):
                if isWater[row][col] == 1:
                    queue.append((row, col))
                    heights[row][col] = 0
      
        # Define four directions: up, right, down, left
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
      
        # BFS to assign heights to all cells
        while queue:
            current_row, current_col = queue.popleft()
          
            # Check all four adjacent cells
            for delta_row, delta_col in directions:
                next_row = current_row + delta_row
                next_col = current_col + delta_col
              
                # Check if the adjacent cell is within bounds and unvisited
                if (0 <= next_row < rows and 
                    0 <= next_col < cols and 
                    heights[next_row][next_col] == -1):
                  
                    # Assign height as current cell's height + 1
                    heights[next_row][next_col] = heights[current_row][current_col] + 1
                    queue.append((next_row, next_col))
      
        return heights
        
