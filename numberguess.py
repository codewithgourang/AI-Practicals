# Intelligent Agent for Number Guessing
# Feedback: Higher / Lower / Correct

def intelligent_agent(low, high):
    print(f"Think of a number between {low} and {high}.")
    print("I will try to guess it!")

    attempts = 0

    while low <= high:
        # Intelligent guess using binary search
        guess = (low + high) // 2
        attempts += 1

        print(f"\nMy guess is: {guess}")
        feedback = input("Is it Higher, Lower, or Correct? ").lower()

        if feedback == "correct":
            print(f"\nI guessed the number {guess} correctly!")
            print(f"Number of attempts: {attempts}")
            return

        elif feedback == "higher":
            # Target number is higher than the guess
            low = guess + 1

        elif feedback == "lower":
            # Target number is lower than the guess
            high = guess - 1

        else:
            print("Invalid feedback! Please enter Higher, Lower, or Correct.")

    print("The feedback provided was inconsistent.")


# Start the intelligent agent
intelligent_agent(1, 100)