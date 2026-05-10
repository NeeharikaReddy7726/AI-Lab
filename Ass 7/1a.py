# Graph Coloring using Backtracking with tracing

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

colors = ["Red", "Green", "Blue", "Yellow"] # Domain

coloring = {}
assignment_count = 0  # Count total attempts


def is_safe(node, color):
    for neighbor in graph[node]:
        if neighbor in coloring and coloring[neighbor] == color:
            return False
    return True


def solve():
    global assignment_count

    if len(coloring) == len(graph):
        return True

    for node in graph:
        if node not in coloring:
            for color in colors:
                assignment_count += 1
                print(f"Trying: {node} → {color}")

                if is_safe(node, color):
                    coloring[node] = color
                    print(f"Assigned: {node} → {color}\n")

                    if solve():
                        return True

                    # Backtracking
                    print(f"Backtracking on: {node} → {color}\n")
                    del coloring[node]

                else:
                    print(f"Rejected: {node} → {color} (constraint violated)\n")

            return False

    return False


if solve():
    print("\nFinal Coloring:\n")
    for state in coloring:
        print(f"{state} → {coloring[state]}")

    print(f"\n🔢 Total Assignments Tried: {assignment_count}")
else:
    print("No solution exists")