import time

digits = set(range(10))

# used digits
used = set()

assign = {}

prune_counts = {
    "units": 0,
    "tens": 0,
    "hundreds": 0,
    "thousands": 0
}

node_count = 0


def solve():
    global node_count

    for D in digits:
        for E in digits - {D}:
            node_count += 1

            for Y in digits - {D, E}:
                # Units: D + E = Y + 10*C1
                total = D + E
                Y_calc = total % 10
                C1 = total // 10

                if Y != Y_calc:
                    prune_counts["units"] += 1
                    continue

                for N in digits - {D, E, Y}:
                    for R in digits - {D, E, Y, N}:
                        node_count += 1

                        # Tens: N + R + C1 = E + 10*C2
                        total = N + R + C1
                        if total % 10 != E:
                            prune_counts["tens"] += 1
                            continue

                        C2 = total // 10

                        for O in digits - {D, E, Y, N, R}:
                            node_count += 1

                            # Hundreds: E + O + C2 = N + 10*C3
                            total = E + O + C2
                            if total % 10 != N:
                                prune_counts["hundreds"] += 1
                                continue

                            C3 = total // 10

                            for S in digits - {D, E, Y, N, R, O}:
                                for M in digits - {D, E, Y, N, R, O, S}:
                                    node_count += 1

                                    # Leading constraint
                                    if S == 0 or M == 0:
                                        continue

                                    # Thousands: S + M + C3 = O + 10*C4
                                    total = S + M + C3
                                    if total % 10 != O:
                                        prune_counts["thousands"] += 1
                                        continue

                                    C4 = total // 10

                                    # Final constraint: C4 = M
                                    if C4 != M:
                                        continue

                                    # SUCCESS
                                    assign.update({
                                        'S': S, 'E': E, 'N': N, 'D': D,
                                        'M': M, 'O': O, 'R': R, 'Y': Y
                                    })
                                    return True

    return False

start = time.time()
solve()
end = time.time()

print("Solution:\n")
for k in assign:
    print(f"{k} = {assign[k]}")

print("\n Pruning Counts per Column:")
for k, v in prune_counts.items():
    print(f"{k}: {v}")

print(f"\nNodes Expanded: {node_count}")
print(f" Time Taken: {end - start:.4f} sec")