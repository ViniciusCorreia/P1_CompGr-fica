from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

N = 5
r = 2
ang = (2 * math.pi) / N


def vertices():
    vertice = []

    for i in range(2 * N):

        aux = []
        if (i >= N):
            x = r * math.cos(i * ang)
            z = r * math.sin(i * ang)

            aux.append(x)
            aux.append(0)
            aux.append(z)

            vertice.append(aux)
        else:
            x = r * math.cos(i * ang)
            z = r * math.sin(i * ang)

            aux.append(x)
            aux.append(5)
            aux.append(z)

            vertice.append(aux)

    return vertice


def linhas():
    linha = []
    base = []
    base1 = []
    getvertice = []
    getvertice = vertices()

    # Construcao das linhas do topo
    for i in range(N):
        aux = []

        if (i == N - 1):
            aux.append(getvertice[i])
            aux.append(getvertice[0])
            linha.append(aux)

        else:
            aux.append(getvertice[i])
            aux.append(getvertice[i + 1])

            linha.append(aux)

    # Construcao das linhas da base.
    for i in range(2 * N):
        aux = []

        if (i == (2 * N) - 1):
            aux.append(getvertice[i])
            aux.append(getvertice[N])

            linha.append(aux)

        if (i >= N and i < 2 * N - 1):
            aux.append(getvertice[i])
            aux.append(getvertice[i + 1])

            linha.append(aux)

    # Contrucao linhas topo base.
    for i in range(N):
        aux = []

        aux.append(getvertice[i])
        aux.append(getvertice[i + N])

        linha.append(aux)

    # Construcao das linhas do centro topo aos vertices do topo.
    base.append(0)
    base.append(5)
    base.append(0)

    for i in range(N):
        aux = []
        aux.append(base)
        aux.append(getvertice[i])
        linha.append(aux)

    # Construcao das linhas centro base aos vertices da base.
    base1.append(0)
    base1.append(0)
    base1.append(0)

    for i in range(2 * N):
        aux = []
        if (i == N):
            break
        else:
            aux.append(base1)
            aux.append(getvertice[N + i])
            linha.append(aux)

    return linha


def faces():
    base = []
    base1 = []
    face = []
    getvertice = []
    getvertice = vertices()

    # Criando faces laterais de maneira triangular.
    for i in range(N):
        aux = []
        for x in range(2):
            if (i < N - 1):
                if (x == 1):
                    aux.append(getvertice[i])
                    aux.append(getvertice[i + x])
                    aux.append(getvertice[N + i + x])
                    face.append(aux)

                if (x == 0):
                    aux.append(getvertice[i])
                    aux.append(getvertice[N + i])
                    aux.append(getvertice[N + i + 1])
                    face.append(aux)

            if (i == N - 1):
                if (x == 0):
                    aux.append(getvertice[N - 1])
                    aux.append(getvertice[2 * N - 1])
                    aux.append(getvertice[N])
                    face.append(aux)
                if (x == 1):
                    aux.append(getvertice[N - 1])
                    aux.append(getvertice[0])
                    aux.append(getvertice[N])
                    face.append(aux)

    # Construcao das faces superiores de maneira triangular.
    base.append(0)
    base.append(5)
    base.append(0)


    for i in range(N):
        aux = []
        if (i == N - 1):
            aux.append(base)
            aux.append(getvertice[i])
            aux.append(getvertice[0])
            face.append(aux)
        else:
            aux.append(base)
            aux.append(getvertice[i])
            aux.append(getvertice[i + 1])
            face.append(aux)

            # Construcao das faces inferiores de maneira triangular.
    base1.append(0)
    base1.append(0)
    base1.append(0)

    for i in range(2 * N):
        aux = []
        if (i == 2 * N - 1):
            aux.append(base1)
            aux.append(getvertice[i])
            aux.append(getvertice[N])
            face.append(aux)
        if (i >= N and i < 2 * N - 1):
            aux.append(base1)
            aux.append(getvertice[i])
            aux.append(getvertice[i + 1])
            face.append(aux)

    return face


cores = ((1, 0, 0), (1, 1, 0), (0, 1, 0), (0, 1, 1), (0, 0, 1), (1, 0, 1), (0.5, 1, 1), (1, 0, 0.5))


def Prisma():
    i = 0
    getvertices = []
    getlinhas = []
    getfaces = []
    getvertices = vertices()
    getlinhas = linhas()
    getfaces = faces()

    glBegin(GL_TRIANGLES)
    for face in getfaces:
        for vertex in face:
            if (i > 2 * N - 1):
                glColor3fv(cores[5])
            else:
                glColor3fv(cores[3])
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
    Prisma()
    glPopMatrix()
    glutSwapBuffers()
    a += 1


def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50, timer, 1)


# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800, 600)
glutCreateWindow("Prisma")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0., 0., 0., 1.)
gluPerspective(45, 800.0 / 600.0, 0.1, 50.0)
glTranslatef(0.0, 0.0, -12)
glRotatef(45, 1, 1, 1)
glutTimerFunc(50, timer, 1)
glutMainLoop()