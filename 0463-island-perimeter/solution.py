class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        total_perimeter=0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==1:
                    total_perimeter+=4
                    if row<rows-1 and grid[row+1][col]==1:
                        total_perimeter-=2
                    if col<cols-1 and grid[row][col+1]==1:
                        total_perimeter-=2
        return total_perimeter                    
        
