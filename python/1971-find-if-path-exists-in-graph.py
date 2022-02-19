class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph = {i:[] for i in range(n)}
        for i, v in edges:
            graph[i].append(v)
            graph[v].append(i)          # Bi-directional graph
            
        stack = [source]
        seen = set()                    # Set to keep track 👀 for visited nodes
        
        def dfs():
            while stack:
                node = stack.pop()      # Use stack.pop(0) for BFS 🤔

                if node == destination:
                    return True         # If destination is found, return True ✅

                if node in seen:
                    continue            # If node is already visited, continue ⏭️

                seen.add(node)

                for i in graph[node]:
                    stack.append(i)

            return False                # If destination is not found, return False ❎
        
        if not dfs():
            return False
        return True