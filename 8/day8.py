from itertools import repeat

INPUT = "8/8.txt"

def transpose(lst: list[list]):
    return list(map(list, zip(*lst)))

def part1(lines: list[str]):
    grid_side = len(lines)

    default_vis_row = list(repeat(False, grid_side))
    default_vis_row[0] = True
    default_vis_row[-1] = True
    visible_grid = [list(default_vis_row) for _ in lines] 
    visible_grid[0] = list(repeat(True, grid_side))
    visible_grid[-1] = list(repeat(True, grid_side))

    grid = []

    for i,line in enumerate(lines):
        grid.append(list(map(int, line[::1])))
        # skip top and bottom row, they're all exposed
        if i == 0 or i == len(line):
            continue
        # search left to right
        lr_max = grid[i][0]
        for j, tree in enumerate(grid[i][1:-1]):
            if tree > lr_max:
                visible_grid[i][j+1] = True
                lr_max = tree
        # search right to left
        reverse_row = grid[i][::-1]
        rl_max = reverse_row[0]
        for j, tree in enumerate(reverse_row[1:-1]):
            if tree > rl_max:
                visible_grid[i][grid_side-2-j] = True
                rl_max = tree
    
    grid = transpose(grid)
    visible_grid = transpose(visible_grid)

    for i,line in enumerate(lines):
        grid.append(list(map(int, line[::1])))
        # skip top and bottom row, they're all exposed
        if i == 0 or i == len(line):
            continue
        # search left to right
        lr_max = grid[i][0]
        for j, tree in enumerate(grid[i][1:-1]):
            if tree > lr_max:
                visible_grid[i][j+1] = True
                lr_max = tree
        # search right to left
        reverse_row = grid[i][::-1]
        rl_max = reverse_row[0]
        for j, tree in enumerate(reverse_row[1:-1]):
            if tree > rl_max:
                visible_grid[i][grid_side-2-j] = True
                rl_max = tree

    return sum([1 if item else 0 for sublist in visible_grid for item in sublist])
    
def part2(lines: list[str]):
    grid_side = len(lines)
    visible_grid = [list(repeat(1, grid_side)) for _ in lines]
    
    grid = [list(map(int, line[::1])) for line in lines]
    
    for i,row in enumerate(grid):
        for j,tree in enumerate(row):
            for y in range(j+1, len(row)):
                if tree <= grid[i][y] or y == len(row)-1:
                    visible_grid[i][j] *= y-j
                    break
            for y in reversed(range(j)):
                if tree <= grid[i][y] or y == 0:
                    visible_grid[i][j] *= j-y
                    break
            for x in range(i+1, len(grid)):
                if tree <= grid[x][j] or x == len(grid)-1:
                    visible_grid[i][j] *= x-i
                    break
            for x in reversed(range(i)):
                if tree <= grid[x][j] or x == 0:
                    visible_grid[i][j] *= i-x
                    break

    remove_edge = [item if (a != 0 and a != grid_side-1 and b!=0 and b!=grid_side-1) else 0 for a,sublist in enumerate(visible_grid) for b,item in enumerate(sublist)]
    return max(remove_edge)


if __name__ == '__main__':
    with open(INPUT) as f:
        data = f.read().splitlines()
        visible_trees = part1(data)
        print(f"Part1: total small folder size is {visible_trees}")
        smallest_free = part2(data)
        print(f"Part2: Smallest folder which can free up enough space is {smallest_free}")