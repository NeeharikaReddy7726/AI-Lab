# Graph Coloring with Forward Checking

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

# Initial domains
domains = {node: colors.copy() for node in graph}

coloring = {}
assignment_count = 0


def forward_check(node, color, domains):
    """Remove color from neighbors' domains"""
    new_domains = {n: domains[n].copy() for n in domains}

    for neighbor in graph[node]:
        if neighbor not in coloring:
            if color in new_domains[neighbor]:
                new_domains[neighbor].remove(color)

            # Failure: domain becomes empty
            if not new_domains[neighbor]:
                return None

    return new_domains


def solve(domains):
    global assignment_count

    if len(coloring) == len(graph):
        return True

    # Select unassigned node
    for node in graph:
        if node not in coloring:

            for color in domains[node]:
                assignment_count += 1
                print(f"\nTrying: {node} → {color}")

                # Apply forward checking
                new_domains = forward_check(node, color, domains)

                if new_domains is not None:
                    coloring[node] = color
                    print(f"Assigned: {node} → {color}")

                    # Print domain sizes
                    print("Domain sizes after assignment:")
                    for n in new_domains:
                        if n not in coloring:
                            print(f"{n}: {len(new_domains[n])} -> {new_domains[n]}")

                    if solve(new_domains):
                        return True

                    # Backtrack
                    print(f"Backtracking on: {node} → {color}")
                    del coloring[node]

                else:
                    print(f"Rejected: {node} → {color} (domain wipeout)")

            return False

    return False


# Run
if solve(domains):
    print("\nFinal Coloring:\n")
    for state in coloring:
        print(f"{state} → {coloring[state]}")

    print(f"\n Total Assignments Tried (Forward Checking): {assignment_count}")
else:
    print("No solution exists")