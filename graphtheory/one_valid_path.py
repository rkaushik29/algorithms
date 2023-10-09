from collections import deque

# Cost to make atleast one valid path - BFS
def min_cost_path(grid):
    m, n = len(grid), len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    pq = deque([(0, 0, 0)])
    
    visited = set()
    while pq:
        cost, x, y = pq.popleft()
        
        if (x, y) == (m-1, n-1):
            return cost
        
        if (x, y) in visited:
            continue
        
        visited.add((x, y))
        
        for d in range(4):
            dx, dy = directions[d]
            newX, newY = x + dx, y + dy
            
            if 0 <= newX < m and 0 <= newY < n:
                newCost = cost + (grid[x][y] - 1 != d)
                pq.append((newCost, newX, newY))
                pq = deque(sorted(pq))
