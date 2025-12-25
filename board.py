from block import Block


class Board:
    def __init__(self, length: int, width: int) -> None:
        self.length = length
        self.width = width
        self.board = [[0 for _ in range(width)] for _ in range(length)]

    def place_block(self, block: Block, x: int, y: int, rotated: bool) -> bool:
        length, width = block.length, block.width
        if rotated:
            length, width = block.width, block.length
            
        if not self.is_valid_position(length, width, x, y):
            return False
        for i in range(length):
            for j in range(width):
                self.board[x + i][y + j] = block.id
        return True

    def remove_block(self, block: Block, x: int, y: int, rotated: bool) -> None:
        length, width = block.length, block.width
        if rotated:
            length, width = block.width, block.length

        for i in range(length):
            for j in range(width):
                self.board[x + i][y + j] = 0
        
    def is_valid_position(self, length: int, width: int, x: int, y: int) -> bool:
        if x + length > self.length or y + width > self.width:
            return False
        for i in range(length):
            for j in range(width):
                if self.board[x + i][y + j] != 0:
                    return False
        return True

    def get_first_empty_position(self) -> tuple[int, int]:
        for i in range(self.length):
            for j in range(self.width):
                if self.board[i][j] == 0:
                    return i, j
        return None