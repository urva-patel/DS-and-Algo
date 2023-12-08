class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkDict(sud, dic, coor):
            if sud in dic:
                if coor in dic[sud]:
                    return True
            else:
                dic[sud] = set()
            dic[sud].add(coor)

            return False

        masterDict = {}
        rowDict = {}
        colDict = {}

        for i in range(len(board)):
            row = i//3
            for j in range(len(board)):
                col = j//3
                if board[i][j] != '.':
                    sud = str(row) + '.' + str(col)
                    if checkDict(sud, masterDict, board[i][j]) or checkDict(str(i), rowDict, board[i][j]) or checkDict(str(j), colDict, board[i][j]):
                        return False

        
        return True