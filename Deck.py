from random import shuffle
from Card import *

class Deck:
    
    def __init__(self) -> None:
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(j, i))
        
        shuffle(self.cards)

    def remove_card(self) -> None:

        if len(self.cards) == 0:
            return
        return self.cards.pop()


