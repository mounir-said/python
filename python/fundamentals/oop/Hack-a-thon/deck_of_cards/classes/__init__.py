# __init__.py
from classes.deck import Deck


class War:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player1_hand = []
        self.player2_hand = []
        self.deal_cards()

    def deal_cards(self):
        for _ in range(len(self.deck.cards) // 2):
            self.player1_hand.append(self.deck.draw())
            self.player2_hand.append(self.deck.draw())

    def play_round(self):
        card1 = self.player1_hand.pop(0)
        card2 = self.player2_hand.pop(0)

        print(f"Player 1: {card1.string_val} of {card1.suit}")
        print(f"Player 2: {card2.string_val} of {card2.suit}")

        if card1.point_val > card2.point_val:
            print("Player 1 wins the round!")
            self.player1_hand.extend([card1, card2])
        elif card1.point_val < card2.point_val:
            print("Player 2 wins the round!")
            self.player2_hand.extend([card1, card2])
        else:
            print("It's a tie!")

    def play_game(self):
        round_num = 1
        while self.player1_hand and self.player2_hand:
            print(f"Round {round_num}:")
            self.play_round()
            round_num += 1

        if not self.player1_hand:
            print("Player 2 wins the game!")
        else:
            print("Player 1 wins the game!")


if __name__ == "__main__":
    game = War()
    game.play_game()
