# %%
from get_inp import get_inp


def range_overlap(from_map, to_map):
    if (from_map[1] <= to_map[0]) or ((to_map[1] <= from_map[0])):
        return False
    else:
        return True


def overlaps(from_map, to_map):
    no_overlap = []
    overlap = []
    start_from = True
    end_from = True
    if from_map[0] < to_map[0]:
        no_overlap.append((from_map[0], to_map[0]))
        start_from = False
    if from_map[1] > to_map[1]:
        no_overlap.append((to_map[1], from_map[1]))
        end_from = False
    if start_from:
        if end_from:
            overlap.append(from_map)
        else:
            overlap.append((from_map[0], to_map[1]))
    else:
        if end_from:
            overlap.append((to_map[0], from_map[1]))
        else:
            overlap.append(to_map)

    return overlap, no_overlap


def solve_1(inp):
    seeds = inp[0][7:].split(" ")
    seeds = [int(seed) for seed in seeds]
    maps = inp[1:]
    cur_map = seeds
    cur_map_copy = seeds.copy()
    next_map = []
    for map in maps:
        map = map.splitlines()[1:]
        for row in map:
            stop, start, r = [int(i) for i in row.split(" ")]
            for c in cur_map:
                if c in range(start, start + r):
                    next_map.append(stop + (c - start))
                    cur_map_copy.remove(c)
        next_map.extend(cur_map_copy)
        cur_map = next_map
        cur_map_copy = cur_map.copy()
        next_map = []

    return min(cur_map)


def solve_2(inp):
    seeds = inp[0][7:].split(" ")
    seeds = [int(seed) for seed in seeds]
    seeds_actual = []
    for i in range(0, len(seeds), 2):
        seeds_actual.append((seeds[i], seeds[i] + seeds[i + 1]))
    maps = inp[1:]
    cur_map = seeds_actual
    cur_map_copy = seeds_actual.copy()
    next_map = []
    track_d = {}
    for map in maps:
        map = map.splitlines()[1:]
        for row in map:
            stop, start, r = [int(i) for i in row.split(" ")]
            for c in cur_map:
                if (c in track_d.keys() and track_d[c] == 0) or (
                    c not in track_d.keys()
                ):
                    if range_overlap(c, (start, start + r)):
                        overlap, no_overlap = overlaps(c, (start, start + r))
                        for no in no_overlap:
                            cur_map.append(no)
                            cur_map_copy.append(no)
                        overlap_start = overlap[0][0]
                        overlap_stop = overlap[0][1]
                        next_map.append(
                            (
                                stop + (overlap_start - start),
                                stop + (overlap_stop - start),
                            )
                        )
                        cur_map_copy.remove(c)
                        track_d[c] = 1
                    else:
                        track_d[c] = 0

        next_map.extend(cur_map_copy)
        cur_map = next_map
        cur_map_copy = cur_map.copy()
        next_map = []

    min_ans = min([s[0] for s in cur_map])
    return min_ans


if __name__ == "__main__":
    inp = get_inp(5).split("\n\n")
    res_1 = solve_1(inp)
    print(res_1)
    res_2 = solve_2(inp)
    print(res_2)
# %%
