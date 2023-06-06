import random


class Decks:
    def __init__(self):
        pass

    def create_deck(self, number_of_decks):
        deck = []
        for i in range(number_of_decks):
            suites = ["-Hearts", "-Diamonds", "-Clubs", "-Spades"]
            pics = ["King", "Queen", "Jack", "Ace"]

            for s in suites:
                for i in range(2, 11):
                    deck.append(str(i) + s)

            for p in pics:
                for s in suites:
                    deck.append(p + s)

        random.shuffle(deck)

        return deck

    # def shuffle_deck(self):
    #     return random.shuffle(self)


def draw_card(deck):
    return deck.pop(0)


def get_score(hand: list):
    """
    TODO: change function to only add total from last card added.
    This means the main program will also need to be updated.
    """

    total = 0
    for card in hand:
        val = card.split("-")[0]
        if val.isnumeric():
            total += int(val)
        elif val.lower() in ["king", "queen", "jack"]:
            total += 10
        elif val.lower() == "ace":
            if total < 11:
                total += 11
            else:
                total += 1
    return total


class Player:
    def __init__(self, name, type):
        self.score = 0
        self.hand = []
        self.name = name
        self.type = type
        self.state = True

    def draw_card(self, deck, hand):
        return hand.append(deck.pop(0))

    def add_score(self, hand):
        self.score = get_score(hand)
        return self.score

    def get_score(self, hand: list):
        """
        TODO: change function to only add total from last card added.
        This means the main program will also need to be updated.
        """

        total = 0
        for card in hand:
            val = card.split("-")[0]
            if val.isnumeric():
                total += int(val)
            elif val.lower() in ["king", "queen", "jack"]:
                total += 10
            elif val.lower() == "ace":
                if total < 11:
                    total += 11
                else:
                    total += 1
        return total
