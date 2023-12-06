# %%
from get_inp import get_inp


def solve_1(inp):
    time_row, dist_row = inp.splitlines()
    times = [int(time) for time in time_row[9:].split(" ") if time]
    dists = [int(dist) for dist in dist_row[9:].split(" ") if dist]
    total_n_wins = 1
    for time, dist in zip(times, dists):
        win_start = 0
        win_end = 0
        for i in range(time):
            if (time - i) * i > dist:
                win_start = i
                break
        for i in range(time, 0, -1):
            if (time - i) * i > dist:
                win_end = i
                break
        total_n_wins *= win_end - win_start + 1
    return total_n_wins


def solve_2(inp):
    time_row, dist_row = inp.splitlines()
    time = int(time_row[9:].replace(" ", ""))
    dist = int(dist_row[9:].replace(" ", ""))
    win_start = 0
    win_end = 0
    for i in range(time):
        if (time - i) * i > dist:
            win_start = i
            break
    for i in range(time, 0, -1):
        if (time - i) * i > dist:
            win_end = i
            break
    return win_end - win_start + 1


if __name__ == "__main__":
    inp = get_inp(6)
    res_1 = solve_1(inp)
    print(res_1)
    res_2 = solve_2(inp)
    print(res_2)

# %%
