import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r') as f:
    lines = f.read().strip().split('\n')

n = int(lines[0].split(',')[0])

start_str, goal_str = lines[1].split(';')
start = tuple(map(int, start_str.split(',')))
goal = tuple(map(int, goal_str.split(',')))

obstacles = set()
for item in lines[2].split(';'):
    obstacles.add(tuple(map(int, item.split(','))))

strategy = lines[3].strip()

print(n, start, goal, obstacles, strategy)

out = open(output_file, 'w')

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def neighbors(pos, n, obstacles):
    x, y = pos
    moves = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
    valid = []

    for nx, ny in moves:
        if 1 <= nx <= n and 1 <= ny <= n and (nx,ny) not in obstacles:
            valid.append((nx,ny))

    return valid

import heapq

def gbfs(n, start, goal, obstacles):
    pq = []
    heapq.heappush(pq, (heuristic(start, goal), start))

    visited = set()
    cost = 0

    while pq:
        _, current = heapq.heappop(pq)

        if current in visited:
            continue

        visited.add(current)
        out.write(str(current) + "\n")

        if current == goal:
            out.write("Total cost: " + str(cost))
            return

        for nb in neighbors(current, n, obstacles):
            if nb not in visited:
                heapq.heappush(pq, (heuristic(nb, goal), nb))

        cost += 1

def astar(n, start, goal, obstacles):
    pq = []
    heapq.heappush(pq, (heuristic(start, goal), start))

    visited = set()
    g_cost = {start: 0}

    while pq:
        _, current = heapq.heappop(pq)

        if current in visited:
            continue

        visited.add(current)
        out.write(str(current) + "\n")

        if current == goal:
            out.write("Total cost: " + str(g_cost[current]))
            return

        for nb in neighbors(current, n, obstacles):
            new_cost = g_cost[current] + 1

            if nb not in g_cost or new_cost < g_cost[nb]:
                g_cost[nb] = new_cost
                f = new_cost + heuristic(nb, goal)
                heapq.heappush(pq, (f, nb))

if strategy == "gbfs":
    gbfs(n, start, goal, obstacles)
elif strategy == "astar":
    astar(n, start, goal, obstacles)

out.close()
