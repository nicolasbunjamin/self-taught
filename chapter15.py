from random import shuffle


class Card:

    """the first two indexes of the values tuple are None,
    so that the strings in the tuple match up with the index they represent"""
    values = (None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10",
              "Jack", "Queen", "King", "Ace")

    """the suits are arranged in order of strength,
    with the strongest suit last"""
    suits = ("spades", "hearts", "diamonds", "clubs")

    def __init__(self, v, s):
        """suit + value are ints"""
        self.value = v
        self.suit = s
        self.name = "{} of {}".format(self.values[v], self.suits[s])

    def __repr__(self):
        return self.name

    def __lt__(self, other):
        if self.value < other.value:
            return True
        if self.value == other.value:
            if self.suit < other.suit:
                return True
        return False

    def __gt__(self, other):
        if self.value > other.value:
            return True
        if self.value == other.value:
            if self.suit > other.suit:
                return True
        return False


class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def remove_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.card = None
        self.wins = 0


class Game:
    def __init__(self):
        player1 = input("Player 1's name: ")
        player2 = input("Player 2's name: ")
        self.deck = Deck()
        self.player1 = Player(player1)
        self.player2 = Player(player2)

    def wins(self, winner):
        print("{} wins this round".format(winner))

    def draw(self, p1n, p1c, p2n, p2c):
        print("{} drew {}. {} drew {}.".format(p1n, p1c, p2n, p2c))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p2.wins > p1.wins:
            return p2.name
        return Nobody

    def play(self):
        cards = self.deck.cards
        print("Let's begin!")

        while len(cards) >= 2:
            response = input("Press Q to quit or any key to play.")
            if response.upper() == "Q":
                break

            p1n = self.player1.name
            p2n = self.player2.name
            p1c = self.deck.remove_card()
            p2c = self.deck.remove_card()
            self.draw(p1n, p1c, p2n, p2c)

            if p1c > p2c:
                self.player1.wins += 1
                self.wins(self.player1.name)
            else:
                self.player2.wins += 2
                self.wins(self.player2.name)

        win = self.winner(self.player1, self.player2)

        print("Game over. {} wins.".format(win))


game = Game()
game.play()
