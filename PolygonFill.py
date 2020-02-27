import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


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

    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glColor3f(1.0, 0.0, 0.0)

    glPushMatrix()
    try:
        glTranslatef(0, -1, 0)
        glRotatef(280, 2, 0, 0)
        glutSolidCone(1, 2, 50, 10)
    finally:
        glPopMatrix()


def load_texture():
    texture_surface = pygame.image.load('texture.jpg')
    texture_data = pygame.image.tostring(texture_surface, "RGBA", 1)
    width = texture_surface.get_width()
    height = texture_surface.get_height()

    glEnable(GL_TEXTURE_2D)
    tex_id = glGenTextures(1)

    glBindTexture(GL_TEXTURE_2D, tex_id)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, texture_data)

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

    return tex_id


def create_cube():
    load_texture()
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

    glRotatef(5, 1.0, 0.0, 0.0)  # Eje x
    glRotatef(150, 0.0, 1.0, 0.0)  # Eje y
    glRotatef(45, 0.0, 0.0, 1.0)  # Eje z

    # Draw Cube (multiple quads)
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(1.0, -1.0, 1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(1.0, 1.0, 1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(1.0, 1.0, -1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(1.0, -1.0, -1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(1.0, 1.0, 1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(1.0, 1.0, -1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(1.0, -1.0, -1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(1.0, -1.0, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(1.0, -1.0, -1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(1.0, 1.0, -1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(1.0, 1.0, 1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(1.0, -1.0, 1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.0, 1.0, -1.0)
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

    glColor3f(8, 0.0, 0.0)  # Red
    glVertex3f(0.0, 1.0, 0.0)  # Top Of Triangle (Front)
    glColor3f(5, 4.0, 0.0)  # Green
    glVertex3f(-1.0, -1.0, 1.0)  # Left Of Triangle (Front)
    glColor3f(2.0, 0.0, 0.0)  # Blue
    glVertex3f(1.0, -1.0, 1.0)

    glColor3f(8, 0.0, 0.0)  # Red
    glVertex3f(0.0, 1.0, 0.0)  # Top Of Triangle (Front)
    glColor3f(5, 4.0, 0.0)  # Green
    glVertex3f(-1.0, -1.0, 1.0)  # Left Of Triangle (Front)
    glColor3f(2.0, 0.0, 0.0)  # Blue
    glVertex3f(1.0, -1.0, 1.0)

    glColor3f(8, 0.0, 0.0)  # Red
    glVertex3f(0.0, 1.0, 0.0)  # Top Of Triangle (Front)
    glColor3f(5, 4.0, 0.0)  # Green
    glVertex3f(-1.0, -1.0, 1.0)  # Left Of Triangle (Front)
    glColor3f(2.0, 0.0, 0.0)  # Blue
    glVertex3f(1.0, -1.0, 1.0)

    glColor3f(8.0, 0.0, 0.0)  # Red
    glVertex3f(0.0, 1.0, 0.0)  # Top Of Triangle (Left)
    glColor3f(5.0, 4.0, 1.0)  # Blue
    glVertex3f(-1.0, -1.0, -1.0)  # Left Of Triangle (Left)
    glColor3f(2.0, 0.0, 0.0)  # Green
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
    #glutIdleFunc(create_cone)

    #glutIdleFunc(draw_pyramid)

    glutIdleFunc(create_cube)


    # Run the OpenGL main loop
    glutMainLoop()


# Call the main function
if __name__ == '__main__':
    main()
