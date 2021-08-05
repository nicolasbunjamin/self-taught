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


deck = Deck()

for card in deck.cards:
    print(card)
