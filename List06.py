def main(fruits):
    """
    Given a list called Fruits, it contains at least one apple. Find how many apples are on the list and return.
    Args:
        fruits(list): parameter
    Returns:
        int: return answer
    """
    i = 0
    sum = 0
    while i < len(fruits):
        if fruits[i] == "apple":
            sum += 1
        i += 1
    return sum
print(main(["apple", "banana", "apple", "apple", "apple"]))