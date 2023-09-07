from graphics import *

def draw_pikachu(win):
    # Create a yellow circle for the face
    face = Circle(Point(100, 100), 50)
    face.setFill("yellow")
    face.draw(win)

    # Create black oval eyes
    left_eye = Oval(Point(85, 85), Point(95, 95))
    left_eye.setFill("black")
    left_eye.draw(win)

    right_eye = Oval(Point(105, 85), Point(115, 95))
    right_eye.setFill("black")
    right_eye.draw(win)

    # Create a smile
    smile = Line(Point(85, 110), Point(115, 110))
    smile.setWidth(2)
    smile.draw(win)

    # Create red rosy cheeks
    left_cheek = Circle(Point(80, 120), 10)
    left_cheek.setFill("red")
    left_cheek.draw(win)

    right_cheek = Circle(Point(120, 120), 10)
    right_cheek.setFill("red")
    right_cheek.draw(win)

    torso = Rectangle(Point(100, 100), 10)
    torso.setfill("yellow")
    torso.draw(win)

# Create a graphics window
win = GraphWin("Pikachu", 200, 200)

# Call the draw_pikachu function to draw the Pikachu image
draw_pikachu(win)

# Wait for the user to close the window
win.mainloop()
