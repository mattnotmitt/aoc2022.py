from collections import defaultdict
import re

INPUT = "5/5.txt"

def load_stacks(stacks_raw: list[str]) -> dict[int,list]:
    stacks = defaultdict(list)
    stack_level = -2
    while stack_level >= 0 - len(stacks_raw):
        for n in range (1, len(stacks_raw[stack_level]), 4):
            if stacks_raw[stack_level][n].isalpha():
                stacks[int(n/4+1)].append(stacks_raw[stack_level][n])
        stack_level = stack_level - 1
    return stacks
        

def part1(data: str) -> str:
    stack_data,instructions = [sub.splitlines() for sub in data.split("\n\n")]
    stacks = load_stacks(stack_data)
    for line in instructions:
        # move 2 from 4 to 9
        count, src, dest = re.match("move (\d+) from (\d+) to (\d+)", line).groups()
        for _ in range(0, int(count)):
            crate = stacks[int(src)].pop()
            stacks[int(dest)].append(crate)
    return "".join([stack[-1] for stack in stacks.values()])

def part2(data: str) -> str:
    stack_data,instructions = [sub.splitlines() for sub in data.split("\n\n")]
    stacks = load_stacks(stack_data)
    for line in instructions:
        # move 2 from 4 to 9
        count, src, dest = re.match("move (\d+) from (\d+) to (\d+)", line).groups()
        moving = stacks[int(src)][0-int(count):]
        stacks[int(src)] = stacks[int(src)][:0-int(count)]
        stacks[int(dest)] += moving
    return "".join([stack[-1] for stack in stacks.values()])

if __name__ == '__main__':
    with open(INPUT) as f:
        data = f.read()
        top_crates = part1(data)
        print(f"Part1: Top crates are {top_crates}")
        top_crates = part2(data)
        print(f"Part2: Top crates are {top_crates}")
