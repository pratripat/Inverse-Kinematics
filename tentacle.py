from globals import *
from segment import Segment

class Tentacle:
    def __init__(self, children, starting_pos, length, base):
        self.children = children
        self.base = base
        self.s = Segment(*starting_pos, length)

        self.initialize_segments()

    def initialize_segments(self):
        #Initializing segments
        for i in range(self.children):
            self.s.add_segment()

    def run(self, target):
        #Making the segment follow the target
        self.s.follow(pygame.math.Vector2(*target))
        self.s.update()

        #Making the tentacle stay at a fixed point
        for i in range(self.children, -1, -1):
            child = self.s.get_segment(i)
            parent = self.s.get_segment(i+1)

            if i == self.children:
                child.setA(self.base)
            else:
                child.setA(parent.b)

        #Rendering all the tentacles
        self.s.show()
