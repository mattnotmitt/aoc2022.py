INPUT = "4/4.txt"

def parse_pair(line: str) -> ((int,int), (int,int)):
    range1, range2 = line.split(",")
    r1l,r1h = [int(val) for val in range1.split("-")]
    r2l,r2h = [int(val) for val in range2.split("-")]
    return (r1l,r1h),(r2l,r2h)

def part1(lines: list[str]) -> int:
    encompass_count = 0
    for line in lines:
        (r1l,r1h),(r2l,r2h) = parse_pair(line)
        if (r1l <= r2l and r1h >= r2h) or (r2l <= r1l and r2h >= r1h):
            encompass_count += 1

    return encompass_count

def part2(lines: list[str]) -> int:
    overlap_count = 0
    for line in lines:
        (r1l,r1h),(r2l,r2h) = parse_pair(line)
        if not any([r1l > r2h, r2l > r1h]):
            overlap_count += 1

    return overlap_count

if __name__ == '__main__':
    with open(INPUT) as f:
        lines = f.read().splitlines()
        count = part1(lines)
        print(f"Part1: Total number of fully contained pairs is {count}") # 547
        overlap_count = part2(lines)
        print(f"Part2: Total number of overlapped pairs is {overlap_count}") # 843
