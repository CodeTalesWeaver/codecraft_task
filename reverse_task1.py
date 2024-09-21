# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 14:36:52 2024

@author: gupta
"""

# Function to insert element at the bottom of the stack
def insert_at_bottom(stack, item):
    if not stack:
        stack.append(item)
    else:
        temp = stack.pop()
        insert_at_bottom(stack, item)
        stack.append(temp)

# Function to reverse the stack
def reverse_stack(stack):
    if stack:
        temp = stack.pop()
        reverse_stack(stack)
        insert_at_bottom(stack, temp)

# Example usage
stack = [1, 2, 3, 4, 5]
reverse_stack(stack)
print(stack)  # Output: [5, 4, 3, 2, 1]
