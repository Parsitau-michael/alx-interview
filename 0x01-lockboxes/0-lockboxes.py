#!/usr/bin/python3
"""
This module contains a function to determine if all boxes in a list can be
unlocked. Each box contains keys to other boxes, and we start with the first
box unlocked. The goal is to check if we can unlock all boxes using the keys
found within them.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked starting from box 0.
    
    Parameters:
    - boxes (list of lists): A list where each index represents a box,
     and each box contains a list of keys to other boxes.
     Each key is a positive integer corresponding to a box number.
    
    Returns:
    - bool: True if all boxes can be opened, otherwise False.
    
    Logic:
    - Begin with the first box (index 0) unlocked.
    - Explore each box’s keys iteratively, adding new boxes unlocked to a set.
    - Continue exploring new boxes until no further boxes can be unlocked.
    - Finally, compare the number of unlocked boxes with the total number
     of boxes.
    """

    openedBoxes = {0}
    boxes_to_check =[0]

    while boxes_to_check:
        current_box = boxes_to_check.pop()
        for key in boxes[current_box]:
            if not key in openedBoxes and key < len(boxes):
                openedBoxes.add(key)
                boxes_to_check.append(key)
    
    return len(openedBoxes) == len(boxes)
