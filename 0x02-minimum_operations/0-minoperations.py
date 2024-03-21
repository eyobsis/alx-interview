#!/usr/bin/python3
'''The minimum operations coding challenge.
'''


def minOperations(n):
    '''Computes the fewest number of operations needed to result
    in exactly n H characters.

    Args:
        n (int): The desired number of H characters.

    Returns:
        int: The minimum number of operations required.
    '''

    if n <= 1:
        return n

    operations = 0
    current_char_count = 1  # Start with one 'H' character

    while current_char_count < n:
        if n % current_char_count == 0:
            # Copy all characters and paste
            operations += 2
            current_char_count *= 2
        else:
            # Paste from clipboard
            operations += 1
            current_char_count += current_char_count

    return operations


if __name__ == "__main__":
    n = 4
    print("Min # of ops to reach {} char: {}".format(n, minOperations(n)))

    n = 12
    print("Min # of ops to reach {} char: {}".format(n, minOperations(n)))
