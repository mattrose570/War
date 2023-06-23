class Card:
    suits = ("spades", "hearts", "diamonds", "clubs")

    values = (None, None, 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace")

    def __init__(self, suit: int, value: int) -> None:
        """suit and value are integers"""
        self.value = value
        self.suit = suit

    def __lt__(self, card2: 'Card') -> bool:
        if self.value < card2.value:
            return True
        
        if self.value == card2.value:
            if self.suit < card2.suit:
                return True
            else:
                return False
        
        return False
    
    def __gt__(self, card2: 'Card') -> bool:
        if self.value > card2.value:
            return True
        if self.value == card2.value:
            if self.suit > card2.suit:
                return True
            
            else: 
                return False
            
        return False
    
    def __repr__(self) -> str:
        returnStr = f"{self.values[self.value]} of {self.suits[self.suit].capitalize()}"
        return returnStr
            


car1 = Card(2, 2)



