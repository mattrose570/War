from Card import *

class Player:
    def __init__(self, name: str) -> None:
        self.wins = 0
        self.card = None
        self.name = name