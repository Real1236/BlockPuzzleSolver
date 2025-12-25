from block import Block
from board import Board


def main():
    # Set Up
    board = Board(56, 56)
    blocksList = [
        [32, 10],
        [21, 14],
        [21, 18],
        [21, 14],
        [32, 11],
        [28, 14],
        [28, 6],
        [21, 18],
        [14, 4],
        [17, 14],
        [10, 7],
        [28, 7]
    ]
    blocks = [Block(i + 1, blockData[0], blockData[1]) for i, blockData in enumerate[list[int]](blocksList)]

    if not check_set_up(board, blocks):
        return

    if not solve(board, blocks):
        print("No solution found")
        return
    print("Solution found")
    print(board)

def solve(board: Board, blocks: list[Block]) -> bool:
    def dfs(blocksLeft: set[Block]) -> bool:
        if len(blocksLeft) == 0:
            return True

        x, y = board.get_first_empty_position()
        for block in blocksLeft:
            if board.place_block(block, x, y, False):
                blocksLeft.discard(block)
                if dfs(blocksLeft):
                    return True
                blocksLeft.add(block)
                board.remove_block(block, x, y, False)
            if board.place_block(block, x, y, True):
                blocksLeft.discard(block)
                if dfs(blocksLeft):
                    return True
                blocksLeft.add(block)
                board.remove_block(block, x, y, True)
            
        return False

    for block in blocks:
        if dfs(set[Block](blocks)):
            return True
        
    return False
    

def check_set_up(board: Board, blocks: list[Block]) -> bool:
    blocksArea = sum(block.length * block.width for block in blocks)
    boardArea = board.length * board.width
    print(len(blocks))
    if blocksArea != boardArea:
        print("The blocks do not fit on the board")
        print("blocksArea: ", blocksArea)
        print("boardArea: ", boardArea)
        return False
    
    print("The blocks fit on the board")
    return True

if __name__ == "__main__":
    main()