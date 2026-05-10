maze = []

for _ in range(5):
    row = list(map(int, input().split()))
    maze.append(row)

start = None
rewards = []
obstacles = set()

for i in range(5):
    for j in range(5):
        if maze[i][j] == 2:        # start
            start = (i, j)
        elif maze[i][j] == 1:      # reward
            rewards.append((i, j))
        elif maze[i][j] == 3:      # obstacle
            obstacles.add((i, j))

print("Start:", start)
print("Rewards:", rewards)
print("Obstacles:", obstacles)

out = open("out_astar.txt", "w")


def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


# choose farthest reward
goal = max(rewards, key=lambda r: heuristic(start, r))
print("Chosen reward:", (goal[0]+1, goal[1]+1))



def neighbors(pos):
    x, y = pos
    moves = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
    valid = []

    for nx, ny in moves:
        if 0 <= nx < 5 and 0 <= ny < 5 and (nx,ny) not in obstacles:
            valid.append((nx,ny))

    return valid


import heapq

def astar(start, goal):
    pq = []
    heapq.heappush(pq, (heuristic(start, goal), start))

    visited = set()
    g_cost = {start:0}

    while pq:
        _, current = heapq.heappop(pq)

        if current in visited:
            continue

        visited.add(current)
        out.write(str((current[0]+1, current[1]+1)) + "\n")


        if current == goal:
            out.write("Steps: " + str(g_cost[current]))
            return

        for nb in neighbors(current):
            new_cost = g_cost[current] + 1

            if nb not in g_cost or new_cost < g_cost[nb]:
                g_cost[nb] = new_cost
                f = new_cost + heuristic(nb, goal)
                heapq.heappush(pq, (f, nb))


astar(start, goal)
out.close()
