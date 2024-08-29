#!/usr/bin/python3.12

import time

from collections import defaultdict
from dataclasses import dataclass

start = time.time()

puzzle_input = open("inputs/day_7.txt")

hands = []
hands_2 = []


@dataclass
class Hand:
    cards: str
    bid: int
    type: int

    card_order = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3",
                  "2"]
    card_order.reverse()

    def __lt__(self, other):
        if self.type < other.type:
            return True
        elif self.type > other.type:
            return False
        elif self.type == other.type:
            for i, card in enumerate(self.cards):
                if (
                        self.card_order.index(card) <
                        self.card_order.index(other.cards[i])):
                    return True
                elif (self.card_order.index(card) >
                      self.card_order.index(other.cards[i])):
                    return False


class Hand2(Hand):
    card_order = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2",
                  "J"]
    card_order.reverse()


def process_hand(cards, two=False):
    sets = list(cards.values())

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
    if two:
        hands_2.append(Hand2(card_word, int(bid), hand_type))
    else:
        hands.append(Hand(card_word, int(bid), hand_type))


for line in puzzle_input:
    card_word, bid = line.split()
    cards_in_hand = defaultdict(int)

    for card in card_word:
        cards_in_hand[card] += 1

    cards_in_hand_2 = cards_in_hand.copy()

    if card_word != "JJJJJ":
        biggest = sorted(cards_in_hand_2, key=cards_in_hand_2.get,
                         reverse=True)
        if biggest[0] == "J":
            cards_in_hand_2[biggest[1]] += cards_in_hand_2["J"]
        else:
            cards_in_hand_2[biggest[0]] += cards_in_hand_2["J"]
        del cards_in_hand_2["J"]

    process_hand(cards_in_hand)
    process_hand(cards_in_hand_2, two=True)


hands = sorted(hands)
hands_2 = sorted(hands_2)

winnings = 0
winnings_2 = 0

for i, hand in enumerate(hands):
    winnings += hand.bid * (i+1)

for i, hand in enumerate(hands_2):
    winnings_2 += hand.bid * (i+1)

print(time.time() - start)
print(winnings, winnings_2)
