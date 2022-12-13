import day13

def test_day13():
    with open("13/test_day13_data.txt") as f:
        data = f.read()
        assert day13.part1(data) == 13
        assert day13.part2(data) == 140