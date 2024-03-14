#!/usr/bin/python3
"""
Module for solving the lockboxes problem.
"""


def can_open_all_boxes(locks):
    """
    Determines if all the boxes can be opened.

    Args:
        locks (list of lists): A list of lists representing the locked boxes.
            Each box may contain keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not locks:
        return False

    visited = [False] * len(locks)
    visited[0] = True
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        for key in locks[current_box]:
            if key < len(locks) and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)


if __name__ == "__main__":
    # Example usage
    locks1 = [[1], [2], [3], [4], []]
    print(can_open_all_boxes(locks1))  # Output: True

    locks2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(can_open_all_boxes(locks2))  # Output: True

    locks3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(can_open_all_boxes(locks3))  # Output: False

