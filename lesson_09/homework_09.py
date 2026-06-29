class Rhombus:
    def __setattr__(self, name, value):
        if name == 'side_a':
            if value <= 0:
                raise ValueError("Side must be greater than 0")
            object.__setattr__(self, name, value)
        elif name == 'angle_a':
            if value <= 0 or value >= 180:
                raise ValueError("Angle must be greater than 0 and less than 180")
            object.__setattr__(self, name, value)
            object.__setattr__(self, 'angle_b', 180 - value)
        elif name == 'angle_b':
            raise AttributeError("angle_b is calculated automatically by angle_a")
        else:
            object.__setattr__(self, name, value)
    def __str__(self):
        return (f"Rhombus: side_a={self.side_a}, "
                f"angle_a={self.angle_a}, "
                f"angle_b={self.angle_b}")
rhombus = Rhombus()
rhombus.side_a = 5
rhombus.angle_a = 80

print(rhombus)
print(f"side_a: {rhombus.side_a}")
print(f"angle_a: {rhombus.angle_a}")
print(f"angle_b: {rhombus.angle_b}")