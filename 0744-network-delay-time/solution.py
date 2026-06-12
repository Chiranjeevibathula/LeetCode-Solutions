class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph=[[float('inf')]*n for _ in range(n)]
        for source,destination,weights in times:
            graph[source-1][destination-1]=weights
        distances=[float('inf')]*n
        distances[k-1]=0
        visited=[False]*n    
        for _ in range(n):
            min_node=-1
            for node in range(n):
                if not visited[node] and (min_node==-1 or distances[min_node]>distances[node]):
                    min_node=node
            visited[min_node]=True
            for neighbor in range(n):
                distances[neighbor]=min(distances[neighbor],distances[min_node]+graph[min_node][neighbor])
        max_distance=max(distances)
        return -1 if max_distance==float('inf') else max_distance       

        
