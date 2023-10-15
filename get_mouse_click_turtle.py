import turtle

# Function to get the position of the mouse click
def get_mouse_click_position(x, y):
    print(f"Clicked at position: ({x}, {y})")

# Set the screen size to 800x600
screen = turtle.Screen()
screen.setup(1000, 800)

# Bind the mouse click event to the function
screen.onclick(get_mouse_click_position)

# Keep the turtle window open
turtle.done()
