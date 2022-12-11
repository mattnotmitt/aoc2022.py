import day10

def test_part1():
    with open("10/test_day10_data.txt") as f:
        data = f.read().splitlines()
        assert day10.day10(data) == 13140