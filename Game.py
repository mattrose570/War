from Card import *
from Deck import *
from Player import *

class Game:
    def __init__(self) -> None:
        self.deck = Deck()
        self.player1 = Player(input("Player 1's name: "))
        self.player2 = Player(input("Player 2's name: "))
        

    def wins(self, winner: Player) -> None:
        w = f"{winner.name} wins this round"
        print(w)

    def draw(self, p1Name: str, p1Card: Card, p2Name: str, p2Card: Card):
        returnStr = f"{p1Name} drew a {p1Card}; {p2Name} drew a {p2Card}"
        print(returnStr)

    def winner(self, player1: Player, player2: Player) -> str:
        if player1.wins > player2.wins:
            return f"War is over. {player1.name} wins!"
        
        elif player2.wins > player1.wins:
            return f"War is over. {player2.name} wins"
        
        else:
            return "It was a tie."
                
    def another_game(self):
        decision = input("Would you like to start another game? (y or n): ")
        while decision.lower() != "y" and decision.lower() != "n":
            decision = input("Would you like to start another game? (y or n): ")
        
            if decision == "y":
                newGame = Game()
                newGame.play_game()

            
        else:
            exit(0)



    def play_game(self):
        cards = self.deck.cards
        while len(cards) >= 2:
            question = input("Press q to quit. Any key to start")
            if question == "q":
                break
        
            p1Name = self.player1.name
            p2Name = self.player2.name
            p1Card = self.deck.remove_card()
            p2Card = self.deck.remove_card()

            self.draw(p1Name, p1Card, p2Name, p2Card)

            if p1Card > p2Card:
                self.player1.wins += 1
                self.wins(self.player1)

            elif p2Card > p1Card:
                self.player2.wins += 1
                self.wins(self.player2)

        print(self.winner(self.player1, self.player2))
        self.another_game()

