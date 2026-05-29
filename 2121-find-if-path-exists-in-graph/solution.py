class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def dfs(current_node:int)->bool:
            if current_node==destination:
                return True
            if current_node in visited:
                return False
            visited.add(current_node)    
            return any(dfs(neighbor) for neighbor in adjacency_list[current_node])
        adjacency_list=[[] for _ in range(n)]
        for u,v in edges:
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)
        visited=set()
        return dfs(source)    

        
