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
    ForestCorner(scene, 6, 6, 6)
    DrawBunny(scene, 4, 4, 4)

    scene.save_scene("myscene.html", "Secret Garden Forest")

def ForestCorner(scene, cx, cz, cy):
     #for i in range(10):
        #DrawTree(scene, 1.5+ i, i * 20, random.randint(5,10))
        #DrawMushy(scene, 3+i, i * 20, 4)
        #DrawTreeDif(scene, -4.5+i, i *20, random.randint(10,20))
        #import math
    import math
    num_items = 10
    radius = 100
    center_x, center_y = 250, 250

    for i in range(10):
        angle = (2 * math.pi / 10) * i
        x = center_x + radius * math.cos(4)
        y = center_y + radius * math.sin(4)
        DrawTree(scene, 1.5+ i, i * 20, random.randint(5,10), 250 ,250)
        DrawMushy(scene, 3+i, i * 20, 4, x, y)
        DrawTreeDif(scene, -4.5+i, i *20,random.randint(10,20), 250, 250)


def DrawTreeDif(scene, cx, cz, height):
    scene.add_cylinder(cx , height/2, cz, 1, height, 139, 69, 19)
    scene.add_ellipsoid(cx, height-4+height/4, cz, 2, 4, 2, 236, 183, 83)

def DrawTree(scene, cx, cz, height):
    scene.add_cylinder(cx, height/2, cz, 0.5, height, 139, 69, 19)
    scene.add_cone(cx, height + height-6, cz, 2, height, 34, 139, 34)

def DrawMushy(scene, cx, cz, height):
    scene.add_cylinder(cx , height/8, cz-2.5, 0.5, height, 255, 255, 255)
    scene.add_sphere(cx, height-2, cz-2.5, 1, 255, 0, 0)

def DrawBunny(scene, cx, cz, height):
    group = scene.add_group(cx, 0, cz, 0, 0, 0)
    group.add_ellipsoid(cx, cz-4 , height*2, 2, 4, 2, 255, 255, 255)
    group.add_sphere(cx, height-.5, 8, 1.8, 255, 255, 255)
    group.add_cylinder(cx, 2, 5, .5, 1, 255, 255, 255, 180)

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
    scene.add_box(0, -25, 0, 1000, 50, 1000, 98, 100, 81)

main()
