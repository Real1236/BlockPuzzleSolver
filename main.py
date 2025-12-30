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
    # board = Board(4, 4)
    # blocksList = [
    #     [1, 2],
    #     [1, 4],
    #     [2, 3],
    #     [2, 2]
    # ]

    # Sort blocks by area (largest first) for better efficiency
    blocksList.sort(key=lambda x: x[0]*x[1], reverse=True)
    blocks = [Block(i + 1, blockData[0], blockData[1]) for i, blockData in enumerate[list[int]](blocksList)]

    if not check_set_up(board, blocks):
        return

    if not solve(board, blocks):
        print("\nNo solution found")
        return
    print("\nSolution found")
    board.print()

    print("\nBlocks used:")
    for block in blocks:
        print(block)

    board.export_csv("solution.csv")

def solve(board: Board, blocks: list[Block]) -> bool:
    counter = 0
    def dfs(blocksUsed: set[Block]) -> bool:
        nonlocal counter
        counter += 1
        if counter % 10000 == 0:
            print(f"DFS iterations: {counter}, blocks used: {len(blocksUsed)}/{len(blocks)}")

        if len(blocksUsed) == len(blocks):
            return True

        x, y = board.get_first_empty_position()
        for block in blocks:
            if block in blocksUsed:
                continue
            for rotated in [False, True]:
                if not board.is_valid_position(block, x, y, rotated):
                    continue
                board.place_block(block, x, y, rotated)
                next_blocks = blocksUsed | {block}
                if dfs(next_blocks):
                    return True
                board.remove_block(block, x, y, rotated)

        return False

    return dfs(set())
    

def check_set_up(board: Board, blocks: list[Block]) -> bool:
    blocksArea = sum(block.length * block.width for block in blocks)
    boardArea = board.length * board.width
    if blocksArea != boardArea:
        print("The blocks do not fit on the board")
        print("blocksArea: ", blocksArea)
        print("boardArea: ", boardArea)
        return False
    
    print("The blocks fit on the board")
    return True

if __name__ == "__main__":
    main()