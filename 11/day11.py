from math import floor
import re

INPUT = "11/11.txt"

class Monkey:
    def __init__(self, data: list[str]):
        self.items = [int(item) for item in data[0].split(": ")[1].split(", ")]
        self.operation = data[1].split("= ")[1]
        self.test_divisor = int(re.match("^.+divisible by (\d+)$", data[2]).groups()[0])
        self.action_true = int(re.match("^.+throw to monkey (\d+)$", data[3]).groups()[0])
        self.action_false = int(re.match("^.+throw to monkey (\d+)$", data[4]).groups()[0])
        self.inspect_count = 0

def day11(monkey_data: list[str], part2: bool = False) -> int:
    monkeys = {}
    for data in monkey_data:
        data = data.splitlines()
        monkey_id = int(re.match("Monkey (\d+):", data[0]).groups()[0])
        monkeys[monkey_id] = Monkey(data[1:])

    product_divisors = 1
    for monkey in monkeys.values():
        product_divisors *= monkey.test_divisor

    for _ in range(10000 if part2 else 20):
        for monkey in monkeys.values():
            while len(monkey.items) > 0:
                item = monkey.items.pop(0)
                worry = eval(monkey.operation, {"old": item})
                monkey.inspect_count += 1

                if part2: 
                    worry %= product_divisors
                else:
                    worry = floor(worry / 3)
                

                if worry % monkey.test_divisor == 0:
                    monkeys[monkey.action_true].items.append(worry)
                else:
                    monkeys[monkey.action_false].items.append(worry)

    inspector_rankings = [monkey.inspect_count for monkey in monkeys.values()]
    inspector_rankings.sort(reverse=True)
    return inspector_rankings[0] * inspector_rankings[1]


if __name__ == '__main__':
    with open(INPUT) as f:
        data = f.read().split("\n\n")
        monkey_business = day11(data)
        print(f"Monkey business after 20 rounds: {monkey_business}")
        monkey_business = day11(data, True)
        print(f"Monkey business after 10000 rounds: {monkey_business}")
