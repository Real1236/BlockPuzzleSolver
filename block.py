class Block:
    def __init__(self, id: int, length: int, width: int) -> None:
        self.id = id
        self.length = length
        self.width = width

    def __repr__(self) -> str:
        return f"Block(id={self.id}, length={self.length}, width={self.width})"