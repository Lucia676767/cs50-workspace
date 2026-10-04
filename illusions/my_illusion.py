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
    #Apply to context
    gradientRectangle(canvas)

    #draw second grey rectangle
    drawRectangle(canvas,canvas.GRAY,5,400, 300, 500, 200)

def drawRectangle(canvas,color,penWidth,x,y,width,height):
    canvas.set_pen_color(color)
    canvas.set_pen_width(penWidth)
    canvas.filled_rectangle(x,y,width,height)

def gradientRectangle(canvas):
    for i in range(100):
        fade= i*2.5
        canvas.set_pen_color_rgb(fade,fade,fade)
        canvas.set_pen_width(10)
        canvas.line(i*10, 0, i*10, 1000)

def main():
    canvas = canvas2d.Canvas(1000, 1000)
    canvas.clear(canvas.WHITE)
    draw_my_illusion(canvas)
    canvas.wait_for_close()


if __name__ == "__main__":
    main()
