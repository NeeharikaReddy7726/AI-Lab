jobs = {
    "J1": {"dur": 2, "deadline": 8, "deps": []},
    "J2": {"dur": 3, "deadline": 10, "deps": ["J1"]},
    "J3": {"dur": 1, "deadline": 6, "deps": []},
    "J4": {"dur": 4, "deadline": 12, "deps": ["J2", "J3"]},
    "J5": {"dur": 2, "deadline": 9, "deps": ["J1"]},
    "J6": {"dur": 3, "deadline": 15, "deps": ["J4", "J5"]},
}

TIME = list(range(1, 16))
ORDER = ["J1", "J2", "J3", "J5", "J4", "J6"]
MAX = 2


def deadline_ok(job, start):
    return start + jobs[job]["dur"] - 1 <= jobs[job]["deadline"]


def precedence_ok(job, start, assign):
    for d in jobs[job]["deps"]:
        if d not in assign:
            return False
        if start <= assign[d] + jobs[d]["dur"] - 1:
            return False
    return True


def concurrency_ok(assign):
    count = {t: 0 for t in TIME}
    for j, s in assign.items():
        for t in range(s, s + jobs[j]["dur"]):
            count[t] += 1
            if count[t] > MAX:
                return False
    return True


def backtrack(assign, i):
    if i == len(ORDER):
        return assign

    job = ORDER[i]

    for s in TIME:
        print("Trying:", job, "=", s)
        assign[job] = s

        if (deadline_ok(job, s) and
            precedence_ok(job, s, assign) and
            concurrency_ok(assign)):

            print("Valid:", assign)
            res = backtrack(assign, i + 1)
            if res:
                return res

        print("Backtrack from", job)
        del assign[job]

    return None


def gantt(sol):
    print("\nTime :", end=" ")
    for t in TIME:
        print(f"{t:2}", end=" ")
    print()

    for j in jobs:
        print(f"{j:3}  :", end=" ")
        s = sol[j]
        for t in TIME:
            if s <= t < s + jobs[j]["dur"]:
                print(" X", end=" ")
            else:
                print(" .", end=" ")
        print()


solution = backtrack({}, 0)

if solution:
    print("\nFinal Schedule:", solution)
    gantt(solution)
else:
    print("No solution")