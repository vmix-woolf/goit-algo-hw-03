import turtle


def draw_koch_segment(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        draw_koch_segment(t, length, level - 1)
        t.left(60)
        draw_koch_segment(t, length, level - 1)
        t.right(120)
        draw_koch_segment(t, length, level - 1)
        t.left(60)
        draw_koch_segment(t, length, level - 1)


def draw_koch_snowflake(t, length, level):
    for _ in range(3):
        draw_koch_segment(t, length, level)
        t.right(120)


def main():
    level = int(input("Enter recursion level (0 or more): "))

    screen = turtle.Screen()
    screen.setup(800, 800)
    screen.bgcolor("white")
    screen.title("Сніжинка Коха")

    t = turtle.Turtle()
    t.speed(0)  # max speed
    t.penup()
    t.goto(-200, 100)  # initial point
    t.pendown()

    draw_koch_snowflake(t, 400, level)

    t.hideturtle()
    screen.mainloop()


if __name__ == "__main__":
    main()
