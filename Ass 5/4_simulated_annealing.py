import random
import math
import time
import matplotlib.pyplot as plt


# ---------------- HEURISTIC ----------------
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


# ---------------- RANDOM STATE ----------------
def random_state(N):
    return [random.randint(0, N - 1) for _ in range(N)]


# ---------------- RANDOM NEIGHBOR ----------------
def random_neighbor(state):
    N = len(state)
    row = random.randint(0, N - 1)
    col = random.randint(0, N - 1)

    new_state = state[:]
    new_state[row] = col
    return new_state


# ---------------- SIMULATED ANNEALING ----------------
def simulated_annealing(N, T0, alpha, schedule="exp", max_iter=10000):
    state = random_state(N)
    T = T0

    temps = []
    heuristics = []

    for t in range(1, max_iter + 1):
        current_h = heuristic(state)
        temps.append(T)
        heuristics.append(current_h)

        if current_h == 0:
            return state, temps, heuristics, True

        neighbor = random_neighbor(state)
        new_h = heuristic(neighbor)

        deltaE = new_h - current_h

        if deltaE < 0:
            state = neighbor
        else:
            prob = math.exp(-deltaE / T) if T > 0 else 0
            if random.random() < prob:
                state = neighbor

        # cooling schedules
        if schedule == "exp":
            T *= alpha
        elif schedule == "linear":
            T = T0 - 0.1 * t
        elif schedule == "log":
            T = T0 / math.log(t + 2)

        if T <= 0:
            break

    return state, temps, heuristics, False


# ---------------- MAIN ----------------
N = int(input("Enter N: "))
T0 = float(input("Initial Temperature: "))
alpha = float(input("Cooling rate (alpha): "))
schedule = input("Schedule (exp/linear/log): ")

start = time.time()
solution, temps, hs, success = simulated_annealing(N, T0, alpha, schedule)
end = time.time()

print("\nSolution:", solution)
print("Heuristic:", heuristic(solution))
print("Success:", success)
print("Execution time:", end - start)

# Plot temperature vs heuristic
plt.plot(temps, hs)
plt.xlabel("Temperature")
plt.ylabel("Heuristic")
plt.title("Temperature vs Heuristic")
plt.show()
