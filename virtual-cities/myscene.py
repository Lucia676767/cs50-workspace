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
    #DrawBear(scene, 4, 4, 90)
    DrawBear(scene, 6, 6, 0)
    DrawLake(scene,0, 0, 0)

    scene.save_scene("myscene.html", "Secret Garden Forest")

def ForestCorner(scene, cx, cz, cy):
    import math
    num_items = 25
    radius = 100
    center_x, center_z = 4, 4

    for i in range(num_items):
        angle = (2 * math.pi / num_items) * i
        x = center_x + radius * math.cos(angle)
        z = center_z + radius * math.sin(angle)
        print("X: ",x," Z:",z)
        DrawTree(scene, x, z, random.randint(5,10))
        DrawMushy(scene, x+10, z+10, 4)
        DrawTreeDif(scene, x+15, z+15,random.randint(10,20))

def DrawLake(scene, cx, cz, cy):
    scene.add_cylinder(cx, cy, cz, 50, .5, 79, 115, 142)

def DrawTreeDif(scene, cx, cz, height):
    scene.add_cylinder(cx , height/2, cz, 1, height, 139, 69, 19)
    scene.add_ellipsoid(cx, height-4+height/4, cz, 2, 4, 2, 236, 183, 83)

def DrawTree(scene, cx, cz, height):
    scene.add_cylinder(cx, height/2, cz, 0.5, height, 139, 69, 19)
    scene.add_cone(cx, height + height-6, cz, 2, height, 34, 139, 34)

def DrawMushy(scene, cx, cz, height):
    scene.add_cylinder(cx , height/8, cz-2.5, 0.5, height, 255, 255, 255)
    scene.add_sphere(cx, height-2, cz-2.5, 1, 255, 0, 0)

def DrawBear(scene, cx, cz, ry):
    group = scene.add_group(cx, 0, cz, 0, ry, 0)
    #body
    group.add_ellipsoid(cx, 3 , 8, 3, 2, 4, 150, 75, 0)
    group.add_sphere(cx, 6, 4, 2, 150, 75, 0)
    #ears
    group.add_sphere(cx+2, 8, 4, 1, 150, 75, 0)
    group.add_sphere(cx-2, 8, 4, 1, 150, 75, 0)
    #legs
    group.add_cylinder(cx-1, 2, cz+6, .5, 4, 255, 150, 75)
    group.add_cylinder(cx+1, 2, cz+6, .5, 4, 255, 150, 75)
    group.add_cylinder(cx-2, 2, cz+3, .5, 4, 255, 150, 75)
    group.add_cylinder(cx+2, 2, cz+3, .5, 4, 255, 150, 75)

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
