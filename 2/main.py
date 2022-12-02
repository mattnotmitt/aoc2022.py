INPUT = "2.txt"

CHOICE_MAP = {
    "A": "R",
    "B": "P",
    "C": "S",
    "X": "R",
    "Y": "P",
    "Z": "S"
}

SCORE_MAP = {
    "R": 1,
    "P": 2,
    "S": 3
}

WIN_MAP = {
    "R": "P",
    "P": "S",
    "S": "R"
}

LOSE_MAP = {
    "R": "S",
    "P": "R",
    "S": "P"
}

# BAD SOLUTION HATE THIS

def round_score(player, opponent) -> int:
    if player == opponent:
        return 3
    if (player == "R" and opponent == "S") \
        or (player == "P" and opponent == "R") \
        or (player == "S" and opponent == "P"):
        return 6
    return 0

def player_choice(player_outcome, opponent) -> str:
    if player_outcome == "X":
        return LOSE_MAP[opponent]
    if player_outcome == "Y":
        return opponent
    return WIN_MAP[opponent]

def part1(lines: list[str]) -> int:
    score_sum = 0
    for line in lines:
        opponent, player = [CHOICE_MAP[choice] for choice in line.split(" ")]
        score_sum += SCORE_MAP[player] + round_score(player, opponent)

    return score_sum

def part2(lines: list[str]) -> int:
    score_sum = 0
    for line in lines:
        opponent, player_outcome = line.split(" ")
        opponent = CHOICE_MAP[opponent]
        player = player_choice(player_outcome, opponent)
        score_sum += SCORE_MAP[player] + round_score(player, opponent)

    return score_sum

if __name__ == '__main__':
    with open(INPUT) as f:
        filestr = f.read().splitlines()
        score_sum = part1(filestr)
        print(f"Part1: Total score is {score_sum}")
        score_sum = part2(filestr)
        print(f"Part2: Total score is {score_sum}")
