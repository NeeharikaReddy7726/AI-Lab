import random
import time

def heuristic(state):
    h = 0
    N = len(state)

    for i in range(N):
        for j in range(i + 1, N):
            if state[i] == state[j]:
                h += 1
            elif abs(i - j) == abs(state[i] - state[j]):
                h += 1

    return h


def random_state(N):
    return [random.randint(0, N - 1) for _ in range(N)]


def simple_hill_climb(N):
    state = random_state(N)
    explored = 0

    while True:
        current_h = heuristic(state)
        if current_h == 0:
            return state, explored, True

        improved = False

        for row in range(N):
            for col in range(N):
                if col == state[row]:
                    continue

                neighbor = state[:]
                neighbor[row] = col
                explored += 1

                if heuristic(neighbor) < current_h:
                    state = neighbor
                    improved = True
                    break
            if improved:
                break

        if not improved:
            return state, explored, False


def steepest_hill_climb(N):
    state = random_state(N)
    explored = 0

    while True:
        current_h = heuristic(state)
        if current_h == 0:
            return state, explored, True

        best = state
        best_h = current_h

        for row in range(N):
            for col in range(N):
                if col == state[row]:
                    continue

                neighbor = state[:]
                neighbor[row] = col
                explored += 1

                h = heuristic(neighbor)
                if h < best_h:
                    best = neighbor
                    best_h = h

        if best_h >= current_h:
            return state, explored, False

        state = best


def random_restart(N):
    restarts = 0
    total_explored = 0

    while True:
        state, explored, success = steepest_hill_climb(N)
        total_explored += explored

        if success:
            return state, restarts, total_explored

        restarts += 1


N = int(input("Enter N: "))

print("\nRunning Random Restart Hill Climbing...")
start = time.time()
solution, restarts, explored = random_restart(N)
end = time.time()

print("Solution:", solution)
print("Restarts:", restarts)
print("States explored:", explored)
print("Execution time:", end - start)
