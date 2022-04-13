class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
  
        ans = [[0 for x in range(n)] for y in range(n)] 
          # create empty matrix with 0's
    
        sr, sc, er, ec = 0, 0, n-1, n-1
          # four vertexes of the matrix
        
        curr_val = iter(range(n*n))
        
        while sr<=er and sc<=ec:
            for i in range(sc, ec+1):
                ans[sr][i] = next(curr_val)+1
            sr+=1
            
            for i in range(sr, er+1):
                ans[i][ec] = next(curr_val)+1
            ec-=1
            
            for i in range(ec, sc-1, -1):
                ans[er][i] = next(curr_val)+1
            er-=1
            
            for i in range(er, sr-1, -1):
                ans[i][sc] = next(curr_val)+1
            sc+=1
            
            
        return ans