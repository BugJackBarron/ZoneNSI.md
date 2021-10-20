from manim import *

class TableauManim :
    def __init__(self, tab, center, counterName="i", cP=0) :
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
    
    def changeColorNumber(self, position, color) :

        return ApplyMethod(self.values[position].set_color,  color)
    

        
    
        
        
        



class QueueWith2Stacks(Scene):
    def construct(self):
        
        ## Titre de la vidéo.
        titre = Text("Créer une file avec deux piles")
        self.play(Write(titre))
        self.wait(1)
        self.play(ApplyMethod(titre.shift,3*UP))
        self.play(FadeOut(titre))
        del(titre)
        
         # Signature de la vidéo
        ccby= ImageMobject("..\ccby.png").scale(0.3).to_corner(DL)
        signature = Tex(r"F. VERGNIAUD, www.zonensi.fr, 2021, made in Python with Manim, thx to Grant Sanderson and the Manim Community ").scale(0.3).next_to(ccby,RIGHT).set_color(GRAY)
        self.play(FadeIn(ccby, signature))
        
        baseObj = Rectangle(width=1, height=0.25)
        
        
        
        
        entrees = [baseObj.copy() for _ in range(4)]
        sorties = [baseObj.copy() for _ in range(3)]
        
        
        file = Rectangle(width = 6, height = 4).shift(DOWN)
        self.add(file)
        self.add(Text("La File").next_to(file, DOWN))
        
        for i, e in enumerate(entrees) :
            e.move_to(2*LEFT +0.25*i*UP)
            if i<3 :
                self.play(FadeIn(e), run_time=0.2)
            
        for i, e in enumerate(sorties) :
            e.move_to(2*RIGHT +0.25*i*UP)
            self.play(FadeIn(e), run_time=0.2)
            
        entryObj = baseObj.copy().move_to(4*LEFT + 3*UP)
        entryObj.set_color(GRAY)
        
        
        exitObj = baseObj.copy().move_to(4*RIGHT + 3*UP)
        exitObj.set_color(GRAY)
            
        entreesText = Text("Pile d'entrées").scale(0.5).next_to(entrees[0], DOWN)
        self.play(FadeIn(entreesText))
        sortiesText = Text("Pile de sorties").scale(0.5).next_to(sorties[0], DOWN)
        self.play(FadeIn(sortiesText))
        
        actualText=Text("On empile sur la pile d'entrées...").move_to(2*DOWN).scale(0.5).set_color(YELLOW)
        self.play(Write(actualText))
        self.play(TransformFromCopy(entryObj, entrees[3]))
        self.play(FadeOut(actualText))
        
        
        actualText=Text("On dépile sur la pile de sorties").move_to(2*DOWN).scale(0.5).set_color(YELLOW)
        self.play(Write(actualText))
        m = sorties.pop()
        self.play(Transform(m, exitObj))
        self.play(FadeOut(m))
        self.play(FadeOut(actualText))
        
        
        actualText=Text("Et on continue...").move_to(2*DOWN).scale(0.5).set_color(YELLOW)
        self.play(Write(actualText))
        m = sorties.pop()
        self.play(Transform(m, exitObj))
        self.play(FadeOut(m))
        m = sorties.pop()
        self.play(Transform(m, exitObj))
        self.play(FadeOut(m))
        self.play(FadeOut(actualText))
        
        actualText=Text("Et quand la pile de sortie est vide...").move_to(2*DOWN).scale(0.5).set_color(YELLOW)
        self.play(Write(actualText))
        self.play(FadeOut(actualText))
        
        actualText=Text("On dépile l'entrée sur la sortie.").move_to(2*DOWN).scale(0.5).set_color(YELLOW)
        self.play(Write(actualText))
        self.play(FadeOut(actualText))
        
        colors= [GREEN, BLUE, YELLOW, RED]
        
        sorties = [baseObj.copy() for _ in range(4)]
        for i, e in enumerate(sorties) :
            e.move_to(2*RIGHT +0.25*i*UP)
            
        for i in range(4) :
            self.play(ApplyMethod(entrees[i].set_color, colors[i]), run_time=0.2)
            sorties[3-i].set_color(colors[i])
            
        for i in range(4) :
            self.play(TransformFromCopy(entrees[3-i], sorties[i]))
            self.play(FadeOut(entrees[3-i]))
            
        actualText=Text("Et le premier de la pile de sorties...").move_to(2*DOWN).scale(0.5).set_color(YELLOW)
        self.play(Write(actualText))
        for _ in range(3) :
            self.play(FadeOut(sorties[-1]), run_time=0.2)
            self.play(FadeIn(sorties[-1]), run_time=0.2)
        self.play(FadeOut(actualText))
        
        
        actualText=Text("Est bien le le plus bas de la pile d'entrées...").move_to(2*DOWN).scale(0.5).set_color(YELLOW)
        actualText2=Text("Soit le premier inséré dans la pile d'entrées !").move_to(2.5*DOWN).scale(0.5).set_color(YELLOW)
        self.play(Write(actualText))
        
        self.add(VGroup(*entrees))
        for _ in range(3) :
            self.play(FadeOut(entrees[0]), run_time=0.2)
            self.play(FadeIn(entrees[0]), run_time=0.2)
        self.play(Write(actualText2))
        self.wait(2)
        self.play(FadeOut(VGroup(*entrees)))
        self.play(FadeOut(VGroup(actualText, actualText2)))
        
        
        actualText=Text("La structure est bien de type PEPS (FIFO)").move_to(2*DOWN).scale(0.5).set_color(YELLOW)
        self.play(Write(actualText))      
        
        
        self.wait(5)
            
        
        

        
        