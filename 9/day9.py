from itertools import repeat

INPUT = "9/9.txt"

MOVE_DIRS = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
T_MOVES = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

def sum_tup(a,b):
    return tuple(sum(x) for x in zip(a, b))

def best_t_move(h_pos, t_pos):
    hx, hy = h_pos
    tx, ty = t_pos

    if abs(hx - tx) <= 1 and abs(hy - ty) <= 1:
        return t_pos

    best_move = (0,0)
    best_dist = 100

    for mx, my in T_MOVES:
        m_tx = tx + mx
        m_ty = ty + my
        # should this be chebyshev distance? yes. I am simply too lazy to import scipy
        distance = abs(hx - m_tx) + abs(hy - m_ty)
        if distance < best_dist:
            best_dist = distance
            best_move = (m_tx, m_ty)

    return best_move

def part1(moves: list[str]) -> int:
    visited = set()
    visited.add((0,0))

    h_pos, t_pos = (0,0), (0,0)

    for move in moves:
        [m, count] = move.split()
        t_dir = MOVE_DIRS[m]
        for _ in range(int(count)):
            h_pos = sum_tup(h_pos, t_dir)
            t_pos = best_t_move(h_pos, t_pos)
            visited.add(t_pos)

    return len(list(visited))

def part2(moves: list[str]) -> int:
    KNOTS = 10
    knot_pos = [(0,0) for _ in range(KNOTS)]

    visited = set()
    visited.add((0,0))

    h_pos = (0,0)

    for move in moves:
        [m, count] = move.split()
        t_dir = MOVE_DIRS[m]
        for _ in range(int(count)):
            h_pos = knot_pos[0] = sum_tup(h_pos, t_dir)
            for k in range(1, KNOTS):
                knot_pos[k] = best_t_move(knot_pos[k-1], knot_pos[k])
            
            visited.add(knot_pos[-1])

    return len(list(visited))

if __name__ == '__main__':
    with open(INPUT) as f:
        data = f.read().splitlines()
        total_visited = part1(data)
        print(f"Part1: total number of points H visited is {total_visited}")
        total_visited = part2(data)
        print(f"Part2: total number of points knot 9 visited is {total_visited}")