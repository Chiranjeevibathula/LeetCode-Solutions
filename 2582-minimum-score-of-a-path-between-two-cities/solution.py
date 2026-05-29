class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph=defaultdict(list)
        for node_a,node_b,distance in roads:
            graph[node_a].append((node_b,distance))
            graph[node_b].append((node_a,distance))
        visited=[False]*(n+1)    
        min_score=float('inf')
        def dfs(current_node):
            nonlocal min_score
            for neighbor,edge_cost in graph[current_node]:
                min_score=min(min_score,edge_cost)
                if not visited[neighbor]:
                    visited[neighbor]=True
                    dfs(neighbor)
        visited[1]=True
        dfs(1)
        return min_score        

            
        
