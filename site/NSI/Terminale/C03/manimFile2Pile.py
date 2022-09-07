from manim import *


class QueueWith2Stacks(Scene):
    def construct(self):
        ## Titre de la vidéo.
        
        titre=Text("Créer une file à l'aide de deux piles")
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
        
        
        file = Rectangle(width = 7, height = 4).shift(UP)
        self.add(file)
        self.add(Text("La File avec deux piles").scale(0.5).next_to(file, DOWN))
           
        
        
        for i, e in enumerate(entrees) :
            e.move_to(2*LEFT +0.25*i*UP)
            if i<3 :
                self.play(FadeIn(e), run_time=0.2)
            
        for i, e in enumerate(sorties) :
            e.move_to(2*RIGHT +0.25*i*UP)
            self.play(FadeIn(e), run_time=0.2)
            
        
        queueLine = Line(start=np.array([-5.5, 2.9,0]), end = np.array([-4.5, 2.9, 0]))
        self.add(queueLine)
        self.add(Text("Queue").scale(0.5).next_to(queueLine, DOWN, buff=SMALL_BUFF))
        headLine = Line(start=np.array([4.5, 2.9,0]), end = np.array([5.5, 2.9, 0]))
        self.add(headLine)
        self.add(Text("Tête").scale(0.5).next_to(headLine, DOWN, buff=SMALL_BUFF))
       
        entryObj = baseObj.copy().next_to(queueLine, UP)
        entryObj.set_color(GRAY)
        
        exitObj = baseObj.copy().next_to(headLine, UP)
        exitObj.set_color(GRAY)
            
        entreesText = Text("Pile d'entrées").scale(0.5).next_to(entrees[0], DOWN)
        self.play(FadeIn(entreesText))
        sortiesText = Text("Pile de sorties").scale(0.5).next_to(sorties[0], DOWN)
        self.play(FadeIn(sortiesText))
        
        actualText=Text("Pour enfiler un élément,").move_to(2*DOWN).scale(0.5).set_color(YELLOW)
        self.play(Write(actualText))
        self.play(FadeIn(entryObj))
        self.play(FadeOut(actualText))
        
        
        actualText=Text("on l'empile sur la pile d'entrées...").move_to(2*DOWN).scale(0.5).set_color(YELLOW)
        self.play(Write(actualText))
        self.play(TransformFromCopy(entryObj, entrees[3]))
        self.play(FadeOut(entryObj))
        self.play(FadeOut(actualText))
        
        actualText=Text("Pour défiler un élément, ").move_to(2*DOWN).scale(0.5).set_color(YELLOW)
        self.play(Write(actualText))
        self.play(FadeOut(actualText))
        
        actualText=Text("on dépile depuis la pile de sorties.").move_to(2*DOWN).scale(0.5).set_color(YELLOW)
        self.play(Write(actualText))
        m = sorties.pop()
        self.play(Transform(m, exitObj))
        self.play(FadeOut(m))
        self.play(FadeOut(actualText))
        
        
        actualText=Text("Et on peut continuer...").move_to(2*DOWN).scale(0.5).set_color(YELLOW)
        self.play(Write(actualText))
        m = sorties.pop()
        self.play(Transform(m, exitObj))
        self.play(FadeOut(m))
        m = sorties.pop()
        self.play(Transform(m, exitObj))
        self.play(FadeOut(m))
        self.play(FadeOut(actualText))
        
        actualText=Text("jusqu'au moment où la pile de sortie est vide...").move_to(2*DOWN).scale(0.5).set_color(YELLOW)
        self.play(Write(actualText))
        self.play(FadeOut(actualText))
        
        actualText=Text("Pour poursuivre,").move_to(2*DOWN).scale(0.5).set_color(YELLOW)
        self.play(Write(actualText))
        self.play(FadeOut(actualText))
        
        
        actualText=Text("on doit dépiler l'entrée sur la sortie.").move_to(2*DOWN).scale(0.5).set_color(YELLOW)
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
        
        
        actualText=Text("La structure est bien de type PEPS (FIFO) !").move_to(2*DOWN).scale(0.5).set_color(YELLOW)
        self.play(Write(actualText))      
        
        
        self.wait(5)
            
        
        

        
        