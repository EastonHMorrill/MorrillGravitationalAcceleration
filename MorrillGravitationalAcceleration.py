import math
import ParticleClass as PC

x_0, y_0, z_0 = input("Where would you like to calculate gravitational force from? (x y z): ").split(" ")
h = input("What is your time step?: ")
  
X = []
Y = []
Z = []
M = []
    
inFile = open("particleSmall.txt", "r")
for line in inFile:
    x, y, z, m = line.split(" ")
    X.append(float(x))
    Y.append(float(y))
    Z.append(float(z))
    M.append(float(m))
inFile.close()

def GravPot(x, y, z, PC):
    phi = 0.0
    for p in PC:
        r= math.sqrt((x_0 - p.x)**2 + (y_0 - p.y)**2 + (z_0 - p.z)**2)
        phi += -G*p.m/r
    return phi

def GravDeriv(f, x, y, z, h):
    ddx = (f(x+h/2, y, z)-f(x-h/2, y, z))/h
    ddy = (f(x, y+h/2, z)-f(x, y-h/2, z))/h
    ddz = (f(x, y, z+h/2)-f(x, y, z-h/2))/h
    return ddx, ddy, ddz

f = GravPot(x, y, z, PC)

print("The Gravitational Potential at " + x_0 + ", " + y_0 + ", " + z_0 + " is " + str(phi))
