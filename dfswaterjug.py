# DFS for Water Jug Problem

def dfs(a, b, target, visited, path):
    if (a, b) in visited:
        return False

    visited.add((a, b))
    path.append((a, b))

    if a == target or b == target:
        return True

    moves = [
        (5, b),                 # Fill Jug A
        (a, 3),                 # Fill Jug B
        (0, b),                 # Empty Jug A
        (a, 0),                 # Empty Jug B
        (max(0, a-(3-b)), min(3, a+b)),  # A -> B
        (min(5, a+b), max(0, b-(5-a)))   # B -> A
    ]

    for state in moves:
        if dfs(state[0], state[1], target, visited, path):
            return True

    path.pop()
    return False


# Jug capacities: 5L and 3L
# Target: 4L
visited = set()
path = []

if dfs(0, 0, 4, visited, path):
    print("Solution:")
    for state in path:
        print(state)
else:
    print("No solution")