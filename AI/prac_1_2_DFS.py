"""The Iterative Depth-First Search (DFS) algorithm is a method for exploring a graph or tree structure. Here’s how it works:

Begin by setting up a stack and a set to keep track of the vertices you’ve already visited.
Push the starting vertex onto the stack and mark it as visited.
Continue the process until the stack is empty:
Pop a vertex from the top of the stack.
Perform an action with that vertex, like printing it or storing it for later use.
Add all of its unvisited neighbors to the stack and mark them as visited.
When the stack is empty, the algorithm is complete, indicating that all reachable vertices have been explored."""

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    
    def add_edge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u) #Assuming an undirected Graph

    def iterative_dfs(self,start,end):
        if start == end:
            return[start]
        
        visited = set()
        stack = [(start,[start])]
        while stack:
            current_vertex,path = stack.pop()
            visited.add(current_vertex)

            for neighbor in self.graph[current_vertex]:
                if neighbor not in visited:
                    if neighbor == end:
                        return path+[neighbor]
                    stack.append((neighbor,path + [neighbor]))

        return None #No Path found
    
#Example usage:
if __name__ == "__main__":
    g=Graph()
    
    g.add_edge(1,2)
    g.add_edge(1,3)
    g.add_edge(2,4)
    g.add_edge(2,5)
    g.add_edge(3,6)
    g.add_edge(3,7)
    g.add_edge(4,8)
    g.add_edge(4,9)
    g.add_edge(5,10)
    g.add_edge(5,11)
    g.add_edge(6,12)
    g.add_edge(6,13)
    g.add_edge(7,14)
    g.add_edge(7,15)

    start_node = 1
    end_node = 9
    shortest_path = g.iterative_dfs(start_node,end_node)

    if shortest_path:
        print(f"Shortest Path Start form {start_node} to {end_node} : {shortest_path}")
    else:
        print(f"No Path found from {start_node} to ")