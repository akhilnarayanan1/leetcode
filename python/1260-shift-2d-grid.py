class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])  # m = number of rows, n = number of columns
        
        new_grid = [[grid[y][x] for x in range(n)] for y in range(m)] 
                                            # Create a copy of grid
        
        
        for i in range(m):
            for j in range(n):
                new_j = (j+k) % n           # Shift the columns till n
                new_i =  (i + (j+k)//n)%m   # Shift the rows till m (reset after end of row)
    
                new_grid[new_i][new_j] = grid[i][j]
                                            # Replace values
        
                
        return new_grid