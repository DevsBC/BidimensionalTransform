# Python imports
from math import *
import time
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# rotation
X_AXIS = 0.0
Y_AXIS = 0.0
Z_AXIS = 0.0
DIRECTION = 1


def transform_cube(transform):
    global X_AXIS, Y_AXIS, Z_AXIS
    global DIRECTION

    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(500) / float(500), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()
    glTranslatef(0.0, 0.0, -6.0)

    if transform == "traslar":
        glTranslatef(3, 0.0, 0.0)
        glTranslatef(0.0, 0.0, 0.0)
        glTranslatef(0, 0.0, -6.0)

    if transform == "escalar":
        glScalef(1.2, 1.2, 1.2)  # Eje x

    if transform == "rotar":
        glRotatef(5, 1.0, 0.0, 0.0)  # Eje x
        glRotatef(150, 0.0, 1.0, 0.0)  # Eje y
        glRotatef(45, 0.0, 0.0, 1.0)  # Eje z

    if transform == "sesgar":
        glRotatef(150, 0.0, 1.0, 0.0)  # Eje y
        glScalef(1.5, 1.3, .5)  # Eje x

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

    X_AXIS = X_AXIS - 0.30
    Z_AXIS = Z_AXIS - 0.30

    glutSwapBuffers()


def main():
    # Initialize the OpenGL pipeline
    glutInit(sys.argv)

    # Set OpenGL display mode
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)

    # Set the Window size and position
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)

    # Create the window with given title
    glutCreateWindow('Tridimensional Cubo: Juan Carlos Aranda')

    glutIdleFunc(transform_cube("sesgar"))
    # Run the OpenGL main loop
    glutMainLoop()


# Call the main function
if __name__ == '__main__':
    main()
