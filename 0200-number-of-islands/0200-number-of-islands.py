class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rowLen = len(grid)
        colLen = len(grid[0])
        total = 0
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for i in range(rowLen):
            for j in range(colLen):
                if(grid[i][j] == "1"):
                    q = [[i , j]]
                    while(len(q) != 0):
                        [row, col] = q.pop(0)
                        for di in dirs:
                            newRow = row + di[0]
                            newCol = col + di[1]
                            if(newRow >= 0 and newCol >= 0 and newRow < rowLen and newCol < colLen and grid[newRow][newCol] == "1"):
                                grid[newRow][newCol] = "2"
                                q.append([newRow, newCol])
                    total += 1
        
        return total




    