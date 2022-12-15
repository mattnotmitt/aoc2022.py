from collections import defaultdict
import re
from typing import Union

INPUT = "14/14.txt"

def sum_tup(a,b):
    return tuple(sum(x) for x in zip(a, b))

def generate_map(input: list[str]) -> dict[int, dict[int, str]]:
    map = defaultdict(lambda: defaultdict(lambda: "."))
    void = 0

    for line in input:
        point_strs = line.split(" -> ")
        for i,point_str in enumerate(point_strs):
            if i == 0:
                continue

            [a_x, a_y] = [int(c) for c in re.match("(\d+),(\d+)",point_strs[i-1]).groups()]
            [b_x, b_y] = [int(c) for c in re.match("(\d+),(\d+)",point_str).groups()]

            if b_x - a_x == 0:
                min_y = min([a_y, b_y])
                max_y = max([a_y, b_y])
                for y in range(min_y, max_y+1):
                    map[a_x][y] = "#"
            elif b_y - a_y == 0:
                min_x = min([a_x, b_x])
                max_x = max([a_x, b_x])
                for x in range(min_x, max_x+1):
                    map[x][a_y] = "#"
            void = max([a_y, b_y, void])
    return map, void

SAND_MOVES = [(0, 1), (-1, 1), (1, 1)]

def get_move(map: dict[int, dict[int, str]], pos: tuple[int,int], floor: int = 0) -> Union[tuple[int,int], None]:
    for move in SAND_MOVES:
        np_x, np_y = sum_tup(pos, move)
        if map[np_x][np_y] == "." and np_y != floor:
            return np_x, np_y
    return None            

def drop_sand(map: dict[int, dict[int, str]], void: int) -> int:
    sand_count = 1

    while True:
        pos = (500, 0)
        new_pos = get_move(map, pos)
        while new_pos:
            pos = new_pos
            if pos[1] > void:
                return sand_count
            new_pos = get_move(map, pos)                

        map[pos[0]][pos[1]] = "O"
        sand_count += 1

def drop_sand_2(map: dict[int, dict[int, str]], void: int) -> int:
    sand_count = 1

    while True:
        pos = (500, 0)
        new_pos = get_move(map, pos, void + 2)
        if not new_pos:
            return sand_count
        while new_pos:
            pos = new_pos
            new_pos = get_move(map, pos, void+2)                

        map[pos[0]][pos[1]] = "O"
        sand_count += 1

def part1(input: list[str]) -> int:
    cave_map, void = generate_map(input)
    return drop_sand(cave_map, void)

def part2(input: list[str]) -> int:
    cave_map, void = generate_map(input)
    return drop_sand_2(cave_map, void)

if __name__ == '__main__':
    with open(INPUT) as f:
        data = f.read().splitlines()
        sand_count = part1(data)
        print(f"Part1: number of sand units before void: {sand_count-1}")
        sand_count = part2(data)
        print(f"Part2: number of sand units before block: {sand_count}")