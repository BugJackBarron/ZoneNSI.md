from manim import *

class TableauManim :
    def __init__(self, tab, center = (0,0), counterName="i", cP=0) :
        self.tab = tab
        self.center = center
        self.counterName = counterName
        self.rect = Rectangle(width=len(self.tab), height=1.0, grid_xstep=1.0)
        self.values = [DecimalNumber(v, num_decimal_places=0).scale(0.75).move_to((-(len(self.tab)//2)+((len(self.tab)+1)%2)*0.5+i)*RIGHT) for i,v in enumerate(self.tab)]       
        self.counterPosition = cP
        self.pointerText = Text(f"{self.counterName} = ").move_to((-(len(self.tab)//2)+((len(self.tab)+1)%2)*0.5+self.counterPosition)*RIGHT+1.5*DOWN).scale(0.5)
        self.pointer = Arrow(start =np.array([0,0,0]), end = np.array([0,1,0])).scale(0.7).next_to(self.pointerText ,UP)
        self.pointerCounter = DecimalNumber(0, num_decimal_places=0).scale(0.75)
        self.pointerCounter.add_updater(lambda d : d.next_to(self.pointerText, RIGHT, buff=SMALL_BUFF))
        self.pointerCounter.add_updater(lambda d : d.set_value(self.counterPosition))
        
        self.pointerGroup = VGroup(self.pointerCounter, self.pointerText, self.pointer)
        
        self.group = VGroup(self.rect, *self.values, self.pointerGroup).scale(0.75)
        self.group.move_to(center[0]*RIGHT+center[1]*UP)
        
    def movecounter(self, np) :
        move = np-self.counterPosition
        self.counterPosition = np
        return ApplyMethod(self.pointerGroup.shift, move*RIGHT*0.75)
    
    def movenumber(self, indice, direction=RIGHT) :
        pass
        
    
    def changeColorNumber(self, position, color) :

        return ApplyMethod(self.values[position].set_color,  color)
    

        
    
        
        
        



class addFirstElement(Scene):
    def construct(self):
        
        ## Titre de la vidéo.
#        titre = Text("How to Merge 2 Sorted Arrays")
#        self.play(Write(titre))
#        self.wait(1)
#        self.play(ApplyMethod(titre.shift,3*UP))
#        self.play(FadeOut(titre))
#        del(titre)
        
         # Signature de la vidéo
#        ccby= ImageMobject("ccby.png").scale(0.3).to_corner(DL)
#        signature = Tex(r"F. VERGNIAUD, www.zonensi.fr, 2021, made in Python with Manim, thx to Grant Sanderson and the Manim Community ").scale(0.3).next_to(ccby,RIGHT).set_color(GRAY)
#        self.play(FadeIn(ccby, signature))
        
        
        tab1 = TableauManim([17,37,45,47,62,85], cP = 5)
        tab2 = TableauManim([17,37,45,47,62,85, None], cP = 5)
        
        
        self.add(tab1)
        self.add(tab2)
        
        