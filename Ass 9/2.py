
def goal_test(state):
    _, A, B = state
    return A == 'Clean' and B == 'Clean'


def actions(state):
    return ['SUCK', 'LEFT', 'RIGHT']


#ALL possible outcomes → AND node
def result(state, action):
    loc, A, B = state

    if action == 'SUCK':
        outcomes = []

        # If at A
        if loc == 'A':
            newA = 'Clean'
            outcomes.append(('A', newA, B))
            outcomes.append(('A', 'Clean', 'Clean'))

            if A == 'Clean':
                outcomes.append(('A', 'Dirty', B))

        # If at B
        elif loc == 'B':
            newB = 'Clean'
            outcomes.append(('B', A, newB))
            outcomes.append(('B', 'Clean', 'Clean'))

            if B == 'Clean':
                outcomes.append(('B', A, 'Dirty'))

        return outcomes

    elif action == 'LEFT':
        return [('A', A, B)]

    elif action == 'RIGHT':
        return [('B', A, B)]


# AND-OR SEARCH
def OR_SEARCH(state, path):
    if goal_test(state):
        return []
    if state in path:
        return None
    for action in actions(state):
        result_states = result(state, action)
        plan = AND_SEARCH(result_states, path + [state])

        if plan is not None:
            return [(action, plan)]

    return None

def AND_SEARCH(states, path):
    plans = []
    for s in states:
        plan = OR_SEARCH(s, path)
        if plan is None:
            return None
        plans.append(plan)
    return plans

def AND_OR_SEARCH(initial_state):
    return OR_SEARCH(initial_state, [])

initial_state = ('A', 'Dirty', 'Dirty')

plan = AND_OR_SEARCH(initial_state)

print("Plan:")
print(plan)