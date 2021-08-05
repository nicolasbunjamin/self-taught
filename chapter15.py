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


card1 = Card(5, 0)
card2 = Card(6, 2)
card3 = Card(6, 1)
card4 = Card(6, 3)

print(card1)
print(card2)
print(card3)
print(card4)

print(card1 > card2)  # False
print(card2 < card3)  # False
print(card2 > card4)  # False
print(card4 > card3)  # True
