# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500
    
    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas,  scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    draw_sea(canvas, scene_width, scene_height)
    draw_sun(canvas, scene_width, scene_height)
    draw_grid(canvas, scene_width, scene_height, 25)
    draw_house(canvas, scene_width, scene_height)
    draw_clouds(canvas, scene_width, scene_height)
    draw_flower(canvas, scene_width, scene_height)
    
    

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_grid(canvas, width, height, interval):

    # draw vertical lines
    label_y = 15
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height, fill="black")
        draw_text(canvas, x, label_y, f"{x}", fill="black")
    
    # draw horizontal lines
    label_x = 15
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y, fill="black")
        draw_text(canvas, label_x, y, f"{y}", fill="black")


def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, scene_height / 3,
        scene_width, scene_height, width=0, fill="sky blue")


    

def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 3, width=0, fill="green")

     # Draw a pine tree.
    tree_center_x = 250
    tree_bottom = 100
    tree_height = 320
    draw_pine_tree(canvas, tree_center_x,
        tree_bottom, tree_height)


    # another pine tree
    tree_center_x = 210
    tree_bottom = 120
    tree_height = 320
    draw_pine_tree(canvas, tree_center_x,
        tree_bottom, tree_height)
    
    tree_center_x = 211
    tree_bottom = 111
    tree_height = 310
    draw_pine_tree(canvas, tree_center_x,
        tree_bottom, tree_height)

    tree_center_x = 400
    tree_bottom = 150
    tree_height = 340
    draw_pine_tree(canvas, tree_center_x, tree_bottom, tree_height)

    tree_center_x = 375
    tree_bottom = 74
    tree_height = 330
    draw_pine_tree(canvas, tree_center_x, tree_bottom, tree_height)


   
def draw_pine_tree(canvas, tree_center_x, bottom, height):
    """draw a single pine trees parameters"""
    
    # trunk also sterm
    trunk_width = height / 10
    trunk_height = height / 4
    trunk_left = tree_center_x - trunk_width / 3
    trunk_right = tree_center_x + trunk_width / 3
    trunk_top = bottom + trunk_height

    draw_rectangle(canvas, trunk_left, trunk_top, trunk_right, bottom, outline="gray20", width=1, fill="tan3")

    # skirt or leaves
    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = tree_center_x - skirt_width / 2
    skirt_right = tree_center_x + skirt_width / 2
    skirt_top = bottom + height

    draw_polygon(canvas, tree_center_x, skirt_top, skirt_right, trunk_top, skirt_left, trunk_top, outline="gray20", width=1, fill="dark green")

def draw_sea(canvas, scene_width, scene_height):
    draw_oval(canvas, 20, 20, 325, 160, fill="dodgerBlue1")

def draw_sun(canvas, scene_width, scene_height):
    draw_oval(canvas, 600, 600, 775, 400, outline="cyan1", fill="orange")
    #draw_oval(canvas, x0, y0, x1, y1)


def draw_house(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 550, 300, 750, 100, fill="gold1")
    draw_rectangle(canvas, 600, 200, 640, 100, fill="oliveDrab4")
    draw_rectangle(canvas, 675, 175, 700, 200, fill="tan4")
    draw_rectangle(canvas, 600, 160, 620, 152, fill="tan4")
    draw_polygon(canvas, 550, 300, 750, 300, 645, 450, fill="peachPuff")

def draw_clouds(canvas, scene_width, scene_height):
    draw_oval(canvas, 25, 475, 70, 400, outline="gray47", fill="gray47")
    draw_oval(canvas, 40, 460, 150, 350, outline="gray47", fill="gray47")
    draw_oval(canvas, 50, 440, 110, 300, outline="gray47", fill="gray47" )
    draw_oval(canvas, 40, 460, 195, 350,outline="gray47", fill="gray47" )
    draw_oval(canvas, 350, 505, 110, 420,outline="gray47", fill="gray47" )
    draw_oval(canvas, 150, 500, 60, 450, outline="gray47", fill="gray47" )


def draw_flower(canvas, scene_width, scene_height ):
    draw_oval(canvas, 550, 20, 500, 40, fill="pink")
    draw_oval(canvas, 550, 40, 540, 70, fill="red")
    draw_oval(canvas, 540, 50, 490, 80, fill="seaGreen3")
    draw_oval(canvas, 500, 70, 510, 100, fill="yellow1") 


   


# Call the main function so that
# this program will start executing.
main()