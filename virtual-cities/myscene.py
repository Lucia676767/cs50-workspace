"""
Virtual Cities!

Instructions and Documentation:
https://gist.github.com/mrsharp-milken/21c48a631c51849a83bf6f05ea9c8b86
"""

from Scene3D import Scene3D

def main():
    scene = Scene3D()

    setup_lights(scene)
    setup_cameras(scene)
    add_ground(scene)

    for i in range(3):
        drawTree(scene, 3 + i, i * 20)

    scene.save_scene("myscene.html", "Secret Garden Forest")


# Task 1: finish this function (delete "pass" once you add your code)
def drawTree(scene, cx, cz, height):
    scene.add_cylinder(cx, height/2, cz, 0.5, height, 139, 69, 19)
    scene.add_cone(cx, height + height/2, cz, 2, height, 34, 139, 34)

#    Task 2 and beyond: define your own functions!

def setup_lights(scene):
    scene.add_point_light(-100, 200, 0, 200, 200, 200, 1.0)
    scene.add_point_light(100, 200, 0, 200, 200, 200, 1.0)
    scene.add_point_light(0, 0, -100, 200, 200, 200, 1.0)
    scene.add_point_light(0, 0, 100, 200, 200, 200, 1.0)

def setup_cameras(scene):
    scene.add_camera(0, 2, 0, 0)
    scene.add_camera(0, 2, -40, 180)

def add_ground(scene):
    # Add a large gray box for the ground
    scene.add_box(0, -25, 0, 1000, 50, 1000, 100, 100, 100)


main()
