import math
from ParticleClass import Particle
import numpy as np

G = 6.67E-11
h = 2E-6

def GravPot(pos, Particles, h):
    phi = 0.0
    for p in Particles:
        r = math.sqrt((pos[0]-p.pos[0])**2 + (pos[1]-p.pos[1])**2 + (pos[2]-p.pos[2])**2)
        if (r > h/2):
            phi += -G*p.m/r
    return phi

Particles = []
inFile = open("particlesLarge.txt", "r")
for line in inFile:
    x, y, z, m = line.split(" ")
    pos = np.array([float(x), float(y), float(z)])
    p = Particle(pos, float(m))
    Particles.append(p)
inFile.close()

def CentralDiffGrav(f, pos, h, i, Particles):
    step = np.zeros(3)
    step[i] = h/2
    r_1 = pos - step
    r_2 = pos + step
    return (f(r_2, Particles, h)-f(r_1, Particles, h))/h

# x, y, z = input("Where would you like to calculate gravitational force from? (x y z): ").split(" ")
# pos = np.array([float(x), float(y), float(z)])

outFile = open("particlesAccel.txt", "w")
for p in Particles:
    dfdx = -CentralDiffGrav(GravPot, p.pos, h, 0, Particles)
    dfdy = -CentralDiffGrav(GravPot, p.pos, h, 1, Particles)
    dfdz = -CentralDiffGrav(GravPot, p.pos, h, 2, Particles)
    outFile.write(str(dfdx) + " " + str(dfdy) + " " + str(dfdz) + "\n")
outFile.close()

print("The Acceleration is: ", dfdx, ", ", dfdy, ", ", dfdz)