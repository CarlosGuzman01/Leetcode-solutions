class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = defaultdict(set)
        columns = defaultdict(set)
        boxes = defaultdict(set)

        for row in range(9):
            for column in range(9):
                n = board[row][column]
                if n == '.':
                    continue
                if n in boxes[(row//3, column//3)] or n in rows[row] or n in columns[column]:
                    return False
                
                rows[row].add(n)
                boxes[(row//3,column//3)].add(n)
                columns[column].add(n)
                   
        return True
        