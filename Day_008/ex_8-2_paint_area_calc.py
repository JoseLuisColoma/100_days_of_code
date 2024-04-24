import math


def paint_calc(**kwargs):
    global height, width, cover
    for key, value in kwargs.items():
        if key == "height":
            height = value
        elif key == "width":
            width = value
        elif key == "cover":
            cover = value
    cans = math.ceil(height * width / cover)
    print(f"You'll need {cans} cans of paint.")


test_h = int(input())
test_w = int(input())
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
