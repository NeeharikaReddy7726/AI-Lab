# Graph Coloring with MRV + Degree Heuristic + Forward Checking

graph = {
    "Rajasthan": ["Punjab", "Haryana", "UP", "MP", "Gujarat"],
    "Punjab": ["Rajasthan", "Haryana"],
    "Haryana": ["Rajasthan", "Punjab", "UP"],
    "UP": ["Rajasthan", "Haryana", "MP"],
    "MP": ["Rajasthan", "UP", "Gujarat", "Maharashtra"],
    "Gujarat": ["Rajasthan", "MP", "Maharashtra"],
    "Maharashtra": ["MP", "Gujarat", "Karnataka"],
    "Karnataka": ["Maharashtra"]
}

colors = ["Red", "Green", "Blue", "Yellow"]

domains = {node: colors.copy() for node in graph}
coloring = {}
assignment_count = 0


def forward_check(node, color, domains):
    new_domains = {n: domains[n].copy() for n in domains}

    for neighbor in graph[node]:
        if neighbor not in coloring:
            if color in new_domains[neighbor]:
                new_domains[neighbor].remove(color)

            if not new_domains[neighbor]:
                return None

    return new_domains


# MRV + Degree Heuristic
def select_unassigned_variable(domains):
    unassigned = [v for v in graph if v not in coloring]

    # MRV: minimum domain size
    min_domain = min(len(domains[v]) for v in unassigned)
    mrv_vars = [v for v in unassigned if len(domains[v]) == min_domain]

    if len(mrv_vars) == 1:
        return mrv_vars[0]

    # Degree heuristic (tie-breaker)
    def degree(var):
        return sum(1 for n in graph[var] if n not in coloring)

    return max(mrv_vars, key=degree)


def solve(domains):
    global assignment_count

    if len(coloring) == len(graph):
        return True

    node = select_unassigned_variable(domains)
    print(f"\nSelected Node (MRV+Degree): {node}")

    for color in domains[node]:
        assignment_count += 1
        print(f"Trying: {node} → {color}")

        new_domains = forward_check(node, color, domains)

        if new_domains is not None:
            coloring[node] = color
            print(f"Assigned: {node} → {color}")

            if solve(new_domains):
                return True

            print(f"Backtracking on: {node} → {color}")
            del coloring[node]

        else:
            print(f"Rejected: {node} → {color} (domain wipeout)")

    return False

if solve(domains):
    print("\n Final Coloring:\n")
    for state in coloring:
        print(f"{state} → {coloring[state]}")

    print(f"\nTotal Assignments Tried (MRV+Degree): {assignment_count}")
else:
    print("No solution exists")