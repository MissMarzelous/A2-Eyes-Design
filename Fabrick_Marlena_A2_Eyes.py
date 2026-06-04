# PROGRAMMER:  Marlena Fabrick
# PROGRAM NAME: Turtle Graphics — Eyes Face Design
# DATE WRITTEN: September 20, 2020
# PURPOSE:      Uses Python turtle graphics to draw a face with
#               two layered eyes, a nose, and a mouth.

import turtle


def setup_screen():
    """Sets up the turtle screen."""
    screen = turtle.Screen()
    screen.bgcolor("green")
    screen.title("Eyes Face Design")
    return screen


def setup_pen():
    """Creates and configures the turtle pen."""
    pen = turtle.Turtle()
    pen.speed(10)
    pen.shape("turtle")
    pen.width(5)
    pen.pencolor("purple")
    return pen


def draw_circle(pen, x, y, radius, fill_color):
    """Draws a filled circle at the given screen position."""
    pen.fillcolor(fill_color)
    pen.begin_fill()
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.circle(radius)
    pen.end_fill()


def draw_eye(pen, x_offset):
    """Draws a layered eye (white, turquoise, black) at the given x offset."""
    draw_circle(pen, x_offset, -36, 100, "white")
    draw_circle(pen, x_offset, -18, 50,  "turquoise")
    draw_circle(pen, x_offset, -9,  25,  "black")


def draw_mouth(pen):
    """Draws a pink rectangular mouth."""
    pen.fillcolor("pink")
    pen.begin_fill()
    pen.penup()
    pen.goto(-160, -90)
    pen.pendown()
    pen.forward(300)
    pen.left(90)
    pen.forward(50)
    pen.left(90)
    pen.forward(300)
    pen.left(90)
    pen.forward(50)
    pen.left(90)
    pen.end_fill()


def main():
    setup_screen()
    pen = setup_pen()

    # Draw left and right eyes
    draw_eye(pen, -100)
    draw_eye(pen, 100)

    # Draw nose
    draw_circle(pen, 0, -5, 10, "red")

    # Draw mouth
    draw_mouth(pen)

    pen.hideturtle()
    turtle.done()


main()
