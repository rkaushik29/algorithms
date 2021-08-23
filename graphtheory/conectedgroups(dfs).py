class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]
     
    # Adds a relation as a two way
    # edge of undirected graph.
    def addRelation(self, v, w):
         
        # Since indexing is 0 based,
        # reducing edge numbers by 1.
        v -= 1
        w -= 1
        self.adj[v].append(w)
        self.adj[w].append(v)
     
    # Returns count of not visited
    # nodes reachable from v using DFS.
    def countUtil(self, v, visited):
        count = 1
        visited[v] = True
        i = 0
        while i != len(self.adj[v]):
            if (not visited[self.adj[v][i]]):
                count = count + self.countUtil(self.adj[v][i],
                                                      visited)
            i += 1
        return count
     
    # A DFS based function to Count number
    # of existing groups and number of new
    # groups that can be formed using a
    # member of every group.
    def countGroups(self):
         
        # Mark all the vertices as
        # not visited
        visited = [0] * self.V
     
        existing_groups = 0
        new_groups = 1
        for i in range(self.V):
             
            # If not in any group.
            if (visited[i] == False):
                existing_groups += 1
                 
                # Number of new groups that
                # can be formed.
                new_groups = (new_groups *
                              self.countUtil(i, visited))
         
        if (existing_groups == 1):
            new_groups = 0
         
        print("No. of existing groups are",
                           existing_groups)
        print("No. of new groups that",
              "can be formed are", new_groups)
 
# Driver code
if __name__ == '__main__':
 
    n = 5 # n in n x n matrix
 
    g = Graph(n)
    # loop over matrix and add relations for n x n matrix input to create a graph
    g.addRelation(1, 2) 
    g.addRelation(3, 4) 
    g.addRelation(5, 6) 
 
    g.countGroups()
