"""
The Assignment: Your Illusion

Pick one of the five optical illusions described in the README and
recreate it here with canvas2d. Then modify it in some way (colors,
number of shapes, line thickness, or anything else) so your version
is distinct from the original, without breaking the illusion.
"""
import canvas2d
print(dir(canvas2d))
canvas2d.set_x_scale(0, 100)
canvas2d.set_y_scale(0, 100)

def draw_my_illusion(canvas):
    """Draw your chosen illusion."""
    # TODO: replace this with your illusion
    canvas.set_pen_color(canvas.GRAY)
    canvas.set_pen_width(5)
    canvas.filled_rectangle(50, 50, 50, 50)
    canvas.rectangle(50, 50, 50, 50)

def main():
    canvas = canvas2d.Canvas(1000, 1000)
    canvas.clear(canvas.WHITE)
    draw_my_illusion(canvas)
    canvas.wait_for_close()


if __name__ == "__main__":
    main()
