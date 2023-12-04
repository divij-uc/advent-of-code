# %%
from get_inp import get_inp


def solve_1(inp):
    final_game_sum = 0
    game_dict = {}
    for game_row in inp:
        game_poss = True
        id, game = game_row.split(":")
        id = int(id[5:])
        game_iters = game.split(";")

        for game_iter in game_iters:
            game_dict["red"] = 0
            game_dict["blue"] = 0
            game_dict["green"] = 0
            draws = game_iter.split(",")
            for draw in draws:
                num, col = draw.split()
                num = int(num)
                game_dict[col] = num
            if (
                game_dict["red"] > 12
                or game_dict["blue"] > 14
                or game_dict["green"] > 13
            ):
                game_poss = False
                break

        if game_poss:
            final_game_sum += id
    return final_game_sum


def solve_2(inp):
    final_game_sum = 0
    game_dict = {}
    for game_row in inp:
        id, game = game_row.split(":")
        id = int(id[5:])
        game_iters = game.split(";")
        min_red, min_blue, min_green = 0, 0, 0
        for game_iter in game_iters:
            game_dict["red"] = 0
            game_dict["blue"] = 0
            game_dict["green"] = 0
            draws = game_iter.split(",")
            for draw in draws:
                num, col = draw.split()
                num = int(num)
                game_dict[col] = num
            min_red = max(min_red, game_dict["red"])
            min_green = max(min_green, game_dict["green"])
            min_blue = max(min_blue, game_dict["blue"])

        final_game_sum += min_red * min_blue * min_green
    return final_game_sum


if __name__ == "__main__":
    inp = get_inp(2).splitlines()
    res_1 = solve_1(inp)
    res_2 = solve_2(inp)
    print(res_1)
    print(res_2)
