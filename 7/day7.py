from __future__ import annotations
from dataclasses import dataclass, field
from collections import defaultdict
import re
import sys

sys.setrecursionlimit(100)

INPUT = "7/7.txt"

@dataclass
class Directory:
    name: str = ""
    parent: str = ""
    subdirectories: list[str] = field(default_factory=list)
    files: dict[str, int] = field(default_factory=dict)
    size: int = 0

def load_dirs(lines) -> list[Directory]:
    dirs = defaultdict(Directory)
    in_ls = False
    most_recent_dir = ""

    def parse_command(line: str):
        nonlocal in_ls
        nonlocal most_recent_dir

        if line.startswith("$ cd"):
            new_dir = re.match("\$ cd (.+)", line).groups()[0]
            if new_dir == "..":
                most_recent_dir = dirs[most_recent_dir].parent
            else:
                name = f"{most_recent_dir}/{new_dir}"
                dirs[name].name = name
                dirs[name].parent = most_recent_dir
                most_recent_dir = name
        elif line.startswith("$ ls"):
            in_ls = True

    def handle_ls(line: str):
        nonlocal in_ls

        filesize_matches = re.match("(\d+) (\w+)", line)

        if line.startswith("$"):
            in_ls = False
            parse_command(line)
        elif line.startswith("dir"):
            dirs[most_recent_dir].subdirectories.append(re.match("dir (\w+)", line).groups()[0])
        elif filesize_matches:
            size, name = filesize_matches.groups()
            dirs[most_recent_dir].files[name] = int(size)
            dirs[most_recent_dir].size += int(size)
            

    for line in lines:
        if in_ls:
            handle_ls(line)
        else:
            parse_command(line)

    return dirs

def part1(dirs: dict[str,Directory]) -> int:
    def directory_size(dir: Directory):
        return dir.size + sum([directory_size(dirs[f"{dir.name}/{subdir}"]) for subdir in dir.subdirectories])

    total_big_size = 0
    for dir in list(dirs.values()):
        size = directory_size(dir)
        if size <= 100000:
            total_big_size += size

    return total_big_size

def part2(dirs: dict[str,Directory]) -> int:
    def directory_size(dir: Directory):
        return dir.size + sum([directory_size(dirs[f"{dir.name}/{subdir}"]) for subdir in dir.subdirectories])

    remaining = 70000000 - directory_size(dirs["//"])
    needed = 30000000 - remaining
    closest = 30000000

    for dir in list(dirs.values()):
        size = directory_size(dir)
        if size > needed:
            if size < closest:
                closest = size

    return closest


if __name__ == '__main__':
    with open(INPUT) as f:
        data = f.read().splitlines()
        dirs = load_dirs(data)
        total_small_folders = part1(dirs)
        print(f"Part1: total small folder size is {total_small_folders}")
        smallest_free = part2(dirs)
        print(f"Part2: Smallest folder which can free up enough space is {smallest_free}")