INPUT = "12/12.txt"

def get_edges(node, map):
    nx, ny = node
    possible = [(nx, ny+1), (nx, ny-1), (nx+1, ny), (nx-1, ny)]
    edges = []
    for px, py in possible:
        if px >= len(map) or px < 0 or py >= len(map[0]) or py < 0:
            continue

        diff = ord(map[nx][ny]) - ord(map[px][py])
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

    return parent

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

    graph = bfs(input, end, start)

    count = 0
    current = start
    while current != end:
        count += 1
        current = graph[current]

    return count

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

    graph = bfs(input, end, (-1,-1)) # oob, generate whole graph

    counts = []
    for start in starts:
        if start not in graph.values():
            continue

        count = 0
        current = start
        while current != end:
            count += 1
            current = graph[current]
        counts.append(count)

    return min(counts)

if __name__ == '__main__':
    with open(INPUT) as f:
        data = f.read().splitlines()
        shortest_dist = part1(data)
        print(f"Shortest distance to E: {shortest_dist}")
        shortest_route = part2(data)
        print(f"Shortest route to E from a: {shortest_route}")