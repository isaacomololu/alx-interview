#!/usr/bin/python3
"""Defines function that determines if all boxes can be opened
   from a list of lists
"""


def canUnlockAll(boxes):
    """
    Determine if all the boxes can be opened.

    Args:
        boxes (list): A list of lists representing the boxes
        and their corresponding keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes:
        return False

    num_boxes = len(boxes)
    keys = boxes[0]  # Store the keys of the first box
    unlocked = [False] * num_boxes  # Track the unlocked status of each box

    unlocked[0] = True  # The first box is unlocked

    # Iterate through the boxes
    for box_idx in range(num_boxes):
        if not unlocked[box_idx]:
            continue

        # Check if the box can be unlocked
        for key in boxes[box_idx]:
            if key < num_boxes and not unlocked[key]:
                unlocked[key] = True  # Mark the box as unlocked
                # Add the keys in the box to the key list
                keys.extend(boxes[key])

    # Check if all boxes are unlocked
    return all(unlocked)