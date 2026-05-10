import itertools

def NOT(p):
    return not p

def AND(p, q):
    return p and q

def OR(p, q):
    return p or q

def IMPLIES(p, q):
    return (not p) or q

def BICONDITIONAL(p, q):
    return p == q

# Truth Table Generator

def generate_values(variables):
    return list(itertools.product([False, True], repeat=len(variables)))


def print_table(variables, func, name):
    print("\nExpression:", name)
    print(" | ".join(variables), "| Result")
    print("-" * (len(variables) * 4 + 10))

    for values in generate_values(variables):
        env = dict(zip(variables, values))
        result = func(**env)
        row = " | ".join(['T' if v else 'F' for v in values])
        print(row, "|", 'T' if result else 'F')

# Expression

# 1. ~P -> Q
def expr1(P, Q):
    return IMPLIES(NOT(P), Q)

# 2. ~P ∧ ~Q
def expr2(P, Q):
    return AND(NOT(P), NOT(Q))

# 3. ~P ∨ ~Q
def expr3(P, Q):
    return OR(NOT(P), NOT(Q))

# 4. ~P -> Q
def expr4(P, Q):
    return IMPLIES(NOT(P), Q)

# 5. ~P <-> Q
def expr5(P, Q):
    return BICONDITIONAL(NOT(P), Q)

# 6. (P ∨ Q) ∧ (~P -> Q)
def expr6(P, Q):
    return AND(OR(P, Q), IMPLIES(NOT(P), Q))

# 7. (P ∨ Q) -> R
def expr7(P, Q, R):
    return IMPLIES(OR(P, Q), R)

# 8. ((P ∨ Q) -> R) <-> ((~P ∧ ~Q) -> ~R)
def expr8(P, Q, R):
    left = IMPLIES(OR(P, Q), R)
    right = IMPLIES(AND(NOT(P), NOT(Q)), NOT(R))
    return BICONDITIONAL(left, right)

# 9. ((P -> Q) ∧ (Q -> R)) -> (Q -> R)
def expr9(P, Q, R):
    left = AND(IMPLIES(P, Q), IMPLIES(Q, R))
    right = IMPLIES(Q, R)
    return IMPLIES(left, right)

# 10. (P -> (Q ∨ R)) -> (~P ∧ ~Q ∧ ~R)
def expr10(P, Q, R):
    left = IMPLIES(P, OR(Q, R))
    right = AND(NOT(P), AND(NOT(Q), NOT(R)))
    return IMPLIES(left, right)

#Truth Table

print_table(['P', 'Q'], expr1, "~P -> Q")
print_table(['P', 'Q'], expr2, "~P ∧ ~Q")
print_table(['P', 'Q'], expr3, "~P ∨ ~Q")
print_table(['P', 'Q'], expr4, "~P -> Q")
print_table(['P', 'Q'], expr5, "~P <-> Q")

print_table(['P', 'Q'], expr6, "(P ∨ Q) ∧ (~P -> Q)")

print_table(['P', 'Q', 'R'], expr7, "(P ∨ Q) -> R")
print_table(['P', 'Q', 'R'], expr8, "((P ∨ Q)->R) <-> ((~P ∧ ~Q)->~R)")
print_table(['P', 'Q', 'R'], expr9, "((P->Q) ∧ (Q->R)) -> (Q->R)")
print_table(['P', 'Q', 'R'], expr10, "(P->(Q∨R)) -> (~P ∧ ~Q ∧ ~R)")