class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        q = deque()
        MAX_VALUE = len(mat)*len(mat[0])
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if(mat[i][j] == 0):
                    q.append([i, j])
                else:
                    mat[i][j] = MAX_VALUE
        
        while q:
            row, col = q.popleft()

            for dir in dirs:
                newRow = row + dir[0]
                newCol = col + dir[1]
                if newRow >= 0 and newCol >= 0 and newRow < len(mat) and newCol < len(mat[0]) and mat[row][col] + 1 < mat[newRow][newCol]:
                    q.append([newRow, newCol])
                    mat[newRow][newCol] = mat[row][col] + 1
        
        return mat
