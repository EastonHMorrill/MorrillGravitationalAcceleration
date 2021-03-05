import math

class Particle:
    def __init__(self, x, y, z, m, v_x, v_y, v_z):
        self.x = x
        self.y = y
        self.z = z
        self.m = m
        self.v_x = v_x
        self.v_y = v_y
        self.v_z = v_z
        return x, y, z, m, v_x, v_y, v_z