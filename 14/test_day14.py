import day14

TEST_INPUT_P1 = [
    "498,4 -> 498,6 -> 496,6",
    "503,4 -> 502,4 -> 502,9 -> 494,9"
]

def test_day14():
    assert day14.part1(TEST_INPUT_P1) == 25
    assert day14.part2(TEST_INPUT_P1) == 93