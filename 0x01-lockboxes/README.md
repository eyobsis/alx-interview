# Lockboxes Problem

This project contains a Python script to solve the lockboxes problem. Given a set of locked boxes, each containing keys to other boxes, the script determines if all boxes can be opened.

## Problem Description

You have `n` number of locked boxes in front of you. Each box is numbered sequentially from 0 to `n - 1`, and each box may contain keys to the other boxes. A key with the same number as a box opens that box. You can assume all keys will be positive integers, and there can be keys that do not have boxes. The first box, `boxes[0]`, is always unlocked. The task is to write a function that determines if all the boxes can be opened.

## Usage

The function `canUnlockAll(boxes)` takes a list of lists `boxes` as input, where each inner list represents a box and contains keys to other boxes. It returns `True` if all boxes can be opened, and `False` otherwise.

Example usage:

```python
boxes1 = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes1))  # Output: True

boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes2))  # Output: True

boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes3))  # Output: False
# Lockboxes Problem

This project contains a Python script to solve the lockboxes problem. Given a set of locked boxes, each containing keys to other boxes, the script determines if all boxes can be opened.

## Problem Description

You have `n` number of locked boxes in front of you. Each box is numbered sequentially from 0 to `n - 1`, and each box may contain keys to the other boxes. A key with the same number as a box opens that box. You can assume all keys will be positive integers, and there can be keys that do not have boxes. The first box, `boxes[0]`, is always unlocked. The task is to write a function that determines if all the boxes can be opened.

## Usage

The function `canUnlockAll(boxes)` takes a list of lists `boxes` as input, where each inner list represents a box and contains keys to other boxes. It returns `True` if all boxes can be opened, and `False` otherwise.

Example usage:

```python
boxes1 = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes1))  # Output: True

boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes2))  # Output: True

boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes3))  # Output: False

