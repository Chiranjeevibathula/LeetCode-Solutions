class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        # Get dimensions of the input matrix
        rows, cols = len(mat), len(mat[0])
      
        # Create prefix sum matrix with padding (one extra row and column of zeros)
        # This helps avoid boundary checks when calculating sums
        prefix_sum = [[0] * (cols + 1) for _ in range(rows + 1)]
      
        # Build the 2D prefix sum matrix
        # prefix_sum[i][j] represents sum of all elements from mat[0][0] to mat[i-1][j-1]
        for i, row in enumerate(mat, start=1):
            for j, value in enumerate(row, start=1):
                # Current prefix sum = sum above + sum to left - overlap + current value
                prefix_sum[i][j] = (prefix_sum[i - 1][j] + 
                                   prefix_sum[i][j - 1] - 
                                   prefix_sum[i - 1][j - 1] + 
                                   value)
      
        # Initialize result matrix with same dimensions as input
        result = [[0] * cols for _ in range(rows)]
      
        # Calculate block sum for each position
        for i in range(rows):
            for j in range(cols):
                # Determine block boundaries, ensuring they stay within matrix bounds
                top_row = max(i - k, 0)
                left_col = max(j - k, 0)
                bottom_row = min(rows - 1, i + k)
                right_col = min(cols - 1, j + k)
              
                # Use prefix sum to calculate sum of the block in O(1) time
                # Formula: sum(bottom_right) - sum(top_right) - sum(bottom_left) + sum(top_left)
                result[i][j] = (prefix_sum[bottom_row + 1][right_col + 1] - 
                               prefix_sum[top_row][right_col + 1] - 
                               prefix_sum[bottom_row + 1][left_col] + 
                               prefix_sum[top_row][left_col])
      
        return result
