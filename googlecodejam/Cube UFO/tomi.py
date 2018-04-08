from math import sin, cos
import matplotlib.pyplot as plt
import matplotlib.lines as lines

class Point2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cords = (x,y)

class Point3d:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.cords = (x,y,z)

    def rotate(self, axis, angle, rotCenter):
        # dejo fijo el eje sobre el que se rota
        if axis == 'x': # hay que fijar x y el plano de rotacion es (y, z)
            rot_cordU = 1
            rot_cordV = 2
            axis_cord = 0
        elif axis == 'y': # hay que fijar y y el plano de rotacion es (x, z)
            rot_cordU = 0
            rot_cordV = 2
            axis_cord = 1
        elif axis == 'z': # hay que fijar z y el plano de rotacion es (x, y)
            rot_cordU = 0
            rot_cordV = 1
            axis_cord = 2

        # guardo valores (u, v) para rotar en el plano y dejo fijo el eje j
        u = self.cords[rot_cordU]
        v = self.cords[rot_cordV]
        j = self.cords[axis_cord]

        # guardo el centro de rotacion (u, v) en el plano y dejo fijo el eje j
        rotCenterU = rotCenter.cords[rot_cordU]
        rotCenterV = rotCenter.cords[rot_cordV]
        rotCenterJ = rotCenter.cords[axis_cord]

        s = sin(angle)
        c = cos(angle)

        # trasladar el punto al origen
        u -= rotCenterU
        v -= rotCenterV

        # rotar el punto respecto del origen
        u_new = u * c - v * s
        v_new = u * s + v * c

        # trasladar a la pocicion original
        u = u_new + rotCenterU
        v = v_new + rotCenterV

        # aplico los cambios
        if rot_cordU == 0: self.x = u
        elif rot_cordU == 1: self.y = u
        elif rot_cordU == 2: self.z = u
        if rot_cordV == 0: self.x = v
        elif rot_cordV == 1: self.y = v
        elif rot_cordV == 2: self.z = v
        if axis_cord == 0: self.x = j
        elif axis_cord == 1: self.y = j
        elif axis_cord == 2: self.z = j

        self.cords = (self.x, self.y, self.z)


class Face:
    def __init__(self, p1, p2, p3, p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4

    def rotate(self, axis, angle):
        rotCenter = Point3d(0,0,0)
        self.p1.rotate(axis, angle, rotCenter)
        self.p2.rotate(axis, angle, rotCenter)
        self.p3.rotate(axis, angle, rotCenter)
        self.p4.rotate(axis, angle, rotCenter)

    def midPoint(self):
        x = (self.p1.x + self.p2.x + self.p3.x + self.p4.x) / 4
        y = (self.p1.y + self.p2.y + self.p3.y + self.p4.y) / 4
        z = (self.p1.z + self.p2.z + self.p3.z + self.p4.z) / 4
        return Point3d(x, y, z)


class Cube:
    def __init__(self):
        self.f1 = Face(Point3d(.5,.5,.5),Point3d(.5,-.5,.5),Point3d(.5,-.5,-.5),Point3d(.5,.5,-.5)) # fijo x
        self.f2 = Face(Point3d(-.5,.5,.5),Point3d(-.5,-.5,.5),Point3d(-.5,-.5,-.5),Point3d(-.5,.5,-.5)) # fijo -x
        self.f3 = Face(Point3d(.5,.5,.5),Point3d(-.5,.5,.5),Point3d(-.5,.5,-.5),Point3d(.5,.5,-.5)) # fijo y
        self.f4 = Face(Point3d(.5,-.5,.5),Point3d(-.5,-.5,.5),Point3d(-.5,-.5,-.5),Point3d(.5,-.5,-.5)) # fijo -y
        self.f5 = Face(Point3d(.5,.5,.5),Point3d(-.5,.5,.5),Point3d(-.5,-.5,.5),Point3d(.5,-.5,.5)) # fijo z
        self.f6 = Face(Point3d(.5,.5,-.5),Point3d(-.5,.5,-.5),Point3d(-.5,-.5,-.5),Point3d(.5,-.5,-.5)) # fijo -z
        # los vetex son los puntos de f1 y f2
        self.vertex = [self.f1.p1,
                       self.f1.p2,
                       self.f1.p3,
                       self.f1.p4,
                       self.f2.p1,
                       self.f2.p2,
                       self.f2.p3,
                       self.f2.p4]
        # los edges son la union de cada punto de la cara f1 y f2 con el punto que le sigue de la misma cara y las uniones entre puntos iguales entre caras
        self.edges = [(self.f1.p1,self.f1.p2),
                      (self.f1.p2,self.f1.p3),
                      (self.f1.p3,self.f1.p4),
                      (self.f1.p4,self.f1.p1),
                      (self.f2.p1,self.f2.p2),
                      (self.f2.p2,self.f2.p3),
                      (self.f2.p3,self.f2.p4),
                      (self.f2.p4,self.f2.p1),
                      (self.f1.p1,self.f2.p1),
                      (self.f1.p2,self.f2.p2),
                      (self.f1.p3,self.f2.p3),
                      (self.f1.p4,self.f2.p4)]

    def rotate(self, axis, angle):
        self.f1.rotate(axis, angle)
        self.f2.rotate(axis, angle)
        self.f3.rotate(axis, angle)
        self.f4.rotate(axis, angle)
        self.f5.rotate(axis, angle)
        self.f6.rotate(axis, angle)

    def proyect(self, axis):
        if axis == 'x': # el resultado es un punto proyectado (y, z)
            rot_cordU = 1
            rot_cordV = 2
        elif axis == 'y': # el resultado es un punto proyectado (x, z)
            rot_cordU = 0
            rot_cordV = 2
        elif axis == 'z': # el resultado es un punto proyectado (x, y)
            rot_cordU = 0
            rot_cordV = 1

        # devuelvo un lista de Point2d proyectados en el plano axis
        lis = []
        for p in self.vertex:
            lis.append(Point2d(p.cords[rot_cordU],p.cords[rot_cordV]))
        return lis

    def proyectPerimeter(self, axis):
        lis = self.proyect(axis)
        #TODO quedarme con los Point2d en la lista que pertencen al perimetro

    def shadowArea(self, axis):
        lis = self.proyectPerimeter(axis)

    def plotProyection(self, axis):
        x = []
        y = []
        for p in self.proyect(axis):
            x.append(p.cords[0])
            y.append(p.cords[1])

        plt.scatter(x, y)
        plt.show()

    def plotProyection2(self, axis):
        if axis == 'x': # el resultado es un punto proyectado (y, z)
            cordU = 1
            cordV = 2
        elif axis == 'y': # el resultado es un punto proyectado (x, z)
            cordU = 0
            cordV = 2
        elif axis == 'z': # el resultado es un punto proyectado (x, y)
            cordU = 0
            cordV = 1

        fig = plt.figure()
        lis_lines = []
        for e in self.edges:
            lis_lines.append(lines.Line2D([e[0].cords[cordU], e[1].cords[cordU]], [e[0].cords[cordV], e[1].cords[cordV]],
                                          transform=fig.transFigure,figure=fig))

        fig.lines.extend(lis_lines)

        plt.show()


C = Cube()
C.rotate('y',30)
C.rotate('x',4)
lis = C.proyect('z')
for p in lis:
    print("x:{:.12f} | y:{:.12f}".format(p.x,p.y))
C.plotProyection2('z')
