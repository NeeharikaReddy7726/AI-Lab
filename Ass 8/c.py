
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

#  Domains 
domains = {}
for j in jobs:
    domains[j] = [t for t in TIME if t + jobs[j]["dur"] - 1 <= jobs[j]["deadline"]]

print("Before AC-3:")
for j in domains:
    print(j, ":", len(domains[j]))

# AC-3
from collections import deque

def consistent(xi, x, xj, y):
    # precedence: xi depends on xj
    if xj in jobs[xi]["deps"]:
        return x > y + jobs[xj]["dur"] - 1
    return True

def revise(xi, xj):
    removed = False
    for x in domains[xi][:]:
        if not any(consistent(xi, x, xj, y) for y in domains[xj]):
            domains[xi].remove(x)
            removed = True
    return removed

def ac3():
    queue = deque()
    for xi in jobs:
        for xj in jobs[xi]["deps"]:
            queue.append((xi, xj))

    while queue:
        xi, xj = queue.popleft()
        if revise(xi, xj):
            for xk in jobs:
                if xi in jobs[xk]["deps"]:
                    queue.append((xk, xi))

ac3()

print("\nAfter AC-3:")
for j in domains:
    print(j, ":", len(domains[j]))


count_plain = 0
count_ac3 = 0

#constraints
def valid(assign):
    # concurrency
    timeline = {t: 0 for t in TIME}
    for j, s in assign.items():
        for t in range(s, s + jobs[j]["dur"]):
            timeline[t] += 1
            if timeline[t] > MAX:
                return False

    # precedence
    for j in assign:
        for d in jobs[j]["deps"]:
            if d not in assign:
                return False
            if assign[j] <= assign[d] + jobs[d]["dur"] - 1:
                return False
    return True


def backtrack(assign, i, use_ac3):
    global count_plain, count_ac3

    if i == len(ORDER):
        return assign

    job = ORDER[i]
    values = domains[job] if use_ac3 else TIME

    for s in values:
        if use_ac3:
            count_ac3 += 1
        else:
            count_plain += 1

        assign[job] = s

        if valid(assign):
            res = backtrack(assign, i + 1, use_ac3)
            if res:
                return res

        del assign[job]

    return None


backtrack({}, 0, False)
backtrack({}, 0, True)

print("\nAssignments tried (without AC-3):", count_plain)
print("Assignments tried (with AC-3):", count_ac3)