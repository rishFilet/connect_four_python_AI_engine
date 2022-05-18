#This is a short class but can be extended to included player colours, names and further customisation of player
class Player:
    def __init__(self, number: int, is_bot: bool = False) -> None:
        self.player = number
        self.is_bot = is_bot

