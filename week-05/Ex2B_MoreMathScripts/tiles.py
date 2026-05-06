# 5. You are going to tile a room whose dimensions are length by width feet. There are
# twelve tiles per box, each 1 foot by 1 foot. How many boxes of tiles do you need? You
# can only buy full boxes, not a partial box.
# You also want to buy at least 10% more tiles than you need in order to handle chips,
# breakage, and mess-ups. How many total boxes will you buy?
import math
length = 10
width = 10
area = length * width
tiles_per_box = 12

tiles_needed = length * width * 1.10


boxes_needed = math.ceil(tiles_needed / tiles_per_box)

print(f'you need {boxes_needed} boxes of tiles')