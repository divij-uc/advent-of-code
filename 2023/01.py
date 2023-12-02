# %%
from get_inp import get_inp


def solve_1(inp):
    res = 0
    for line in inp:
        first_num = None
        last_num = None
        for char in line:
            if char in "0123456789":
                first_num = int(char)
                break
        for char in line[::-1]:
            if char in "0123456789":
                last_num = int(char)
                break
        res += first_num * 10 + last_num

    return res


def forward_search(search_str):
    if search_str[:3] == "one":
        return 1
    elif search_str[:3] == "two":
        return 2
    elif search_str == "three":
        return 3
    elif search_str[:4] == "four":
        return 4
    elif search_str[:4] == "five":
        return 5
    elif search_str[:3] == "six":
        return 6
    elif search_str == "seven":
        return 7
    elif search_str == "eight":
        return 8
    elif search_str[:4] == "nine":
        return 9
    return None


def backward_search(search_str):
    if search_str[-3:] == "one":
        return 1
    elif search_str[-3:] == "two":
        return 2
    elif search_str == "three":
        return 3
    elif search_str[-4:] == "four":
        return 4
    elif search_str[-4:] == "five":
        return 5
    elif search_str[-3:] == "six":
        return 6
    elif search_str == "seven":
        return 7
    elif search_str == "eight":
        return 8
    elif search_str[-4:] == "nine":
        return 9
    return None


def solve_2(inp):
    res = 0
    for line in inp:
        first_num = None
        last_num = None
        cur_num = None
        ptr = 0
        while ptr < len(line):
            if line[ptr] in "0123456789":
                cur_num = int(line[ptr])
            else:
                cur_num = forward_search(line[ptr : ptr + 5])
            ptr += 1
            if cur_num:
                first_num = cur_num
                break
            cur_num = None
        ptr = len(line)
        cur_num = None
        while ptr >= 0:
            if line[ptr - 1] in "0123456789":
                cur_num = int(line[ptr - 1])
            else:
                cur_num = backward_search(line[ptr - 5 : ptr])
            ptr -= 1
            if cur_num:
                last_num = cur_num
                break
            cur_num = None

        res += first_num * 10 + last_num
    return res


if __name__ == "__main__":
    inp = get_inp()
    res_1 = solve_1(inp)
    res_2 = solve_2(inp)
    print("puz_1", res_1)
    print("puz_2", res_2)

# %%
