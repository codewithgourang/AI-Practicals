import heapq

def heuristic(state, goal):
    distance = 0
    for i in range(9):
        if state[i] != 0:
            j = goal.index(state[i])
            distance += abs(i // 3 - j // 3) + abs(i % 3 - j % 3)
    return distance

def get_neighbors(state):
    neighbors = []
    zero = state.index(0)
    row, col = zero // 3, zero % 3

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        r, c = row + dr, col + dc
        if 0 <= r < 3 and 0 <= c < 3:
            new_state = list(state)
            new_zero = r * 3 + c
            new_state[zero], new_state[new_zero] = \
                new_state[new_zero], new_state[zero]
            neighbors.append(tuple(new_state))

    return neighbors

def a_star(start, goal):
    pq = []
    heapq.heappush(pq, (heuristic(start, goal), 0, start, [start]))
    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if state == goal:
            return path

        if state in visited:
            continue
        visited.add(state)

        for next_state in get_neighbors(state):
            if next_state not in visited:
                new_g = g + 1
                new_f = new_g + heuristic(next_state, goal)
                heapq.heappush(
                    pq, (new_f, new_g, next_state, path + [next_state])
                )

def display(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

start = (1, 2, 3, 0, 4, 6, 7, 5, 8)
goal  = (1, 2, 3, 4, 5, 6, 7, 8, 0)

solution = a_star(start, goal)

print("A* Search - 8 Puzzle")
print("Number of moves:", len(solution) - 1)
print()

for i, state in enumerate(solution):
    print("Step", i)
    display(state)