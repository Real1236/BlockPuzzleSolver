from typing import Any
import csv

from block import Block

class Board:
    def __init__(self, length: int, width: int) -> None:
        self.length = length
        self.width = width
        self.board = [[0 for _ in range(width)] for _ in range(length)]

    def place_block(self, block: Block, x: int, y: int, rotated: bool) -> None:
        length, width = block.length, block.width
        if rotated:
            length, width = block.width, block.length
            
        for i in range(length):
            for j in range(width):
                self.board[x + i][y + j] = block.id

    def remove_block(self, block: Block, x: int, y: int, rotated: bool) -> None:
        length, width = block.length, block.width
        if rotated:
            length, width = block.width, block.length

        for i in range(length):
            for j in range(width):
                self.board[x + i][y + j] = 0
        
    def is_valid_position(self, block: Block, x: int, y: int, rotated: bool) -> bool:
        length, width = block.length, block.width
        if rotated:
            length, width = block.width, block.length

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
        return -1, -1

    def print(self) -> None:
        # Print header row with column numbers starting from 1
        header = "    " + " ".join(f"{j+1:2}" for j in range(self.width))
        print(header)
        print("   +" + "---" * self.width + "--+")

        for i, row in enumerate[Any](self.board):
            row_str = " ".join(f"{cell if cell != 0 else '.':2}" for cell in row)
            print(f"{i+1:2} | {row_str} |")

        print("   +" + "---" * self.width + "--+")

    def export_csv(self, filename: str) -> None:
        """Export the current board state to a CSV file."""
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for row in self.board:
                writer.writerow(row)
