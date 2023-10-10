class UnionFind:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 1 for v in vertices}

    def find(self, u):
        if self.parent[u] == u:
            return u
        self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)

        if u == v:
            return
        if self.rank[u] > self.rank[v]:
            u, v = v, u

        self.parent[u] = v

        if self.rank[u] == self.rank[v]:
            self.rank[v] += 1
