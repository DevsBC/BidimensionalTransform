
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

pos_x = 400
pos_y = 400

def create_circle():
    # Parametros para crear un circulo
    radio = 100
    double_pi = math.pi * 2.0
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.4, 0.2)
    glBegin(GL_POLYGON)
    for segment in range(0, 360):
        theta = segment * double_pi / 180
        x = radio * math.cos(theta)
        y = radio * math.sin(theta)
        glVertex2f(pos_x + x, pos_y + y)
    glEnd()
    glFlush()


def create_ellipse():
    # Parametros para crear un ovalo
    radio_x = 100
    radio_y = 250
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.4, 0.2)
    glBegin(GL_LINE_LOOP)
    for segment in range(0, 360):
        theta = segment * math.pi / 180
        x = radio_x * math.cos(theta)
        y = radio_y * math.sin(theta)
        glVertex2f(pos_x + x, pos_y + y)
    glEnd()
    glFlush()


def create_arc():
    cx = pos_x
    cy = pos_y
    start_angle = 0
    arc_angle = 3
    num_segments = 360
    r = 100
    theta = arc_angle / float(num_segments - 1)
    tangetial_factor = math.tan(theta)
    radial_factor = math.cos(theta)
    x = r * math.cos(start_angle)
    y = r * math.sin(start_angle)

    glBegin(GL_LINE_STRIP)
    for ii in range(num_segments):
        glVertex2f(x + cx, y + cy)
        tx = -y
        ty = x

        x += tx * tangetial_factor
        y += ty * tangetial_factor

        x *= radial_factor
        y *= radial_factor
    glEnd()
    glFlush()


def create_wave():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.4, 0.2)
    glBegin(GL_POINTS)
    for segment in range(0, 360):
        y = 100 * math.sin(segment * (10/360))
        glVertex2f(pos_x + segment, pos_y + y)
    glEnd()
    glFlush()


def create_spiral():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.4, 0.2)
    a = 4
    b = 4
    for i in range(0, 1000):
        glBegin(GL_LINES)
        angle = 0.1 * i
        x = (a + b * angle) * math.cos(angle)
        y = (a + b * angle) * math.sin(angle)
        glVertex2f(pos_x + x, pos_y + y)
        glVertex2f(a*pow(2.7 ,b *angle)*math.cos(angle), a*pow(2.7, b*angle)*math.sin(angle))
        glEnd()
    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowPosition(50, 50)
    glutInitWindowSize(800, 600)
    glutCreateWindow("Figuras circulares: Juan Carlos Aranda")
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(0.0, 800.0, 0.0, 800.0)
    #glutDisplayFunc(create_circle)
    #glutDisplayFunc(create_ellipse)
    #glutDisplayFunc(create_arc)
    #glutDisplayFunc(create_wave)
    glutDisplayFunc(create_spiral)
    glutMainLoop()


main()


