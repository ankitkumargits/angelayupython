print("Paint area calculator.")
import math

def paint_calc(height, width, coverage):
    area = height * width
    num_of_cans = math.ceil(area / coverage)
    print(f"You'll need {num_of_cans} cans to paint")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))

coverage = 5

paint_calc(height=test_h, width=test_w, coverage=coverage)
