# %%
from get_inp import get_inp
import numpy as np
import numpy.ma as ma


def get_neighbors(arr, center, j_n, i_n):
    i, j = center
    i_start, i_end = i
    j_start, j_end = j
    j_start_out = np.max([j_start - 1, 0])
    i_start_out = np.max([i_start - 1, 0])
    j_end_out = np.min([j_end + 1, j_n])
    i_end_out = np.min([i_end + 1, i_n])
    neighborhood = arr[j_start_out:j_end_out, i_start_out:i_end_out]

    start_j_ma = j_start - j_start_out
    start_i_ma = i_start - i_start_out
    end_j_ma = j_end - j_start_out
    end_i_ma = i_end - i_start_out

    mask = np.zeros((j_end_out - j_start_out, i_end_out - i_start_out))
    mask[start_j_ma:end_j_ma, start_i_ma:end_i_ma] = 1

    masked_neighbors = ma.masked_array(neighborhood, mask)

    return masked_neighbors.compressed()


def solve_1(inp):
    i_n = len(inp)
    j_n = len(inp[0])
    start_i = -1
    end_i = -1
    final_sum = 0
    for j in range(j_n):
        for i in range(i_n):
            if inp[j, i] in "0123456789":
                if start_i == -1:
                    start_i = i
                end_i = i
            elif end_i != -1:
                neighbors = get_neighbors(
                    inp, ((start_i, end_i + 1), (j, j + 1)), j_n, i_n
                )
                if not all(neighbors == "."):
                    n = "".join(inp[j, start_i : end_i + 1])
                    final_sum += int(n)
                start_i = -1
                end_i = -1
        if end_i != -1:
            neighbors = get_neighbors(inp, ((start_i, end_i + 1), (j, j + 1)), j_n, i_n)
            if not all(neighbors == "."):
                n = "".join(inp[j, start_i : end_i + 1])
                final_sum += int(n)
            start_i = -1
            end_i = -1

    return final_sum


def get_star_pos(arr, center, j_n, i_n):
    i, j = center
    i_start, i_end = i
    j_start, j_end = j
    j_start_out = np.max([j_start - 1, 0])
    i_start_out = np.max([i_start - 1, 0])
    j_end_out = np.min([j_end + 1, j_n])
    i_end_out = np.min([i_end + 1, i_n])
    stars = []
    for j in range(j_start_out, j_end_out):
        for i in range(i_start_out, i_end_out):
            if arr[j, i] == "*":
                stars.append((j, i))
    return stars


def solve_2(inp):
    i_n = len(inp)
    j_n = len(inp[0])
    start_i = -1
    end_i = -1
    final_sum = 0
    final_gears = 0
    arr_gears = np.zeros((j_n, i_n))
    for j in range(j_n):
        for i in range(i_n):
            if inp[j, i] in "0123456789":
                if start_i == -1:
                    start_i = i
                end_i = i
            elif end_i != -1:
                neighbors = get_neighbors(
                    inp, ((start_i, end_i + 1), (j, j + 1)), j_n, i_n
                )
                if "*" in neighbors:
                    n = "".join(inp[j, start_i : end_i + 1])
                    stars = get_star_pos(
                        inp, ((start_i, end_i + 1), (j, j + 1)), j_n, i_n
                    )
                    for star in stars:
                        if arr_gears[star[0], star[1]] == 0:
                            arr_gears[star[0], star[1]] = int(n)
                        else:
                            g = arr_gears[star[0], star[1]] * int(n)
                            arr_gears[star[0], star[1]] = 0
                            final_gears += g
                start_i = -1
                end_i = -1
        if end_i != -1:
            neighbors = get_neighbors(inp, ((start_i, end_i + 1), (j, j + 1)), j_n, i_n)
            if "*" in neighbors:
                n = "".join(inp[j, start_i : end_i + 1])
                j_start_out = np.max([j - 1, 0])
                i_start_out = np.max([start_i - 1, 0])
                j_end_out = np.min([j + 2, j_n])
                i_end_out = np.min([end_i + 2, i_n])
                if np.any(arr_gears[j_start_out:j_end_out, i_start_out:i_end_out] != 0):
                    val = np.max(
                        arr_gears[j_start_out:j_end_out, i_start_out:i_end_out]
                    )
                    g = val * int(n)
                    final_gears += g
                else:
                    arr_gears[j_start_out:j_end_out, i_start_out:i_end_out] = n
            start_i = -1
            end_i = -1
    return final_gears


if __name__ == "__main__":
    inp = get_inp(3)
    inp = np.array([list(line) for line in inp.splitlines()])
    res_1 = solve_1(inp)
    print(res_1)
    res_2 = solve_2(inp)
    print(res_2)
