# %%
from get_inp import get_inp
import numpy as np


def solve_1_2(inp):
    total_points = 0
    num_scratchcards = np.ones(len(inp))
    for card_idx, line in enumerate(inp):
        cur_num_wins = -1
        win_cards = line[10:39]
        cur_cards = line[42:]
        win_cards = [int(card) for card in win_cards.split(" ") if card]
        cur_cards = [int(card) for card in cur_cards.split(" ") if card]
        for win_card in win_cards:
            if win_card in cur_cards:
                cur_num_wins += 1
        if cur_num_wins >= 0:
            total_points += 2**cur_num_wins
            num_scratchcards[card_idx + 1: card_idx + 2 + cur_num_wins] += num_scratchcards[card_idx]

    return total_points, np.sum(num_scratchcards)


if __name__ == "__main__":
    inp = get_inp(4).splitlines()
    res_1, res_2 = solve_1_2(inp)
    print(res_1)
    print(res_2)
# %%
