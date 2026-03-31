import numpy as np
class Solution:
    def validate_num(self, counter):
        counter.pop('.')
        counter_values = counter.values()
        for val in counter_values:
            if val > 1:
                return False
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board = np.array(board)
        for i in range(9):
            # 3 * 3 Block
            threeblock = board[i//3*3:int(i//3+1)*3, i%3*3:int(i%3+1)*3]
            flattened_block = threeblock.flatten()
            counter = Counter(flattened_block)

            if self.validate_num(counter):
                pass
            else: return False

            # column Check
            row = board[:, i]
            row_flattened = row.flatten()
            counter = Counter(row_flattened)

            if self.validate_num(counter):
                pass
            else: return False

            # Row Check
            col = board[i, :]   
            col_flattened = col.flatten()
            counter = Counter(col_flattened)
            
            if self.validate_num(counter):
                pass
            else: return False
    
        return True
        