import json
from typing import Union
from functools import cmp_to_key

INPUT = "13/13.txt"

def normalise(lval, rval):
    if type(lval) is list and type(rval) is int:
        return (lval, [rval])
    elif type(rval) is list and type(lval) is int:
        return ([lval], rval)
    return (lval,rval)


def compare(left: list[Union[list, int]], right: list[Union[list, int]]) -> bool:
    lctr, rctr = 0, 0

    while True:
        if lctr == len(left) and rctr != len(right):
            return True
        elif rctr == len(right) and lctr != len(left):
            return False
        elif lctr == len(left) and rctr == len(right):
            return None 

        lval, rval = normalise(left[lctr], right[rctr])
        if type(lval) is int:
            if lval > rval:
                return False
            elif rval > lval:
                return True

        elif type(lval) is list:
            ret_compare = compare(lval, rval)
            if ret_compare != None:
                return ret_compare
        lctr += 1
        rctr += 1

    return None

def compare_wrapper(left, right) -> int:
    compare_ret = compare(left, right)
    if compare_ret is None:
        return 0
    elif compare_ret is False:
        return 1
    elif compare_ret is True:
        return -1

def part1(input: str):
    count = 0
    for i, pair in enumerate(input.split("\n\n")):
        [left_str, right_str] = pair.splitlines()
        if compare(json.loads(left_str), json.loads(right_str)):
            count += (i + 1)
    return count

def part2(input: str):
    input_lists = [json.loads(line) for line in input.splitlines() if len(line) > 0]
    input_lists.append([[2]])
    input_lists.append([[6]])
    input_lists.sort(key=cmp_to_key(compare_wrapper))
        
    return (input_lists.index([[2]]) + 1) * (input_lists.index([[6]]) + 1)

if __name__ == '__main__':
    with open(INPUT) as f:
        data = f.read()
        indices_sum = part1(data)
        print(f"Part1: sum of indices of good pairs: {indices_sum}")
        indices_product = part2(data)
        print(f"Part2: product of indices of divider packets {indices_product}")