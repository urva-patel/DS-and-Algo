class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        #start at each gate and update empty rooms if they have a val larger than curr dist
        colLen = len(rooms[0])
        inf = 2147483647
        q = []
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for i in range(len(rooms)):
            for j in range(len(rooms[i])):
                if rooms[i][j] == 0:
                    q.append([i, j])
        while len(q) != 0:
            qLen = len(q)
            for i in range(qLen):
                [row, col] = q.pop(0)
                distance = rooms[row][col]+1
                for [i, j] in dirs:
                    newRow = row + i
                    newCol = col + j
                    if(newRow >= 0 and newCol >= 0 and newRow < len(rooms) and newCol < colLen and rooms[newRow][newCol] == inf):
                        rooms[newRow][newCol] = distance
                        q.append([newRow, newCol])

        