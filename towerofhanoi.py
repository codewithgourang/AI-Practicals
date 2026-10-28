# Tower of Hanoi using State Space Search
# State represents the positions of all disks on the three pegs.

def tower_of_hanoi(n, source, auxiliary, destination):
    # Base case: If only one disk remains, move it directly
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    # Move n-1 disks from source to auxiliary peg
    tower_of_hanoi(n - 1, source, destination, auxiliary)

    # Move the largest disk to the destination peg
    print(f"Move disk {n} from {source} to {destination}")

    # Move n-1 disks from auxiliary to destination peg
    tower_of_hanoi(n - 1, auxiliary, source, destination)


# Main program
n = int(input("Enter the number of disks: "))

print("\nSteps to solve Tower of Hanoi:")
tower_of_hanoi(n, 'A', 'B', 'C')

# Explanation:
# 1. A, B, and C represent the three pegs.
# 2. The initial state has all disks on peg A.
# 3. The goal state has all disks on peg C in the correct order.
# 4. A valid state transition moves one disk at a time.
# 5. A larger disk cannot be placed on a smaller disk.
# 6. The recursive function explores the sequence of valid moves
#    needed to reach the goal state.
# 7. The minimum number of moves required is 2^n - 1.
# 8. This recursive solution finds an optimal path through the
#    state space, although it does not explicitly store a search tree.