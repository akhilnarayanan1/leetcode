class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        vertices = len(graph)
        target = len(graph) - 1
        preMap = {i:graph[i] for i in range(vertices)}  # Graph created 🕸️

        
        results = []                                    # List to store results 📝 (output)
        
        def dfs(curr, path):
            if curr == target:
                results.append(list(path))              # path=connection between nodes 🔗
                return
            
            for i in preMap[curr]:
                path.append(i)
                dfs(i, path)                            # Recursive call 🔥
                path.pop()                              # pop to backtrack 🔙
            
        path = [0]
        dfs(0, path)
        
        return results
