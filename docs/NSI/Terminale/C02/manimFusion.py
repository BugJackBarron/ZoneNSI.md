from manim import *

class TableauManim :
    def __init__(self, tab, center, counterName="i", cP=0) :
        self.tab = tab
        self.center = center
        self.counterName = counterName
        self.rect = Rectangle(width=len(self.tab), height=1.0, grid_xstep=1.0)
        self.values = [Text(str(v)).scale(0.75).move_to((-(len(self.tab)//2)+i)*RIGHT) for i,v in enumerate(self.tab)]
        self.counterPosition = cP
        self.pointerCounter = Text(f"{self.counterName} = {self.counterPosition}").move_to((-(len(self.tab)//2)+self.counterPosition)*RIGHT+1.5*DOWN).scale(0.5)
        self.pointer = Arrow(start =np.array([0,0,0]), end = np.array([0,1,0])).scale(0.7).next_to(self.pointerCounter, UP)
        
        self.group = VGroup(self.rect, *self.values, self.pointerCounter, self.pointer).scale(0.75)
        self.group.move_to(center[0]*RIGHT+center[1]*UP)



class MergeAlgo(Scene):
    def construct(self):
        tab1 = TableauManim([17,37,45,72,85], (0,2.5))
        tab2 = TableauManim([11,28,59], (-0.75,0.5), counterName="j", cP=2)
        
        tabf = TableauManim([" "]*7, (0.75,-1.5), counterName="k")
        self.add(tab1.group, tab2.group, tabf.group)
        
        