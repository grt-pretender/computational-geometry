# You are given a map of a server center, represented as a m * n integer matrix grid, 
# where 1 means that on that cell there is a server and 0 means that it is no server. 
# Two servers are said to communicate if they are on the same row or on the same column.

# Return the number of servers that communicate with any other server.


def countServers(grid: list[list[int]]) -> int:

    n = len(grid)
    m = len(grid[0])
    rows, columns = [0]*n, [0]*m

    for i in range(n):
        for j in range(m):
            if grid[i][j]:
                rows[i] += 1
                columns[j] += 1
    res = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] and (rows[i] > 1 or columns[j] > 1):
                res += 1
    return res



grid = [[1,0],[1,1]]
ans = countServers(grid)
print(ans)