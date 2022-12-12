INPUT = "12/12.txt"

def get_edges(node, map):
    nx, ny = node
    possible = [(nx, ny+1), (nx, ny-1), (nx+1, ny), (nx-1, ny)]
    edges = []
    for px, py in possible:
        if px >= len(map) or px < 0 or py >= len(map[0]) or py < 0:
            continue

        diff = ord(map[px][py]) - ord(map[nx][ny])
        if diff < 2:
            edges.append((px,py))
    return edges

def bfs(map, origin, goal):
    visited = []
    queue = []
    parent = {}

    queue.append(origin)
    while len(queue) > 0:
        n = queue.pop(0)
        if n == goal:
            break
        for edge in get_edges(n, map):
            if edge not in visited:
                visited.append(edge)
                parent[edge] = n
                queue.append(edge)

    if goal not in visited:
        return 2000

    count = 0
    current = goal
    while current != origin:
        count += 1
        current = parent[current]
    
    return count

def part1(input: list[str]):
    input = [[char for char in row] for row in input]
    start = (0,0)
    end = (0,0)
    for x,row in enumerate(input):
        for y,char in enumerate(row):
            if char == "S":
                start = (x,y)
                input[x][y] = "a"
            elif char == "E":
                end = (x,y)
                input[x][y] = "z"

    return bfs(input, start, end)

def part2(input: list[str]):
    input = [[char for char in row] for row in input]
    starts = []
    end = (0,0)
    for x,row in enumerate(input):
        for y,char in enumerate(row):
            if char == "S" or char == "a":
                starts.append((x,y))
                input[x][y] = "a"
            elif char == "E":
                end = (x,y)
                input[x][y] = "z"

    counts = []
    total_starts = len(starts)
    for i,start in enumerate(starts):
        print(f"Searching from start {i} of {total_starts}")
        counts.append(bfs(input, start, end))

    return min(counts)

if __name__ == '__main__':
    with open(INPUT) as f:
        data = f.read().splitlines()
        shortest_dist = part1(data)
        print(f"Shortest distance to E: {shortest_dist}")
        shortest_route = part2(data)
        print(f"Shortest route to E from a: {shortest_route}")