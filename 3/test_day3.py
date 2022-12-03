import day3

TEST_DATA_P1 = {
    "vJrwpWtwJgWrhcsFMMfFFhFp": "p",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL": "L",
    "PmmdzqPrVvPwwTWBwg": "P",
    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn": "v",
    "ttgJtRGJQctTZtZT": "t",
    "CrZsJsPPZsGzwwsLwLmpwMDw": "s"
}

TEST_DATA_P2 = [
    "vJrwpWtwJgWrhcsFMMfFFhFp",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    "PmmdzqPrVvPwwTWBwg"
]

def test_find_common_item():
    for backpack in TEST_DATA_P1.keys():
        assert day3.find_common_item(backpack) == TEST_DATA_P1[backpack]

def test_score_item():
    assert day3.score_item("a") == 1
    assert day3.score_item("z") == 26
    assert day3.score_item("A") == 27
    assert day3.score_item("Z") == 52

def test_find_badge():
    assert day3.find_badge(TEST_DATA_P2) == "r"