class Solution:
    def gameOfLifeInfinite(self, live):
        ctr = collections.Counter((I, J)
                              for i, j in live
                              for I in range(i-1, i+2)
                              for J in range(j-1, j+2)
                              if I != i or J != j)
              # for each lives get a counter of adjacent from range [-1,-1 -> m+1,n+1]
        
        return {ij for ij in ctr if ctr[ij] == 3 or (ctr[ij] == 2 and ij in live)}
              # Return only where lives are equal to 3 or 2(if in live)

    def gameOfLife(self, board):
        live = {(i, j) for i, row in enumerate(board) for j, live in enumerate(row) if live}
                # Get indexes for current lives

        live = self.gameOfLifeInfinite(live)
                # Get updated lives

        for i, row in enumerate(board):
            for j, alive in enumerate(row):
                row[j] = int((i, j) in live)
                # Update each row from updated lives