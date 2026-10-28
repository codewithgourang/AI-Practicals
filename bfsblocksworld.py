from collections import deque

def get_next_states(state):
    states = []

    for i in range(3):
        if not state[i]:
            continue

        for j in range(3):
            if i == j:
                continue

            new_state = [list(stack) for stack in state]
            block = new_state[i].pop()
            new_state[j].append(block)

            states.append(tuple(tuple(stack) for stack in new_state))

    return states


def bfs(start, goal):
    queue = deque([(start, [])])
    visited = {start}

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path + [state]

        for next_state in get_next_states(state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [state]))

    return None


# Initial and goal states
start = (("A", "B"), ("C",), ())
goal = (("A",), ("B", "C"), ())

solution = bfs(start, goal)

print("Blocks World using BFS")

if solution:
    for i, state in enumerate(solution):
        print("Step", i, ":", state)
else:
    print("No solution")