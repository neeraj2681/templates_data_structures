#Assumes the 0 based indexing for the nodes in the graph
class DFS:
    #pass the number of vertices, and adj_list(if exist) to the constructor
    def __init__(self, vertices, adj_list):
        self.vertices = vertices
        self.adj_list = adj_list
        self.visited = [0] * vertices
        self.paths = []
    
    #adds an edge b/w the two given vertex        
    def add_edge(self, edge):
        self.adj_list[edge[0]].append(edge[1])
        self.adj_list[edge[1]].append(edge[0])
    
    #returns True if a path exist b/w the source and the destination vertex, o/w returns False
    def path_exists(self, source, destination):
        if (source == destination):
            self.path = True
        self.visited[source] = 1
        
        for vertex in self.adj_list[source]:
            if (self.visited[vertex] == 0):
                self.path_exists(vertex, destination)
        return self.path
    
    #return the list of all the possible paths from the source vertex to the destination vertex
    def find_paths(self, source, destination, path):
        path = path + [source]
        if source == destination:
            self.paths.append(path)
        
        if source != destination:
            for neighbour in self.adj_list[source]:
                self.find_paths(neighbour, destination, path)