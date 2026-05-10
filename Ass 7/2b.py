import itertools

# ------------------ BRUTE FORCE ------------------
def brute_force():
    digits = range(10)
    count = 0

    for perm in itertools.permutations(digits, 8):
        count += 1

        S,E,N,D,M,O,R,Y = perm

        if S == 0 or M == 0:
            continue

        send = 1000*S + 100*E + 10*N + D
        more = 1000*M + 100*O + 10*R + E
        money = 10000*M + 1000*O + 100*N + 10*E + Y

        if send + more == money:
            return count  # stop when found

    return count


# BACKTRACKING + PROPAGATION 

letters = ['M','S','O','E','N','R','D','Y']
digits = list(range(10))

assignment = {}
used_digits = set()

nodes = 0


def is_safe(letter, digit):
    if digit in used_digits:
        return False
    if (letter == 'M' or letter == 'S') and digit == 0:
        return False
    return True


def check_partial():
    if all(k in assignment for k in ['D','E','Y']):
        if (assignment['D'] + assignment['E']) % 10 != assignment['Y']:
            return False

    if all(k in assignment for k in ['N','R','E']):
        if (assignment['N'] + assignment['R']) % 10 != assignment['E']:
            return False

    if all(k in assignment for k in ['E','O','N']):
        if (assignment['E'] + assignment['O']) % 10 != assignment['N']:
            return False

    if all(k in assignment for k in ['S','M','O']):
        if (assignment['S'] + assignment['M']) % 10 != assignment['O']:
            return False

    return True


def solve(index=0):
    global nodes

    if index == len(letters):
        return True

    letter = letters[index]

    for digit in digits:
        nodes += 1

        if is_safe(letter, digit):
            assignment[letter] = digit
            used_digits.add(digit)

            if check_partial():
                if solve(index + 1):
                    return True

            del assignment[letter]
            used_digits.remove(digit)

    return False


# ------------------ RUN BOTH ------------------

bf_count = brute_force()

solve()

# ------------------ PRINT COMPARISON ------------------

print("\n COMPARISON:\n")
print(f"Brute Force Candidates Checked: {bf_count}")
print(f"Backtracking Nodes Expanded: {nodes}")

improvement = bf_count / nodes if nodes != 0 else 0
print(f"Improvement Factor: {improvement:.2f}x faster")