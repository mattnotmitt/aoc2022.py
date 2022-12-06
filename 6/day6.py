INPUT = "6/6.txt"

def part1(signal: str) -> int:
    for i, char in enumerate(signal):
        if len(set(signal[i:i+4])) == 4:
            return i+4

def part2(signal: str) -> int:
    for i, char in enumerate(signal):
        if len(set(signal[i:i+14])) == 14:
            return i+14

if __name__ == '__main__':
    with open(INPUT) as f:
        filestr = f.read()
        print(f"First start-of-packet signal arrives after {part1(filestr)} characters")
        print(f"First start-of-message signal arrives after {part2(filestr)} characters")