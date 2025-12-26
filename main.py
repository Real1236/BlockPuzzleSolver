from block import Block
from board import Board


def main():
    # Set Up
    # board = Board(56, 56)
    # blocksList = [
    #     [32, 10],
    #     [21, 14],
    #     [21, 18],
    #     [21, 14],
    #     [32, 11],
    #     [28, 14],
    #     [28, 6],
    #     [21, 18],
    #     [14, 4],
    #     [17, 14],
    #     [10, 7],
    #     [28, 7]
    # ]
    board = Board(4, 4)
    blocksList = [
        [1, 2],
        [1, 4],
        [2, 3],
        [2, 2]
    ]
    blocks = [Block(i + 1, blockData[0], blockData[1]) for i, blockData in enumerate[list[int]](blocksList)]
    # Sort blocks by area (largest first) for better efficiency
    blocks.sort(key=lambda b: b.length * b.width, reverse=True)

    if not check_set_up(board, blocks):
        return

    if not solve(board, blocks):
        print("No solution found")
        return
    print("Solution found")
    board.print()

def solve(board: Board, blocks: list[Block]) -> bool:
    def dfs(blocksLeft: list[Block]) -> bool:
        board.print()
        if not blocksLeft:
            return True

        x, y = board.get_first_empty_position()
        for i, block in enumerate(blocksLeft):
            # Try both orientations
            for rotated in [False, True]:
                if board.place_block(block, x, y, rotated):
                    # Prune: check if any remaining block can fit at all
                    can_fit = False
                    for b in blocksLeft[:i] + blocksLeft[i+1:]:
                        for rx in range(board.length):
                            for ry in range(board.width):
                                if board.is_valid_position(b.length if not rotated else b.width, b.width if not rotated else b.length, rx, ry):
                                    can_fit = True
                                    break
                            if can_fit:
                                break
                        if can_fit:
                            break
                    if not blocksLeft[1:] or can_fit:
                        next_blocks = blocksLeft[:i] + blocksLeft[i+1:]
                        if dfs(next_blocks):
                            return True
                    board.remove_block(block, x, y, rotated)
        return False

    return dfs(blocks)
    

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