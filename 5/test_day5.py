import day5

TEST_DATA_P1 = """\
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

def test_part1():
    assert day5.part1(TEST_DATA_P1) == "CMZ"

def test_part2():
    assert day5.part2(TEST_DATA_P1) == "MCD"