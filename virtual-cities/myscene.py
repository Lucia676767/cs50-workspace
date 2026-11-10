"""
Virtual Cities!

Instructions and Documentation:
https://gist.github.com/mrsharp-milken/21c48a631c51849a83bf6f05ea9c8b86
"""
import random
from Scene3D import Scene3D


def main():
    scene = Scene3D()
    setup_lights(scene)
    setup_cameras(scene)
    add_ground(scene)
    for i in range(10):
        DrawTree(scene, 1.5+ i, i * 20, random.randint(5,10))
        DrawMushy(scene, 3+i, i * 20, 4)
        DrawTreeDif(scene, -6+i, i *20, random.randint(10,20))
    scene.save_scene("myscene.html", "Secret Garden Forest")

def DrawTreeDif(scene, cx, cz, height):
    scene.add_cylinder(cx , height/2, cz, 1, height, 139, 69, 19)
    scene.add_ellipsoid(cx, height-4+height/4, cz, 2, 4, 2, 236, 183, 83)

def DrawTree(scene, cx, cz, height):
    scene.add_cylinder(cx, height/2, cz, 0.5, height, 139, 69, 19)
    scene.add_cone(cx, height + height-3, cz, 2, height, 34, 139, 34)

def DrawMushy(scene, cx, cz, height):
    scene.add_cylinder(cx , height/8, cz-2.5, 0.5, height, 255, 255, 255)
    scene.add_sphere(cx, height-2, cz-2.5, 1, 255, 0, 0)


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
