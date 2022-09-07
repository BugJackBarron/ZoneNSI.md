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
    

        
    
        
        
        



class MergeAlgo(Scene):
    def construct(self):
        
        ## Titre de la vidéo.
        titre = Text("How to Merge 2 Sorted Arrays")
        self.play(Write(titre))
        self.wait(1)
        self.play(ApplyMethod(titre.shift,3*UP))
        self.play(FadeOut(titre))
        del(titre)
        
         # Signature de la vidéo
        ccby= ImageMobject("ccby.png").scale(0.3).to_corner(DL)
        signature = Tex(r"F. VERGNIAUD, www.zonensi.fr, 2021, made in Python with Manim, thx to Grant Sanderson and the Manim Community ").scale(0.3).next_to(ccby,RIGHT).set_color(GRAY)
        self.play(FadeIn(ccby, signature))
        
        
        tab1 = TableauManim([17,37,45,47,62,85], (0,2.5))
        tab2 = TableauManim([11,28,59], (0,0), counterName="j")
        tabf = TableauManim([0]*9, (0,0), counterName="k")
        
        VGroup(tab1.group, tab2.group, tabf.group).arrange(DOWN,  center=False, aligned_edge=LEFT)
        
        self.play(FadeIn(tab1.group, tab2.group, tabf.group))
        
        i, j, k = 0, 0, 0
        while i<len(tab1.tab) or j<len(tab2.tab) :
            if i<len(tab1.tab) and j<len(tab2.tab) :
                if tab1.tab[i]< tab2.tab[j] :
                    tabf.tab[k] = tab1.tab[i]
                    self.play(tab1.changeColorNumber(i, GREEN), tab2.changeColorNumber(j, RED))
                    self.wait(0.5)
                    tabf.values[k].set_value(tabf.tab[k])
                    self.play(TransformFromCopy(tab1.values[i], tabf.values[k]))
                    i+=1
                    k+=1
                    self.play(tab1.movecounter(i))
                    self.play(tabf.movecounter(k))
                else :
                    tabf.tab[k] = tab2.tab[j]
                    self.play(tab2.changeColorNumber(j, GREEN), tab1.changeColorNumber(i, RED))
                    self.wait(0.5)
                    tabf.values[k].set_value(tabf.tab[k])
                    self.play(TransformFromCopy(tab2.values[j], tabf.values[k]))
                    j+=1
                    k+=1
                    self.play(tab2.movecounter(j))
                    self.play(tabf.movecounter(k))
                    
            elif i<len(tab1.tab) :
                tabf.tab[k] = tab1.tab[i]
                self.play(tab1.changeColorNumber(i, GREEN))
                self.wait(0.5)
                tabf.values[k].set_value(tabf.tab[k])
                self.play(TransformFromCopy(tab1.values[i], tabf.values[k]))
                i+=1
                k+=1
                self.play(tab1.movecounter(i))
                self.play(tabf.movecounter(k))
            elif j<len(tab2.tab):
                tabf.tab[k] = tab2.tab[j]
                self.play(tab2.changeColorNumber(j, GREEN))
                self.wait(0.5)
                tabf.values[k].set_value(tabf.tab[k])
                self.play(TransformFromCopy(tab2.values[j], tabf.values[k]))
                j+=1
                k+=1
                self.play(tab2.movecounter(j))
                self.play(tabf.movecounter(k))
        
        
        self.wait(5)
        
        