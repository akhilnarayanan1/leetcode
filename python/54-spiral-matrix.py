class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    
        m = len(matrix)
        n = len(matrix[0])
        sr, sc, er, ec = 0, 0, m-1, n-1
        ans = []
        count = 0
        
        while sr<=er and sc<=ec:
            for i in range(sc, ec+1):
                ans.append(matrix[sr][i])
                count+=1
            sr+=1
            
            if count == m*n: return ans
            
            
            for i in range(sr, er+1):
                ans.append(matrix[i][ec])
                count+=1
            ec-=1
            
            if count == m*n: return ans
            
            for i in range(ec, sc-1, -1):
                ans.append(matrix[er][i])
                count+=1
            er-=1
            
            if count == m*n: return ans
            
            for i in range(er, sr-1, -1):
                ans.append(matrix[i][sc])
                count+=1
            sc+=1
            
            if count == m*n: return ans
            
            
        return ans