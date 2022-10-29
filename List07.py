def main(list01):
    """
    A list of zeros and ones is given. Find how many zeros are involved and return.
    Args:
        list01(list): parameter
    Returns:
        int: return answer
    """
    i = 0
    zero = 0
    while i < len(list01):
        if list01[i] == 0:
            zero += 1
        i += 1
    return zero

print(main([1, 1, 0, 1, 1, 0, 1]))