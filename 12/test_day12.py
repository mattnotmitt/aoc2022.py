import day12

TEST_DATA_P1 = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""

def test_day12():
    data = TEST_DATA_P1.splitlines()
    assert day12.part1(data) == 31
    assert day12.part2(data) == 29