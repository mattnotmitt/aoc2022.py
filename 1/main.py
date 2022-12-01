INPUT = "1.txt"

def day1(filestr: str):
    elflines = filestr.split("\n\n")
    per_elf_data = list(map(lambda t: list(map(lambda n: int(n), t.splitlines())), elflines))

    per_elf_sum = [sum(elf) for elf in per_elf_data]
    per_elf_sum.sort(reverse=True)
    
    print(f"Max number of calories: {per_elf_sum[0]}")
    print(f"Total calories top 3 elves: {per_elf_sum[0] + per_elf_sum[1] + per_elf_sum[2]}")

if __name__ == '__main__':
    with open(INPUT) as f:
        filestr = f.read()
        day1(filestr)