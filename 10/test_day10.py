import day10

def test_part1():
    with open("10/10_p1_test.txt") as f:
        data = f.read().splitlines()
        assert day10.day10(data) == 13140