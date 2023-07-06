#!/usr/bin/python3
"""A module for working with the Locked Boxes problem
"""


def canUnlockAll(boxes):
    """determines if all the boxes can be opened."""
    locked_boxes = [False] * len(boxes)
    locked_boxes[0] = True
    for box in boxes:
        for key in box:
            if key == boxes.index(box) and locked_boxes[key] == False:
                locked_boxes[key] = False
            elif key >= 0 and key < len(boxes):
                locked_boxes[key] = True
            else:
                locked_boxes[key] = False

    return all(locked_boxes)


"""
def canUnlockAll(boxes):
    n = len(boxes)  # Total number of boxes
    unlocked = [False] * n  # List to keep track of the unlocked boxes
    unlocked[0] = True  # The first box is already unlocked
    stack = [0]  # Stack to store the boxes to be checked

    while stack:
        current_box = stack.pop()  # Get the next box to be checked
        for key in boxes[current_box]:  # Iterate through the keys in the current box
            if (
                key < n and not unlocked[key]
            ):  # Check if the key is valid and the box is not already unlocked
                unlocked[key] = True  # Unlock the box
                stack.append(key)  # Add the box to the stack for further exploration

    return all(unlocked)  # Return True if all boxes are unlocked, else False

"""
