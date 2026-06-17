class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        def dijkstra(start_city:int)->int:
            distances=[float('inf')]*n
            distances[start_city]=0
            visited=[False]*n
            for _ in range(n):
                min_dist_city=-1
                for city in range(n):
                    if not visited[city] and (min_dist_city==-1 or distances[min_dist_city]>distances[city]):
                        min_dist_city=city
                visited[min_dist_city]=True
                for neighbor in range(n):
                    if distances[min_dist_city]+adjacency_matrix[min_dist_city][neighbor]<distances[neighbor]:
                        distances[neighbor]=distances[min_dist_city]+adjacency_matrix[min_dist_city][neighbor]
            return sum(dist<=distanceThreshold for dist in distances) 
        adjacency_matrix=[[float('inf')]*n for _ in range(n)]
        for from_city,to_city,weight in edges:
            adjacency_matrix[from_city][to_city]=weight
            adjacency_matrix[to_city][from_city]=weight
        result_city=n
        min_reachable_count=float('inf')
        for city in range(n-1,-1,-1):
            reachable_count=dijkstra(city)
            if reachable_count<min_reachable_count:
                min_reachable_count=reachable_count
                result_city=city
        return result_city            




        
