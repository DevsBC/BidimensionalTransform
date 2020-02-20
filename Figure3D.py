# Python imports
from math import *
import time
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import itertools


def create_sphere():

    # Number of latitudes in sphere
    lats = 100

    # Number of longitudes in sphere
    longs = 100

    user_theta = 0
    user_height = 0

    # Direction of light
    direction = [0.0, 2.0, -1.0, 1.0]

    # Intensity of light
    intensity = [0.7, 0.7, 0.7, 1.0]

    # Intensity of ambient light
    ambient_intensity = [0.3, 0.3, 0.3, 1.0]

    # The surface type(Flat or Smooth)
    surface = GL_FLAT

    x = 2 * cos(user_theta)
    y = 2 * sin(user_theta)
    z = user_height
    d = sqrt(x * x + y * y + z * z)

    # Set matrix mode
    glMatrixMode(GL_PROJECTION)

    # Reset matrix
    glLoadIdentity()
    glFrustum(-d * 0.5, d * 0.5, -d * 0.5, d * 0.5, d - 1.1, d + 1.1)

    # Set camera
    gluLookAt(x, y, z, 0, 0, 0, 0, 0, 1)

    # Set OpenGL parameters
    glEnable(GL_DEPTH_TEST)

    # Enable lighting
    glEnable(GL_LIGHTING)

    # Set light model
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambient_intensity)

    # Enable light number 0
    glEnable(GL_LIGHT0)

    # Set position and intensity of light
    glLightfv(GL_LIGHT0, GL_POSITION, direction)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, intensity)

    # Setup the material
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Set color to white
    glColor3f(1.0, 1.0, 1.0)

    # Set shade model
    glShadeModel(surface)

    draw_sphere(lats, longs)

    glutSwapBuffers()


def draw_sphere(lats, longs):
    for i in range(0, lats + 1):
        lat0 = pi * (-0.5 + float(float(i - 1) / float(lats)))
        z0 = sin(lat0)
        zr0 = cos(lat0)

        lat1 = pi * (-0.5 + float(float(i) / float(lats)))
        z1 = sin(lat1)
        zr1 = cos(lat1)

        # Use Quad strips to draw the sphere
        glBegin(GL_QUAD_STRIP)

        for j in range(0, longs + 1):
            lng = 2 * pi * float(float(j - 1) / float(longs))
            x = cos(lng)
            y = sin(lng)
            glNormal3f(x * zr0, y * zr0, z0)
            glVertex3f(x * zr0, y * zr0, z0)
            glNormal3f(x * zr1, y * zr1, z1)
            glVertex3f(x * zr1, y * zr1, z1)
        glEnd()


def create_cone():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # establish the projection matrix (perspective)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(500) / float(500), 0.1, 100.0)

    # and then the model view matrix
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(
        0, 1, 5,  # eyepoint
        0, 0, 0,  # center-of-view
        0, 1, 0,  # up-vector
    )

    draw_cone()

    glutSwapBuffers()


def draw_cone():
    glLightfv(GL_LIGHT0, GL_AMBIENT, GLfloat_4(0.0, 1.0, 0.0, 1.0))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, GLfloat_4(1.0, 1.0, 1.0, 1.0))
    glLightfv(GL_LIGHT0, GL_SPECULAR, GLfloat_4(1.0, 1.0, 1.0, 1.0))
    glLightfv(GL_LIGHT0, GL_POSITION, GLfloat_4(1.0, 1.0, 1.0, 0.0))
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, GLfloat_4(0.2, 0.2, 0.2, 1.0))
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)

    glMaterialfv(GL_FRONT, GL_AMBIENT, GLfloat_4(0.2, 0.2, 0.2, 1.0))
    glMaterialfv(GL_FRONT, GL_DIFFUSE, GLfloat_4(0.8, 0.8, 0.8, 1.0))
    glMaterialfv(GL_FRONT, GL_SPECULAR, GLfloat_4(1.0, 0.0, 1.0, 1.0))
    glMaterialfv(GL_FRONT, GL_SHININESS, GLfloat(50.0))

    start_time = time.time()
    angle = (((time.time() - start_time) % 10) / 10) * 360
    glRotate(angle, 0, 1, 0)

    glPushMatrix()
    try:
        glTranslatef(0, -1, 0)
        glRotatef(280, 2, 0, 0)
        glutSolidCone(1, 2, 50, 10)
    finally:
        glPopMatrix()


