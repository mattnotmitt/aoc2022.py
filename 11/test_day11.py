import day11

def test_part1():
    with open("11/test_day11_data.txt") as f:
        data = f.read().split("\n\n")
        assert day11.day11(data) == 10605