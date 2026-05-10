jobs = {
    "J1": {"dur": 2, "deadline": 8, "deps": []},
    "J2": {"dur": 3, "deadline": 10, "deps": ["J1"]},
    "J3": {"dur": 1, "deadline": 6, "deps": []},
    "J4": {"dur": 4, "deadline": 12, "deps": ["J2", "J3"]},
    "J5": {"dur": 2, "deadline": 9, "deps": ["J1"]},
    "J6": {"dur": 3, "deadline": 15, "deps": ["J4", "J5"]},
    "J7": {"dur": 3, "deadline": 10, "deps": ["J3"]},
}

TIME = list(range(1, 16))
ORDER = ["J1", "J2", "J3", "J5", "J4", "J7", "J6"]


def valid(assign, MAX):
    timeline = {t: 0 for t in TIME}

    for j, s in assign.items():
        for t in range(s, s + jobs[j]["dur"]):
            timeline[t] += 1
            if timeline[t] > MAX:
                return False

    for j in assign:
        for d in jobs[j]["deps"]:
            if d not in assign:
                return False
            if assign[j] <= assign[d] + jobs[d]["dur"] - 1:
                return False

    for j, s in assign.items():
        if s + jobs[j]["dur"] - 1 > jobs[j]["deadline"]:
            return False

    return True


def backtrack(assign, i, MAX):
    if i == len(ORDER):
        return assign

    job = ORDER[i]

    for s in TIME:
        # prevent overflow
        if s + jobs[job]["dur"] - 1 > jobs[job]["deadline"]:
            continue

        assign[job] = s

        if valid(assign, MAX):
            res = backtrack(assign, i + 1, MAX)
            if res:
                return res

        del assign[job]

    return None



print("Concurrency = 1")
sol1 = backtrack({}, 0, 1)
print("Solution:" if sol1 else "No solution", sol1)

print("\nConcurrency = 2")
sol2 = backtrack({}, 0, 2)
print("Solution:" if sol2 else "No solution", sol2)