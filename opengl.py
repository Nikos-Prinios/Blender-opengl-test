bl_info = {
    "name": "Blzblz",
    "author": "Nikos",
    "version": (1, 0),
    "blender": (2, 75, 0),
    "location": "View3D",
    "description": "Draws two points using BGL",
    "warning": "",
    "wiki_url": "",
    "category": "User Interface",
    }


import bpy
import bmesh
import bgl
import random
handle = [None]

ON = False
    
def callbackFunction():
    d=5
    mesh = bpy.context.scene.objects.active.data
    bm = bmesh.from_edit_mesh(mesh)
    for v in bm.verts:
        x = v.co.x
        y = v.co.y
        z = v.co.z

        bgl.glPointSize(d)
        bgl.glColor3f(random.random(), random.random(), random.random())
        bgl.glBegin(bgl.GL_POINTS)
        bgl.glVertex3f(x,y,z)
        bgl.glEnd()
        


def register():
    handle[0] = bpy.types.SpaceView3D.draw_handler_add(callbackFunction, (), 'WINDOW', 'POST_VIEW')


def unregister():
    bpy.types.SpaceView3D.draw_handler_remove(handle[0], 'WINDOW')
    handle[0] = None


if __name__ == "__main__":
    register()
