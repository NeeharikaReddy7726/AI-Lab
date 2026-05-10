import itertools
import time

letters = ('S','E','N','D','M','O','R','Y') # Variables
digits = range(10) # Domain

start = time.time()
count = 0

for perm in itertools.permutations(digits, 8):
    count += 1

    S, E, N, D, M, O, R, Y = perm

    # Leading digit constraint
    if S == 0 or M == 0:
        continue

    send = 1000*S + 100*E + 10*N + D
    more = 1000*M + 100*O + 10*R + E
    money = 10000*M + 1000*O + 100*N + 10*E + Y

    if send + more == money:
        end = time.time()

        print("Solution Found:\n")
        print(f"S={S}, E={E}, N={N}, D={D}")
        print(f"M={M}, O={O}, R={R}, Y={Y}")
        print(f"\nSEND = {send}")
        print(f"MORE = {more}")
        print(f"MONEY = {money}")

        print(f"\nCandidates Checked: {count}")
        print(f"⏱ Time Taken: {end - start:.4f} seconds")
        break