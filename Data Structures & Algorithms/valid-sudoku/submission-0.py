class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        alrSeen = set()
        for i in range(9):
            for j in range (9):
                if board[i][j] in alrSeen and board[i][j] != ".":
                    return False
                alrSeen.add(board[i][j])
            alrSeen = set()
        for i in range(9):
            for j in range (9):
                if board[j][i] in alrSeen and board[j][i] != ".":
                    return False
                alrSeen.add(board[j][i])
            alrSeen = set()
        boxes = {}
        for row in range (9):
            for col in range (9):
                if board[row][col] == ".":
                    continue
                box = (row // 3) * 3 + (col // 3)

                if box not in boxes:
                    boxes[box] = set()

                if board[row][col] in boxes[box]:
                    return False

                boxes[box].add(board[row][col])
        return True
                
        