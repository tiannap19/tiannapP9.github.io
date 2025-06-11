
"""
Tianna Perez
Project Variation #11 

Improvements:
- Created functions for logical groupings
- Made a function to draw multiple at a time
- created utility functions
- grouped realted functions to be more logical
- added comments
- I added clouds to show enhancement
"""

import turtle
import math

# Constants
DEFAULT_SPEED = 0
DEFAULT_TITLE = "Turtle Graphics Assignment"
FILL_COLOR_DEFAULT = "blue"

# Setup Functions
def setup_turtle():
    """Initialize turtle with standard settings"""
    t = turtle.Turtle()
    t.speed(DEFAULT_SPEED)
    screen = turtle.Screen()
    screen.title(DEFAULT_TITLE)
    return t, screen

# Fill Helpers
def start_fill(t, fill_color):
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()

def end_fill(t, fill_color):
    if fill_color:
        t.end_fill()

# Shape Functions
def draw_rectangle(t, width, height, fill_color=None):
    start_fill(t, fill_color)
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    end_fill(t, fill_color)

def draw_circle(t, radius, fill_color=None):
    start_fill(t, fill_color)
    t.circle(radius)
    end_fill(t, fill_color)

def draw_polygon(t, length, sides, fill_color=None):
    start_fill(t, fill_color)
    for _ in range(sides):
        t.forward(length)
        t.left(360 / sides)
    end_fill(t, fill_color)

def draw_arc_segment(t, radius, angle):
    arc_length = 2 * math.pi * radius * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    for _ in range(n):
        t.forward(step_length)
        t.left(step_angle)

def draw_scene(t):
    screen = t.getscreen()
    screen.bgcolor("lightblue")

def jump_to(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


def draw_house(t):
    jump_to(t, -80, -120)
    draw_rectangle(t, 150, 250, "white")

def draw_roofs(t):
    jump_to(t, -80, -180)
    draw_polygon(t, 150, 3)

    jump_to(t, -80, -50)
    draw_polygon(t, 150, 3)

    jump_to(t, -150, -85)
    draw_polygon(t, 150, 3)

    jump_to(t, -10, -85)
    draw_polygon(t, 150, 3)

def draw_sun(t):
    jump_to(t, 200, 200)
    draw_circle(t, 50, "white")


# constants
CLOUD_POSITIONS = [(-210, 200), (-150, 210,), (-80, 200)]
ROOF_POSITIONS = [(-80, -180), (-80, -50), (-150, -85), (-10, -85)]
GROUND_RECTANGLES = [(-400, -200), (70, -200)]
RECT_SIZE = (320, 150)


def draw_roof(t, x, y, size=150, sides=3):
    """Draw a single polygonal roof at (x, y)."""
    jump_to(t, x, y)
    draw_polygon(t, size, sides)

def draw_all_roofs(t):
    """Draw all roofs using predefined positions."""
    for x, y in ROOF_POSITIONS:
        draw_roof(t, x, y)

def draw_cloud(t, x, y, radius=50, color="grey"):
    """Draw a single cloud at (x, y)."""
    jump_to(t, x, y)
    draw_circle(t, radius, color)

def draw_all_clouds(t):
    """Draw all clouds using predefined positions."""
    for x, y in CLOUD_POSITIONS:
        draw_cloud(t, x, y)   

def draw_ground(t):
    """Draw the ground rectangles."""
    for x, y in GROUND_RECTANGLES:
        jump_to(t, x, y)
        draw_rectangle(t, *RECT_SIZE, "yellow")

def draw_scene(t):
    """Compose the full scene using helper components."""
    screen = t.getscreen()
    screen.bgcolor("lightblue")

def main():
    t, screen = setup_turtle()
    draw_scene(t)
    draw_house(t)
    draw_all_clouds(t)
    draw_all_roofs(t)
    draw_ground(t)
    draw_sun(t)
    screen.mainloop()

turtle.done

if __name__ == "__main__":
    main()
    