# For obstacles, like bishops on the board, maintain visited cells based on row, col and whether the bishop has been taken; separate visited array for other pieces

class cell:
    def __init__(self, x = 0, y = 0, d = 0):
        self.x = x
        self.y = y
        self.d = d


# checks if position is within board
def isWithin(x, y, n):
    if (x >= 1 and x <= n and y >= 1 and y <= n):
        return True
    
    return False

# min steps to reach target
def minSteps(start, end, n):

    # possible movement for knight
    dx = [2, 2, -2, -2, 1, 1, -1, -1]
    dy = [1, -1, 1, -1, 2, -2, 2, -2]

    queue = []

    # start posn in queue
    queue.append(cell(start[0], start[1], 0))

    # all cells unvisted
    visited = [[False for i in range(n + 1)]
                    for j in range(n + 1)]
    
    visited[start[0]][start[1]] = True

    while(len(queue) > 0):
        t = queue[0]
        queue.pop(0)

        if (t.x == end[0] and t.y == end[1]):
            return t.d

        for i in range(8):
            x = t.x + dx[i]
            y = t.y + dy[i]

            if(isWithin(x, y, n) and not visited[x][y]):
                visited[x][y] = True
                queue.append(cell(x, y, t.d + 1))

