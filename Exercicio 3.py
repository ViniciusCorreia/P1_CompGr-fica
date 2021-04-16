from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

N = 8
r = 2
ang = (2 * math.pi) / N

def vertices():
    y = 0
    vertice = []

    for i in range(N + 1):

        aux = []

        if (i == 0):
            aux.append(0)
            aux.append(5)
            aux.append(0)

            vertice.append(aux)

        else:
            x = r * math.cos(i * ang)
            z = r * math.sin(i * ang)

            aux.append(x)
            aux.append(y)
            aux.append(z)

            vertice.append(aux)

    return vertice

def linhas():
    linha = []
    getvertice = []
    getvertice = vertices()

    for i in range(N):
        aux = []
        if (i == 0):
            aux.append(getvertice[0])
            aux.append(getvertice[i + 1])
            linha.append(aux)
        else:
            aux.append(getvertice[0])
            aux.append(getvertice[i + 1])
            linha.append(aux)

    for i in range(N + 1):

        aux = []

        if (i == N):
            aux.append(getvertice[i])
            aux.append(getvertice[1])
            linha.append(aux)

        if (i != 0 and i != N):
            aux.append(getvertice[i])
            aux.append(getvertice[i + 1])
            linha.append(aux)

    return linha


def faces():
    face = []
    getvertice = []
    getvertice = vertices()

    for i in range(N):
        aux = []
        if (i == 0):
            aux.append(getvertice[0])
            aux.append(getvertice[1])
            aux.append(getvertice[N])
            face.append(aux)
        else:
            aux.append(getvertice[0])
            aux.append(getvertice[i])
            aux.append(getvertice[i + 1])
            face.append(aux)
    return face


cores = ((1, 0, 0), (1, 1, 0), (1, 0, 0), (1, 1, 0), (1, 0, 0), (1, 1, 0), (1, 0, 0), (1, 1, 0))


def Piramide():
    getvertices = []
    getlinhas = []
    getfaces = []
    getvertices = vertices()
    getlinhas = linhas()
    getfaces = faces()

    glBegin(GL_TRIANGLES)
    i = 0
    for face in getfaces:
        glColor3fv(cores[i])
        for vertex in face:
            glVertex3fv(vertex)
        i = i + 1
    glEnd()

    glColor3fv((0, 0.5, 0))
    glBegin(GL_LINES)
    for linha in getlinhas:
        for vertice in linha:
            glVertex3fv(vertice)
    glEnd()

a = 0

def desenha():
    global a
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glTranslatef(0, -2, 0)
    glRotatef(-a, 0, 1, 0)
    Piramide()
    glPopMatrix()
    glutSwapBuffers()
    a += 1

def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50, timer, 1)

glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800, 600)
glutCreateWindow("Piramide")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0., 0., 0., 1.)
gluPerspective(45, 800.0 / 600.0, 0.1, 50.0)
glTranslatef(0.0, 0.0, -12)
# glRotatef(45,1,1,1)
glutTimerFunc(50, timer, 1)
glutMainLoop()