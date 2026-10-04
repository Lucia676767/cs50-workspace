"""
The Assignment: Your Illusion

Pick one of the five optical illusions described in the README and
recreate it here with canvas2d. Then modify it in some way (colors,
number of shapes, line thickness, or anything else) so your version
is distinct from the original, without breaking the illusion.
"""
import canvas2d
print(dir(canvas2d))


def draw_my_illusion(canvas):
    """Draw your chosen illusion."""
    # TODO: replace this with your illusion

    #Create a linear gradient (x0, y0, x1, y1)
    const gradient = ctx.createLinearGradient(0, 0, 200, 0);
    gradient.addColorStop(0, "red");
    gradient.addColorStop(1, "yellow");

    #Apply to context
    ctx.fillStyle = gradient;
    canvas.filled_rectangle(400, 300, 100, 200)

    #draw second grey rectangle
    canvas.set_pen_color(canvas.GRAY)
    canvas.set_pen_width(5)
    canvas.filled_rectangle(400, 300, 500, 200)


def main():
    canvas = canvas2d.Canvas(1000, 1000)
    canvas.clear(canvas.WHITE)
    draw_my_illusion(canvas)
    canvas.wait_for_close()


if __name__ == "__main__":
    main()
