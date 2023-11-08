// You are given a map of a server center, represented as a m * n integer matrix grid, 
// where 1 means that on that cell there is a server and 0 means that it is no server. 
// Two servers are said to communicate if they are on the same row or on the same column.

// Return the number of servers that communicate with any other server.

func countServers(grid [][]int) int {
    res := 0
    m, n := len(grid), len(grid[0])
    rows := make([]int, m)
    columns := make([]int, n)
    
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if grid[i][j] == 1 {
                rows[i]++
                columns[j]++
            }
        }
    }
    
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if grid[i][j] == 1 && (rows[i] + columns[j] > 2) {
                res++
            }
        }
    }
    return res
}


