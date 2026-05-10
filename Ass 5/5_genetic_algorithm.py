import random

# ---------- HEURISTIC ----------
def heuristic(state):
    h = 0
    N = len(state)
    for i in range(N):
        for j in range(i + 1, N):
            if abs(i - j) == abs(state[i] - state[j]):
                h += 1
    return h


def fitness(state):
    N = len(state)
    return (N * (N - 1) // 2) - heuristic(state)


# ---------- POPULATION ----------
def create_population(size, N):
    pop = []
    for _ in range(size):
        s = list(range(N))
        random.shuffle(s)
        pop.append(s)
    return pop


# ---------- SELECTION ----------
def roulette_selection(pop):
    total = sum(fitness(p) for p in pop)
    r = random.uniform(0, total)
    s = 0
    for p in pop:
        s += fitness(p)
        if s >= r:
            return p


def tournament_selection(pop, k=3):
    chosen = random.sample(pop, k)
    chosen.sort(key=fitness, reverse=True)
    return chosen[0]


def rank_selection(pop):
    ranked = sorted(pop, key=fitness)
    return random.choice(ranked[len(pop)//2:])


# ---------- CROSSOVER ----------
def single_point(p1, p2):
    N = len(p1)
    point = random.randint(1, N - 2)
    child = p1[:point] + p2[point:]
    return repair(child)


def two_point(p1, p2):
    N = len(p1)
    a, b = sorted(random.sample(range(N), 2))
    child = p1[:a] + p2[a:b] + p1[b:]
    return repair(child)


def repair(child):
    N = len(child)
    missing = [x for x in range(N) if x not in child]
    seen = set()
    for i in range(N):
        if child[i] in seen:
            child[i] = missing.pop()
        seen.add(child[i])
    return child


# ---------- MUTATION ----------
def swap_mutation(ch):
    i, j = random.sample(range(len(ch)), 2)
    ch[i], ch[j] = ch[j], ch[i]


def inversion_mutation(ch):
    i, j = sorted(random.sample(range(len(ch)), 2))
    ch[i:j] = reversed(ch[i:j])


def scramble_mutation(ch):
    i, j = sorted(random.sample(range(len(ch)), 2))
    sub = ch[i:j]
    random.shuffle(sub)
    ch[i:j] = sub


# ---------- GA ENGINE ----------
def GA(
    N,
    pop_size=100,
    generations=500,
    crossover_rate=0.8,
    mutation_rate=0.05,
    selection_method="tournament",
    crossover_method="single",
    mutation_method="swap"
):
    pop = create_population(pop_size, N)

    for gen in range(generations):
        pop.sort(key=fitness, reverse=True)

        if heuristic(pop[0]) == 0:
            print("Solution found at generation", gen)
            return pop[0]

        new_pop = pop[:2]  # elitism
        while len(new_pop) < pop_size:
            # selection
            if selection_method == "roulette":
                p1 = roulette_selection(pop)
                p2 = roulette_selection(pop)
            elif selection_method == "rank":
                p1 = rank_selection(pop)
                p2 = rank_selection(pop)
            else:
                p1 = tournament_selection(pop)
                p2 = tournament_selection(pop)

            # crossover
            if random.random() < crossover_rate:
                if crossover_method == "two":
                    child = two_point(p1, p2)
                else:
                    child = single_point(p1, p2)
            else:
                child = p1[:]

            # mutation
            if random.random() < mutation_rate:
                if mutation_method == "invert":
                    inversion_mutation(child)
                elif mutation_method == "scramble":
                    scramble_mutation(child)
                else:
                    swap_mutation(child)

            new_pop.append(child)

        pop = new_pop

    return pop[0]


# ---------- MAIN ----------
N = int(input("Enter N: "))

solution = GA(
    N,
    pop_size=100,
    generations=500,
    selection_method="tournament",
    crossover_method="single",
    mutation_method="swap"
)

print("Solution:", solution)
print("Conflicts:", heuristic(solution))
