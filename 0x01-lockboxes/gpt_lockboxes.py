#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determine if all the boxes can be opened.

    Args:
        boxes (list): A list of lists representing the boxes and their corresponding keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    num_boxes = len(boxes)
    unlocked = [False] * num_boxes  # Track the unlocked status of each box
    unlocked[0] = True  # The first box is unlocked

    # Iterate through the keys in each box
    for box_num, keys in enumerate(boxes):
        if unlocked[box_num]:
            # Mark all the boxes that can be opened by the current box
            for key in keys:
                if key < num_boxes:
                    unlocked[key] = True

    # Check if all boxes are unlocked
    return all(unlocked)

if __name__ == '__main__':
    print(canUnlockAll([[1, 4, 5], [2], [5, 2], [3], [4, 1], [3, 5]]))
    print(canUnlockAll([[4, 6], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]))

