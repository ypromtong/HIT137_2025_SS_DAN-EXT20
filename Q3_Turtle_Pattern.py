import turtle


def pattern_edge(length: float, depth: int):
    """
    Depth 0: straight line
    Depth 1+: split into 3, replace middle with two sides of inward equilateral triangle
    Inward indentation turns: Right 60, Left 120, Right 60 (instead of outward)
    """
    if depth == 0:
        turtle.forward(length)
        return

    seg = length / 3.0
    pattern_edge(seg, depth - 1)
    turtle.right(60)
    pattern_edge(seg, depth - 1)
    turtle.left(120)
    pattern_edge(seg, depth - 1)
    turtle.right(60)
    pattern_edge(seg, depth - 1)


def draw_pattern_polygon(sides: int, side_length: float, depth: int):
    angle = 360 / sides
    for _ in range(sides):
        pattern_edge(side_length, depth)
        turtle.left(angle)


def get_int(prompt: str, min_val=None):
    while True:
        try:
            x = int(input(prompt))
            if min_val is not None and x < min_val:
                print(f"Please enter a number >= {min_val}")
                continue
            return x
        except ValueError:
            print("Please enter a whole number (integer).")


def get_float(prompt: str, min_val=None):
    while True:
        try:
            x = float(input(prompt))
            if min_val is not None and x <= min_val:
                print(f"Please enter a number > {min_val}")
                continue
            return x
        except ValueError:
            print("Please enter a number.")


def main():
    print("Q3 - Recursive Turtle Pattern")
    sides = get_int("Enter the number of sides: ", min_val=3)
    side_length = get_float("Enter the side length (pixels): ", min_val=0)
    depth = get_int("Enter the recursion depth: ", min_val=0)

    turtle.speed(0)
    turtle.hideturtle()

    # Move to a nicer starting position
    turtle.penup()
    turtle.goto(-side_length / 2, side_length / 3)
    turtle.pendown()

    draw_pattern_polygon(sides, side_length, depth)

    turtle.done()


if __name__ == "__main__":
    main()
