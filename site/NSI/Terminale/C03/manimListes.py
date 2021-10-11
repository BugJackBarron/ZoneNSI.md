from manim import *

class TableauManim :
    def __init__(self, tab, center = (0,0)) :
        self.tab = tab
        self.center = center
        self.rect = Rectangle(width=len(self.tab), height=1.0, grid_xstep=1.0)
        self.values = [DecimalNumber(v, num_decimal_places=0).scale(0.75).move_to((-(len(self.tab)//2)+((len(self.tab)+1)%2)*0.5+i)*RIGHT) for i,v in enumerate(self.tab)]       
        self.group = VGroup(self.rect, *self.values).scale(0.75)
        self.group.move_to(center[0]*RIGHT+center[1]*UP)
        
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
        
        
        tab1 = TableauManim([17,37,45,47,62,85])
        
        
        
        tab2 = TableauManim([17,37,45,47,62,85, 0])
        tab3 = TableauManim([55,17,37,45,47,62,85])
        VGroup(tab1.group, tab2.group, tab3.group).arrange(direction=np.array([0., 0., 0.]), center=False, aligned_edge=LEFT)  
        tabI = TableauManim([0])
        tabI.group.next_to(tab1.group, RIGHT, buff=0)
        
        
        self.add(tab1.group)
        self.wait(1)
        self.play(FadeIn(tabI.group))
        self.wait(1)
        self.remove(tab1.group)
        self.remove(tabI.group)
        self.add(tab2.group)
        
        for i in reversed(range(0,len(tab2.tab)-1)) :
            self.play(Transform(tab2.values[i], tab3.values[i+1]))
            if i==len(tab2.tab)-1 :
                tab2[-1] = tab3[-1]
        
        self.wait(5)
        
        