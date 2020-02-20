from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


# The cube class
class Cube:

    # Constructor for the cube class
    def __init__(self):
        self.X_AXIS = 0.0
        self.Y_AXIS = 0.0
        self.Z_AXIS = 0.0
        self.scale = 2.0

    def create_cube(self):
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, float(500) / float(500), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)
        self.draw_cube()

    def draw_cube(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glLoadIdentity()
        glTranslatef(0.0, 0.0, -6.0)

        glRotatef(20, 1.0, 0.0, 0.0)  # Eje x
        glRotatef(30, 0.0, 1.0, 0.0)  # Eje y
        glRotatef(300, 0.0, 0.0, 1.0)  # Eje z

        # Draw Cube (multiple quads)
        glBegin(GL_QUADS)

        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(1.0, 1.0, -1.0)
        glVertex3f(-1.0, 1.0, -1.0)
        glVertex3f(-1.0, 1.0, 1.0)
        glVertex3f(1.0, 1.0, 1.0)

        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(1.0, -1.0, 1.0)
        glVertex3f(-1.0, -1.0, 1.0)
        glVertex3f(-1.0, -1.0, -1.0)
        glVertex3f(1.0, -1.0, -1.0)

        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(1.0, 1.0, 1.0)
        glVertex3f(-1.0, 1.0, 1.0)
        glVertex3f(-1.0, -1.0, 1.0)
        glVertex3f(1.0, -1.0, 1.0)

        glColor3f(1.0, 1.0, 0.0)
        glVertex3f(1.0, -1.0, -1.0)
        glVertex3f(-1.0, -1.0, -1.0)
        glVertex3f(-1.0, 1.0, -1.0)
        glVertex3f(1.0, 1.0, -1.0)

        glColor3f(0.0, 0.0, 1.0)
        glVertex3f(-1.0, 1.0, 1.0)
        glVertex3f(-1.0, 1.0, -1.0)
        glVertex3f(-1.0, -1.0, -1.0)
        glVertex3f(-1.0, -1.0, 1.0)

        glColor3f(1.0, 0.0, 1.0)
        glVertex3f(1.0, 1.0, -1.0)
        glVertex3f(1.0, 1.0, 1.0)
        glVertex3f(1.0, -1.0, 1.0)
        glVertex3f(1.0, -1.0, -1.0)

        glEnd()

        glutSwapBuffers()




