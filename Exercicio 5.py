import OpenGL.GLUT as GLUT
import OpenGL.GLU as GLU
import OpenGL.GL as GL
from sys import argv
from math import sin, cos, pi

window_name = "Questão 5"
alpha = 0
beta = 180.0
delta_alpha = 0.5
delta_x = 0
delta_y = 0
delta_z = 0
down_x = 0
down_y = 0
background_color = (0.000, 0.300, 0.500, 1)
m, n = 20, 20
radius = 2

def f(i,j):
    theta = ((pi * i) / (m - 1)) - (pi / 2)
    phi = 2 * pi * j / (n - 1)
    x = radius * cos(theta) * cos(phi)
    y = radius * sin(theta)
    z = radius * cos(theta) * sin(phi)
    return x, y ** 2, z

def figure():
    GL.glPushMatrix()
    GL.glTranslatef(delta_x, delta_y + 1.5, delta_z)
    GL.glRotatef(alpha, 0.0, 1.0, 0.0)
    GL.glRotatef(beta, 0.0, 0.0, 1.0)

    for i in range(round(m / 2)):
        GL.glBegin(GL.GL_QUAD_STRIP)
        for j in range(n):
            GL.glColor3fv(((2.0 * i / (m - 1)),3,1 - (1.0 * i / (m - 1))))
            x, y, z = f(i, j)
            GL.glVertex3f(x, y, z)
            GL.glColor3fv(((2.0 * (i + 1) / (m - 1)), 3,1 - (1.0 * (i + 1) / (m - 1))))
            x, y, z = f(i + 1, j)
            GL.glVertex3f(x, y, z)
        GL.glEnd()
    GL.glPopMatrix()

def draw():
    global alpha
    GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
    figure()
    alpha = alpha + delta_alpha
    GLUT.glutSwapBuffers()

def timer(i):
    GLUT.glutPostRedisplay()
    GLUT.glutTimerFunc(10, timer, 1)

def key_pressed(key, x, y):
    global delta_alpha

    if key == b"\033":
        GLUT.glutLeaveMainLoop()
    elif key == b" ":
        if delta_alpha == 0:
            delta_alpha = 0.5
        else:
            delta_alpha = 0


GLUT.glutInit(argv)
GLUT.glutInitDisplayMode(
GLUT.GLUT_DOUBLE | GLUT.GLUT_RGBA | GLUT.GLUT_DEPTH | GLUT.GLUT_MULTISAMPLE)
screen_width = GLUT.glutGet(GLUT.GLUT_SCREEN_WIDTH)
screen_height = GLUT.glutGet(GLUT.GLUT_SCREEN_HEIGHT)
window_width = round(2 * screen_width / 2)
window_height = round(2 * screen_height / 2)
GLUT.glutInitWindowSize(window_width, window_height)
GLUT.glutInitWindowPosition(
round((screen_width - window_width) / 2), round((screen_height - window_height) / 2))
GLUT.glutCreateWindow(window_name)
GLUT.glutDisplayFunc(draw)
GL.glEnable(GL.GL_MULTISAMPLE)
GL.glEnable(GL.GL_DEPTH_TEST)
GL.glClearColor(*background_color)
GLU.gluPerspective(-60, window_width / window_height, 0.1, 100.0)
GL.glTranslatef(0.0, 0.0, -10)
GLUT.glutTimerFunc(10, timer, 1)
GLUT.glutMainLoop()

