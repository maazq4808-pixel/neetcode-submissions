class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()
            for cell in row:
                if cell == ".":
                    continue
                if cell in seen:
                    return False
                seen.add(cell)
        for  j in range(len(board)):
            seen = set()
            for i in range(len(board)):
                if board[i][j] == ".":
                    continue
                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])
        for br in range(0, 9, 3):
            for bc in range(0, 9, 3):
                seen = set()
                for i in range(br, br + 3):
                    for j in range(bc , bc + 3):
                        if board[i][j] == ".":
                            continue
                        if board[i][j] in seen:
                            return False
                        seen.add(board[i][j])
        return True

