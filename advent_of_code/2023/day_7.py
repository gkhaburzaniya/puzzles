from collections import defaultdict
from dataclasses import dataclass

puzzle_input = open("inputs/day_7_input.txt")

card_order = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
card_order.reverse()
hands = []


@dataclass
class Hand:
    cards: str
    bid: int
    type: int

    def __lt__(self, other):
        if self.type < other.type:
            return True
        elif self.type > other.type:
            return False
        elif self.type == other.type:
            for i, card in enumerate(self.cards):
                if card_order.index(card) < card_order.index(other.cards[i]):
                    return True
                elif card_order.index(card) > card_order.index(other.cards[i]):
                    return False


for line in puzzle_input:
    card_word, bid = line.split()
    cards_in_hand = defaultdict(int)

    for card in card_word:
        cards_in_hand[card] += 1

    sets = list(cards_in_hand.values())

    if 5 in sets:
        hand_type = 6
    elif 4 in sets:
        hand_type = 5
    elif 3 in sets and 2 in sets:
        hand_type = 4
    elif 3 in sets:
        hand_type = 3
    elif 2 in sets and 2 in sets[(sets.index(2)+1):]:
        hand_type = 2
    elif 2 in sets:
        hand_type = 1
    else:
        hand_type = 0
    hands.append(Hand(card_word, int(bid), hand_type))

hands = sorted(hands)

winnings = 0

for i, hand in enumerate(hands):
    winnings += hand.bid * (i+1)

print(winnings)
