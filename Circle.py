from OpenGL.GL import *
import math


class Circle:
    def __init__(self, radio, pos_x, pos_y):
        self.__radio = radio
        self.__pos_x = pos_x
        self.__pos_y = pos_y

    def create_circle(self):
        double_pi = math.pi * 2.0
        glColor(0.0, 0.4, 0.2)
        glBegin(GL_LINE_LOOP)
        glVertex(self.__pos_x, self.__pos_y, 0.0)
        for segment in range(0, 360):
            theta = segment * double_pi / 180
            x = self.__radio * math.cos(theta)
            y = self.__radio * math.sin(theta)
            glVertex2f(self.__pos_x + x, self.__pos_y + y)
        glEnd()
