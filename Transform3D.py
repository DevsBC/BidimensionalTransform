from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from objects.Cube import Cube


# The main function
def main():

    # Initialize OpenGL
    glutInit(sys.argv)

    # Set display mode
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

    # Set size and position of window size
    glutInitWindowSize(400, 400)
    glutInitWindowPosition(100, 100)

    # Create window with given title
    glutCreateWindow("Cube")

    # Instantiate the cube
    cube = Cube()


    # The callback for display function
    glutDisplayFunc(cube.create_cube())


    # Start the main loop
    glutMainLoop()

# Call the main function
if __name__ == '__main__':
    main()