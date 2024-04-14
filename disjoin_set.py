class DisjointSet:
    
    #pass the number of nodes to the constructor
    def __init__(self, nodes):
        #stores the root for the vertex -- root acts as a key for the connected component
        self.root = [i for i in range(nodes)]

        #store the rank : rank is the height, to have a tree with minimum height possible
        self.rank = [1] * nodes

    #find with path compression 
    def find(self, x):
        if self.root[x] == x:
            return self.root[x]
        
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    # union with rank(the tree with higher rank~height will become thr root)    
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)

        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.root[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.root[rootx] = rooty
            else:
                self.root[rooty] = rootx
                self.rank[rootx] += 1
                
            
        