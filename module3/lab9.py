"""
Your task is to write a program which reads the number of blocks the builders have, and outputs the height of the pyramid that can be built using these blocks.
The height is measured by the number of fully completed layers - if the builders don't have a sufficient number of blocks and cannot complete the next layer, they finish their work immediately. Important : each lower layer contains one block more than the layer above.
"""

blocks = int(input("Enter the number of blocks: "))
height = 0
in_layer = 1
while in_layer <= blocks:
    height += 1
    blocks -= in_layer
    in_layer += 1
print("The height of the pyramid:", height)