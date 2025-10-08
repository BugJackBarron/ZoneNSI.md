import turtle
import math

def draw_pentagon(t, side_length):
    """Draws a pentagon with the given side length."""
    for _ in range(5):
        t.forward(side_length)
        t.left(72)

def draw_pentagram(t, side_length):
    """Draws a pentagram inscribed in a pentagon with the given side length."""
    # Calculate the distance between two non-adjacent vertices of the pentagon
    angle = math.radians(36)
    diagonal_length = 2 * side_length * math.sin(angle)
    
    # Move to the starting point of the pentagram
    t.penup()
    t.forward(side_length / 2)
    t.pendown()
    
    # Draw the pentagram
    for _ in range(5):
        t.forward(diagonal_length)
        t.right(144)

def main():
    # Setup turtle
    screen = turtle.Screen()
    screen.title("Pentagram in a Pentagon")
    t = turtle.Turtle()
    t.speed(3)
    
    # Side length of the pentagon
    side_length = 100
    
    # Draw the pentagon
    draw_pentagon(t, side_length)
    
    # Draw the pentagram
    t.penup()
    t.goto(0, 0)
    t.pendown()
    draw_pentagram(t, side_length)
    
    # Finish
    turtle.done()

if __name__ == "__main__":
    main()