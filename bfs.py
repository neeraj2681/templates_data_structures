from collections import deque

#Assumes 0-based indexing for the nodes in the graph
class BFS:
    #pass the number of vertices and adj_list(if exists) to the constructor
    def __init__(self, vertices, adj_list):
        self.vertices = vertices
        self.adj_list = adj_list
        self.paths = []
        self.visited = [False] * vertices
        
    #adds and edge b/w the given vertices(assumes the graph is undirected in nature)    
    def add_edge(self, source, destination):
        self.adj_list[source].append(destination)
        self.adj_list[destination].append(source)
    
    #returns True if a path exist b/w the source and the destination, o/w returns False
    def path_exist(self, source, destination):
        queue = deque()
        queue.append(source)
        
        
        while (queue):
            cur_node = queue.popleft()
            self.visited[cur_node] = True

            if cur_node == destination:
                    return True

            for neighbour in self.adj_list[cur_node]:
                if not self.visited[neighbour]:
                    queue.append(neighbour)
                    
        return False
    #returns a list of all the possible paths from source to destination
    def all_paths(self, source, destination):
        queue = deque()
        queue.append([source])
        
        while (queue):
            cur_path = queue.popleft()
            cur_node = cur_path[-1]
            
            if cur_node == destination:
                self.paths.append(cur_path)
                
            for neighbour in self.adj_list[cur_node]:
                temp = cur_path + [neighbour]
                queue.append(temp)
                
            
            