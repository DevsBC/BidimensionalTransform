from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# Posicion centrada del objeto
pos_x = 400
pos_y = 400


def create_circle():
    # Parametros para crear un circulo
    radio = 300
    double_pi = math.pi * 2.0
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.4, 0.2)
    glBegin(GL_POLYGON)
    for segment in range(0, 360): # ciclo hasta completar el circulo
        theta = segment * double_pi / 180
        x = radio * math.cos(theta)
        y = radio * math.sin(theta)
        glVertex2f(pos_x + x, pos_y + y)
    glEnd()
    glFlush()


def create_ellipse():
    # Parametros para crear un ovalo
    radio_x = 100
    radio_y = 250 # Radio irregular para lograr la forma
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.8, 0.1)
    glBegin(GL_LINE_LOOP)
    for segment in range(0, 360): # la misma implementacion de un circulo
        theta = segment * math.pi / 180
        x = radio_x * math.cos(theta)
        y = radio_y * math.sin(theta)
        glVertex2f(pos_x + x, pos_y + y)
    glEnd()
    glFlush()


def create_arc():
    start_angle = 0
    arc_angle = 3.2 # la vuelta del angulo
    num_segments = 100
    radio = 200 # Radio del semicirculo
    theta = arc_angle / float(num_segments - 1)
    tan_factor = math.tan(theta)
    radial_factor = math.cos(theta)
    x = radio * math.cos(start_angle)
    y = radio * math.sin(start_angle)

    glColor3f(0.0, 1, 2)
    glBegin(GL_LINE_STRIP)
    for angle in range(num_segments):
        glVertex2f(pos_x + x, pos_y + y)
        tan_x = -y
        tan_y = x

        x += tan_x * tan_factor  # forma un medio arco
        y += tan_y * tan_factor

        x *= radial_factor  # multiplica por el factor del radio
        y *= radial_factor
    glEnd()
    glFlush()


def create_wave():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.4, 0.2)
    amplitude = 10
    frequency = 500
    glBegin(GL_POINTS)
    for segment in range(0, 1000):
        y = 100 * math.sin(segment * (amplitude/frequency))
        glVertex2f(segment, pos_y + y)
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

    glutDisplayFunc(create_wave)
    glutMainLoop()


main()


