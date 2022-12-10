from math import floor

INPUT = "10/10.txt"

SAMPLE_POINTS = [20, 60, 100, 140, 180, 220]

def print_display(display: list[list[str]]):
    print("\n".join(["".join(l) for l in display]))

def day10(instructions: list[str]) -> int:
    ip = 0
    signal_strengths = 0
    clock = 1
    x_reg = 1
    wait = 0
    action = 0

    display = [["." for _ in range(40)]  for _ in range(6)]

    while ip < len(instructions):
        col = (clock-1) % 40
        if col in [x_reg-1, x_reg, x_reg+1]:
            row = floor((clock-1) / 40)
            display[row][col] = "#"

        if wait > 0:
            wait -= 1
            if wait == 0:
                x_reg += action
        else:
            instr = instructions[ip]
            if instr.startswith("noop"):
                wait = 0
                action = 0
            elif instr.startswith("addx"):
                wait = 1
                action = int(instr.split(" ")[1])
            ip += 1        

        clock += 1

        if clock in SAMPLE_POINTS:
            signal_strengths += clock * x_reg

    print_display(display)
    return signal_strengths

if __name__ == '__main__':
    with open(INPUT) as f:
        data = f.read().splitlines()
        signal_strengths = day10(data)
        print(f"Part1: sum of signal strengths {signal_strengths}")
        # PART 2: RUAKHBEK
        # ###..#..#..##..#..#.#..#.###..####.#..#.
        # #..#.#..#.#..#.#.#..#..#.#..#.#....#.#..
        # #..#.#..#.#..#.##...####.###..###..##...
        # ###..#..#.####.#.#..#..#.#..#.#....#.#..
        # #.#..#..#.#..#.#.#..#..#.#..#.#....#.#..
        # #..#..##..#..#.#..#.#..#.###..####.#..#.
