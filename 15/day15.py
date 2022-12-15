import re

INPUT = "15/15.txt"

# find points within row which are seen by each sensor
def part1(input: list[str], row: int) -> int:
    seen = set()
    beacons = set()

    for line in input:
        sx, sy, bx, by = [int(m) for m in re.findall("[xy]=([-\d]+)", line)]
        
        if by == row:
            beacons.add(bx)

        # calculate manhattan distance to extremeties of line visible to sensor
        md_beacon = abs(sx - bx) + abs(sy - by)
        md_row = md_beacon - abs(row - sy)

        # mark range visible to sensor as seen
        for x in range(sx - md_row, sx + md_row + 1):
            seen.add(x)

    return len(seen - beacons)



def part2(input: list[str], max_row: int) -> int:
    sensors = set()

    for line in input:
        sx, sy, bx, by = [int(m) for m in re.findall("[xy]=([-\d]+)", line)]

        md_beacon = abs(sx - bx) + abs(sy - by)
        sensors.add((sx, sy, md_beacon))

    def seen(x, y):
        for sx, sy, d in sensors:
            if (abs(sx-x) + abs(sy-y)) <= d:
                return True

        return False


    for sx, sy, md in sensors:
        # check every point around each edge of each sensor range
        for dx in range(md+2):
            dy = (md+1)-dx
            for x,y in [(sx-dx,sy-dy),(sx-dx,sy+dy),(sx+dx,sy-dy),(sx+dx,sy+dy)]:
                if not(0<=x<=max_row and 0<=y<=max_row):
                    continue
                # check if in another sensor's array
                if not seen(x,y):
                    return x*4000000 + y


if __name__ == '__main__':
    with open(INPUT) as f:
        data = f.read().splitlines()
        beacon_pos = part1(data, 2000000)
        print(f"Part1: number of positions which can't be beacon: {beacon_pos}")
        print(f"Part2: beacon tuning frequency: {part2(data, 4000000)}")
        
