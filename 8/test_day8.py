import day8

TEST_INPUT_P1 = [
    "30373",
    "25512",
    "65332",
    "33549",
    "35390",
]

def test_day8():
    assert day8.part1(TEST_INPUT_P1) == 21
    assert day8.part2(TEST_INPUT_P1) == 8