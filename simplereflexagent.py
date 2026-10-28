def vacuum_agent(location, status):
    if status == "Dirty":
        return "Suck"

    elif location == "A":
        return "Move Right"

    elif location == "B":
        return "Move Left"


# Test cases
print(vacuum_agent("A", "Dirty"))
print(vacuum_agent("A", "Clean"))
print(vacuum_agent("B", "Dirty"))
print(vacuum_agent("B", "Clean"))