from manim import *

class TableauManim :
    def __init__(self, tab, center, status=False, nextTM = None) :
        self.tab = tab
        self.center = center
        self.next = nextTM
        self.status = status
        
    def affiche(self) :
        rect = Rectangle(width=len(self.tab), height=1.0, grid_xstep=1.0)
        self.group = VGroup(rect)
        
        
        
class MergeSort(Scene):
    def construct(self):
        tab = TableauManim([2,3,4,], (1,2))
        tab.affiche()
        self.add(tab.group)
        