# rotation
X_AXIS = 0.0
Y_AXIS = 0.0
Z_AXIS = 0.0
DIRECTION = 1


def create_cube():
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(500) / float(500), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    draw_cube()


def draw_cube():
    global X_AXIS, Y_AXIS, Z_AXIS
    global DIRECTION

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


def draw_pyramid():
    glClearColor(0.0, 0.0, 0.0, 0.0)  # This Will Clear The Background Color To Black
    glClearDepth(1.0)  # Enables Clearing Of The Depth Buffer
    glDepthFunc(GL_LESS)  # The Type Of Depth Test To Do
    glEnable(GL_DEPTH_TEST)  # Enables Depth Testing
    glShadeModel(GL_SMOOTH)  # Enables Smooth Color Shading

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()  # Reset The Projection Matrix
    # Calculate The Aspect Ratio Of The Window
    gluPerspective(45.0, float(500) / float(500), 0.1, 100.0)

    glMatrixMode(GL_MODELVIEW)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()  # Reset The View
    glTranslatef(0.0, 0.0, -6.0)  # Move Left And Into The Screen

    glRotatef(25, 0.4, 3.0, 0.0)  # Rotate The Pyramid On It's Y Axis

    glBegin(GL_TRIANGLES)  # Start Drawing The Pyramid

    glColor3f(1.0, 0.0, 0.0)  # Red
    glVertex3f(0.0, 1.0, 0.0)  # Top Of Triangle (Front)
    glColor3f(0.0, 1.0, 0.0)  # Green
    glVertex3f(-1.0, -1.0, 1.0)  # Left Of Triangle (Front)
    glColor3f(0.0, 0.0, 1.0)  # Blue
    glVertex3f(1.0, -1.0, 1.0)

    glColor3f(1.0, 0.0, 0.0)  # Red
    glVertex3f(0.0, 1.0, 0.0)  # Top Of Triangle (Right)
    glColor3f(0.0, 0.0, 1.0)  # Blue
    glVertex3f(1.0, -1.0, 1.0)  # Left Of Triangle (Right)
    glColor3f(0.0, 1.0, 0.0)  # Green
    glVertex3f(1.0, -1.0, -1.0)  # Right

    glColor3f(1.0, 0.0, 0.0)  # Red
    glVertex3f(0.0, 1.0, 0.0)  # Top Of Triangle (Back)
    glColor3f(0.0, 1.0, 0.0)  # Green
    glVertex3f(1.0, -1.0, -1.0)  # Left Of Triangle (Back)
    glColor3f(0.0, 0.0, 1.0)  # Blue
    glVertex3f(-1.0, -1.0, -1.0)  # Right Of

    glColor3f(1.0, 0.0, 0.0)  # Red
    glVertex3f(0.0, 1.0, 0.0)  # Top Of Triangle (Left)
    glColor3f(0.0, 0.0, 1.0)  # Blue
    glVertex3f(-1.0, -1.0, -1.0)  # Left Of Triangle (Left)
    glColor3f(0.0, 1.0, 0.0)  # Green
    glVertex3f(-1.0, -1.0, 1.0)  # Right Of Triangle (Left)
    glEnd()
    #  since this is double buffered, swap the buffers to display what just got drawn.
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
    glutCreateWindow('Tridimensional: Juan Carlos Aranda')

    # Set the callback function for display
    #glutDisplayFunc(create_sphere)

    #glutDisplayFunc(create_cone)

    #glutDisplayFunc(create_cube)

    glutDisplayFunc(draw_pyramid)

    # Run the OpenGL main loop
    glutMainLoop()


# Call the main function
if __name__ == '__main__':
    main()
