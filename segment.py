from globals import *
import math

class Segment:
    def __init__(self, x, y, length):
        self.a = pygame.math.Vector2(x, y)
        self.b = pygame.math.Vector2()
        self.angle = 0
        self.child = None
        self.len = length

    def update(self):
        #Updating position b according to the angle
        v = pygame.math.Vector2(math.cos(self.angle), math.sin(self.angle))
        v *= self.len
        v += self.a
        self.b = v

    def follow(self, target):
        #Moving and rotating towards the target
        dx = self.a.x - target.x
        dy = self.a.y - target.y

        self.angle = math.atan2(-dx, dy) - math.pi/2

        dir = pygame.math.Vector2(math.cos(self.angle), math.sin(self.angle))
        dir *= self.len
        dir *= -1
        self.a = target+dir

        if self.child:
            self.child.follow(self.a)
            self.child.update()

    def show(self):
        #Rendering self and child
        pygame.draw.line(screen, white, self.a, self.b)

        if self.child:
            self.child.show()

    def add_segment(self):
        #Adding children to self
        if not self.child:
            self.child = Segment(self.b.x, self.b.y, self.len)
        #Adding children to self child
        else:
            self.child.add_segment()

    def get_segment(self, depth):
        #Returning back Segment according to depth
        if depth == 0 or not self.child:
            return self
        else:
            return self.child.get_segment(depth-1)

    def setA(self, pos):
        #Sets the position a to given position
        self.a = pygame.math.Vector2(pos.x, pos.y)
        self.update()
