class Player:
    def __init__(self, number: int, is_bot: bool = False) -> None:
        self.player = number
        self.is_bot = is_bot
