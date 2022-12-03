INPUT = "3/3.txt"

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def find_common_item(backpack: str) -> str:
    comp_size = int(len(backpack) / 2)
    comp_a = set(backpack[:comp_size])
    comp_b = list(backpack[comp_size:])
    common = list(comp_a.intersection(comp_b))
    return common[0]

def score_item(item: str) -> int:
    ascii_code = ord(item)
    if ascii_code >= 65 and ascii_code < 91:
        return ascii_code - 38
    if ascii_code >= 97 and ascii_code < 123:
        return ascii_code - 96

def part1(lines: list[str]) -> int:
    priority = 0
    for line in lines:
        priority += score_item(find_common_item(line))

    return priority

def find_badge(group: list[str]) -> int:
    common = list(set(group[0]).intersection(list(group[1])).intersection(list(group[2])))
    return common[0]

def part2(lines: list[str]) -> int:
    priority = 0
    for group in chunks(lines, 3):
        priority += score_item(find_badge(group))

    return priority

if __name__ == '__main__':
    with open(INPUT) as f:
        lines = f.read().splitlines()
        priority = part1(lines)
        print(f"Part1: Total priority is {priority}")
        priority = part2(lines)
        print(f"Part2: Total badge priority is {priority}")
