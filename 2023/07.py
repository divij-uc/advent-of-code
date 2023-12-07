# %%
from get_inp import get_inp
from enum import IntEnum


class Card(IntEnum):
    A = 14
    K = 13
    Q = 12
    J = 11
    T = 10
    _9 = 9
    _8 = 8
    _7 = 7
    _6 = 6
    _5 = 5
    _4 = 4
    _3 = 3
    _2 = 2
    _J = 1


card_map = {
    "A": Card.A,
    "K": Card.K,
    "Q": Card.Q,
    "T": Card.T,
    "9": Card._9,
    "8": Card._8,
    "7": Card._7,
    "6": Card._6,
    "5": Card._5,
    "4": Card._4,
    "3": Card._3,
    "2": Card._2,
}


class Hand:
    def __init__(self, cards) -> None:
        self.cards = cards

    def __repr__(self) -> str:
        return " ".join([str(c) for c in self.cards])

    def get_highest_card(self):
        high_card = -1
        for card in self.cards:
            if card > high_card:
                high_card = card

    def get_hand_dict(self):
        hand_dict = {}
        for card in self.cards:
            if card in hand_dict.keys():
                hand_dict[card] += 1
            else:
                hand_dict[card] = 1
        return hand_dict

    def get_type(self):
        hand_dict = self.get_hand_dict()

        hand_type = -1
        max_hand = max(hand_dict.values())
        if max_hand >= 4:
            hand_type = max_hand
        elif max_hand == 3:
            if 2 in hand_dict.values():
                hand_type = 3
            else:
                hand_type = 2
        elif max_hand == 2:
            pair = 0
            for val in hand_dict.values():
                if val == 2:
                    pair += 1
            if pair == 2:
                hand_type = 1
            else:
                hand_type = 0
        return hand_type

    def get_type_J(self):
        if Card._J not in self.cards:
            hand_type = self.get_type()
        else:
            hand_type = -1
            hand_dict = self.get_hand_dict()
            vals_wo_J = [
                hand_dict[card] for card in hand_dict.keys() if card != Card._J
            ]
            if len(vals_wo_J) == 0:
                hand_type = 5
            else:
                max_hand = max(vals_wo_J)
                if max_hand == 4:
                    hand_type = 5
                elif max_hand == 3:
                    hand_type = 3 + hand_dict[Card._J]
                elif max_hand == 2:
                    pair = 0
                    for val in vals_wo_J:
                        if val == 2:
                            pair += 1
                    if pair == 2:
                        hand_type = 3
                    elif hand_dict[Card._J] == 1:
                        hand_type = 2
                    else:
                        hand_type = 2 + hand_dict[Card._J]
                else:
                    if hand_dict[Card._J] == 1:
                        hand_type = 0
                    elif hand_dict[Card._J] == 2:
                        hand_type = 2
                    else:
                        hand_type = 1 + hand_dict[Card._J]
        return hand_type


def solve(inp, q=1):
    track = []  ## (hand, type+high, rank, bid)
    for row in inp:
        hand, bid = row.split(" ")
        card_list = []
        if q == 1:
            card_map["J"] = Card.J
        else:
            card_map["J"] = Card._J
        for card in hand:
            card_list.append(card_map[card])
        hand = Hand(card_list)
        cur_rank = len(track) + 1
        cur_score = (
            (15**4) * hand.cards[0]
            + (15**3) * hand.cards[1]
            + (15**2) * hand.cards[2]
            + (15**1) * hand.cards[3]
            + (15**0) * hand.cards[4]
        )
        if q == 1:
            cur_score += (15**5) * hand.get_type()
        else:
            cur_score += (15**5) * hand.get_type_J()
        for i in range(len(track)):
            if track[i][1] > cur_score:
                track[i][2] += 1
                cur_rank -= 1

        track.append([hand, cur_score, cur_rank, int(bid)])

    sum_ans = 0
    for row in track:
        sum_ans += row[2] * row[3]

    return sum_ans


if __name__ == "__main__":
    inp = get_inp(7).splitlines()
    res_1 = solve(inp, 1)
    print(res_1)
    res_2 = solve(inp, 2)
    print(res_2)

# %%
