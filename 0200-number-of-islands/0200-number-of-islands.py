class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Count the number of islands in a 2D grid.
        An island is formed by connecting adjacent lands ('1') horizontally or vertically.
      
        Args:
            grid: 2D grid of '1's (land) and '0's (water)
      
        Returns:
            Number of islands in the grid
        """
      
        def dfs(row: int, col: int) -> None:
            """
            Depth-first search to mark all connected land cells as visited.
            Modifies the grid in-place by changing '1' to '0'.
          
            Args:
                row: Current row index
                col: Current column index
            """
            # Mark current cell as visited (water)
            grid[row][col] = '0'
          
            # Check all 4 adjacent directions (up, right, down, left)
            for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                next_row, next_col = row + dr, col + dc
              
                # If the adjacent cell is within bounds and is unvisited land
                if (0 <= next_row < rows and 
                    0 <= next_col < cols and 
                    grid[next_row][next_col] == '1'):
                    # Recursively explore the adjacent land
                    dfs(next_row, next_col)
      
        # Initialize island counter
        island_count = 0
      
        # Get grid dimensions
        rows, cols = len(grid), len(grid[0])
      
        # Traverse each cell in the grid
        for i in range(rows):
            for j in range(cols):
                # If we find unvisited land, it's a new island
                if grid[i][j] == '1':
                    # Explore and mark the entire island
                    dfs(i, j)
                    # Increment island count
                    island_count += 1
      
        return island_count

        