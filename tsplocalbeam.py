import random

# Distance matrix between cities
distance = [
    [0, 10, 15, 20, 25],
    [10, 0, 35, 25, 30],
    [15, 35, 0, 30, 20],
    [20, 25, 30, 0, 15],
    [25, 30, 20, 15, 0]
]

N = len(distance)


# Calculate total distance of a tour
def tour_cost(tour):
    cost = 0

    for i in range(N - 1):
        cost += distance[tour[i]][tour[i + 1]]

    # Return to starting city
    cost += distance[tour[-1]][tour[0]]

    return cost


# Generate neighboring tours by swapping two cities
def get_neighbors(tour):
    neighbors = []

    for i in range(1, N):
        for j in range(i + 1, N):
            new_tour = tour[:]
            new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
            neighbors.append(new_tour)

    return neighbors


# Local Beam Search
def local_beam_search(k=3, iterations=100):
    
    # Generate k random initial tours
    states = []

    for _ in range(k):
        tour = list(range(N))
        random.shuffle(tour)
        states.append(tour)

    best_tour = min(states, key=tour_cost)
    best_cost = tour_cost(best_tour)

    for _ in range(iterations):

        # Generate all successors
        candidates = []

        for tour in states:
            candidates.extend(get_neighbors(tour))

        # Remove duplicate tours
        unique = []
        seen = set()

        for tour in candidates:
            key = tuple(tour)

            if key not in seen:
                seen.add(key)
                unique.append(tour)

        # Select k best candidates
        unique.sort(key=tour_cost)
        states = unique[:k]

        # Update global best
        current_best = min(states, key=tour_cost)
        current_cost = tour_cost(current_best)

        if current_cost < best_cost:
            best_tour = current_best[:]
            best_cost = current_cost

    return best_tour, best_cost


# Run the algorithm
best_tour, best_cost = local_beam_search(k=3, iterations=100)

print("Best Tour:", [city + 1 for city in best_tour])
print("Minimum Distance:", best_cost)