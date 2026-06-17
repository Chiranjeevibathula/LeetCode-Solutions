class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n=n
        self.adjacency_matrix=[[inf]*n for _ in range(n)]
        for from_node,to_node,cost in edges:
            self.adjacency_matrix[from_node][to_node]=cost

        
    def addEdge(self, edge: List[int]) -> None:
        from_node,to_node,cost=edge
        self.adjacency_matrix[from_node][to_node]=cost
        

    def shortestPath(self, node1: int, node2: int) -> int:
        distances=[inf]*self.n
        distances[node1]=0
        visited=[False]*self.n
        for _ in range(self.n):
            current_node=-1
            for node in range(self.n):
                if not visited[node] and (current_node==-1 or distances[current_node]>distances[node]):
                    current_node=node
            visited[current_node]=True
            for neighbor in range(self.n):
                distances[neighbor]=min(distances[neighbor],distances[current_node]+self.adjacency_matrix[current_node][neighbor])
        return -1 if distances[node2]==inf else distances[node2]                
        


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
