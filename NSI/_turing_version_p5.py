import p5
from copy import deepcopy


###############################################
# authors : Laurent Freguin, Fabien Vergniaud #
#                                             #
#    2023-2024                                #
#                                             #
###############################################

class TuringBase:
    def __init__(self, tape : list, states : list, pointer_start = 0):
        '''Build a Turing Machine 
        - tape : type list, start state of the Turing Machine, each element if None, 0 or 1 ;
        - states : type list, each cell contains a dictionary based on the following construction :
             r : (w, m, next_state), where
             * r is the value read on the current pointer position (None, 0 or 1);
             * w is the value that will be written on that position (None, 0 or 1);
             * next_state is the index of the next state of the machine. Possibly -1 if it's the final state.
        '''
        self.tape = tape
        self.states = states
        self.n = len(self.tape)
        self.pointer = pointer_start
        self.current_state = 0
    
    def write(self, value):
        '''write the value on the cell pointed by the pointer'''
        self.tape[self.pointer] = value # 
    
    def read(self):
        '''return the value read on the cell pointed by the pointer'''
        return self.tape[self.pointer] 
    
    def show_tape(self):
        """ print the tape"""
        print(self.tape)
    
    def move(self, d : int):
        '''move the pointer to the right (d=1) or to the left (d=-1).
        if the pointer get out of the tape, go on the opposite side        
        '''
        self.pointer += d
        self.pointer = self.pointer%self.n
        
    def pre_process(self):
        '''return the next state of the machine, 
        without processing it.
        '''
        reading = self.read() 
        dic_actions = self.states[self.current_state]
        if reading not in dic_actions :
            raise ValueError("Impossible action")
        return dic_actions[reading]
    
    def transition(self):
        '''Process the transition to the next state'''
        w, m, next_state = self.pre_process()
        self.write(w)
        self.move(m)
        self.current_state = next_state
        
    def execute(self):
        """Execute the program given to the machine, until it finish (if it finish)"""
        while self.current_state != -1:
            self.transition() 
            self.show_tape()
            

class Button :
    
    def __init__(self, x : int, y :int, 
                 x_size : int, y_size : int,
                 text : str,
                 bg_color : str = 'GRAY', text_color :str ='BLACK') :
        """ Create a button, with the following arguments :
        - x, y : poition of the top left corner ;
        - x_size, y_size : size of the button, in pixels ;
        - text : text of the button ;
        - bg_color, text_color : string which represent a color (must match colors from TuringGui)        
        """
        self.x = x
        self.y = y
        self.x_size = x_size
        self.y_size = y_size
        self.text = text
        self.bg_color = bg_color
        self.text_color = text_color       
        
        
    def draw(self, bg_color=None, text_color = None) :
        """ draw the button """
        if not bg_color : bg_color=self.bg_color
        if not text_color : text_color=self.text_color
        p5.fill(TuringGui.colors[bg_color])
        p5.stroke(0)
        p5.rect(self.x, self.y, self.x_size, self.y_size)
        p5.fill(TuringGui.colors[text_color])
        p5.stroke(TuringGui.colors[text_color])
        p5.text(self.text, self.x+self.x_size//2, self.y + self.y_size//2)
        
    def __contains__(self, pos : tuple) -> bool :
        """ return a boolean if the position given by the argument pos (a tuple) is inside the button"""
        posx, posy = pos
        return self.x<= posx <= self.x+self.x_size and self.y<= posy <= self.y+self.y_size


class TuringGui :
    """ Build a Turing Machine with Capytale P5 module"""
    # 
    colors={'WHITE' : (255, 255, 255),
            'BLACK' : (0, 0, 0),
            'GRAY' : (150,150,150),
            'RED' : (255, 0, 0),
            'ORANGE' : (255,140,0),
            'PURPLE' :(255,0,255),
            'GREEN' : (0, 255, 0),
            'BLUE' : (0, 0, 255),
            'YELLOW' : (255,255,0),
            'CYAN' : (0,255,255)
                    }
    # Possible status of a machine
    status = {'started' : 'BLACK',
             'move' : 'ORANGE',
             'change' :'GREEN',
              'next_state' :'GREEN',
             'error' : 'RED',
             'finished' : 'CYAN',
             'read' : 'BLUE',
             'write' : 'PURPLE'}
    # steps of a state
    steps = ['read', 'write', 'move', 'next_state', 'change']
    
    def __init__(self, T, width : int = 1000, height : int = 400, tempo : int = 750) :
        """ Build a GUI for a Turing machine, with the following arguments
        - T : an object of Turing class ;
        - width, height : dimension of the P5 window ;
        - tempo : an integer, the number of milliseconds between two actions        
        """
        
        self.machine = T
        self.SCREEN_WIDTH = width   
        self.SCREEN_HEIGHT = height 
        self.X_SHIFT = 20 # shift of the left border of the tape
        self.Y_SHIFT = 50 # shift of the top border oof the tape
        self.CELL_SIZE = max(10,(self.SCREEN_WIDTH-2*self.X_SHIFT)//self.machine.n)        
        self.step = 0 # firts step, read
        self.auto_move = False
        self.tape = deepcopy(self.machine.tape)
        self.pointer_position = self.machine.pointer        
        self.next_step_button = Button (self.SCREEN_WIDTH-self.X_SHIFT*6, 10,self.X_SHIFT*5, 40, "NEXT" )
        self.auto_move_button = Button (self.SCREEN_WIDTH-self.X_SHIFT*11, 10,self.X_SHIFT*5, 40, "AUTO" )
        self.last_click = 0 # time of last click 
        self.status = 'started' # actual status of the machine
        self.tempo = tempo # time in milliseconds between two actions
        
        
    def setup(self) :
        """ P5 setup function"""
        p5.createCanvas(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)    
        p5.background(TuringGui.colors['GRAY'])
        p5.stroke(TuringGui.colors['BLACK'])
        p5.fill(TuringGui.colors['GRAY'])
        p5.textAlign(p5.CENTER)
        
        
    def draw_cell(self, x, y, cell_value, case_color = 'BLACK',  number_color = 'BLACK'):
        """ draw a celll of the tape"""
        p5.stroke(TuringGui.colors[case_color])
        p5.fill(TuringGui.colors['WHITE'])
        p5.rect(x,y, self.CELL_SIZE, self.CELL_SIZE)
        p5.stroke(TuringGui.colors[number_color])
        p5.fill(TuringGui.colors[number_color])
        p5.text(cell_value, x+self.CELL_SIZE//2, y+self.CELL_SIZE//2)
        
            
        
    def draw_tape(self) :
        """ draw the tape"""
        p5.textSize(12)
        for i in range(self.machine.n) :
            if i == self.pointer_position :
                if self.status == 'started' : # status is needed for the cell color
                    status = TuringGui.steps[self.step]
                else :
                    status = self.status
                cell_value = self.tape[i]  
                self.draw_cell(self.X_SHIFT+self.CELL_SIZE*i, self.Y_SHIFT, cell_value,
                               case_color=TuringGui.status[status], number_color = TuringGui.status[status])
            else :
                self.draw_cell(self.X_SHIFT+self.CELL_SIZE*i, self.Y_SHIFT,self.tape[i])
            
    def draw_pointer(self) :
        """ draw the pointer"""
        i = self.pointer_position
        if self.status == 'started' :
            status = TuringGui.steps[self.step]
        else :
            status = self.status
        tip_x, tip_y = (self.X_SHIFT+(i+0.5)*self.CELL_SIZE, self.Y_SHIFT+self.CELL_SIZE)
        left_tip_x, left_tip_y = tip_x - self.CELL_SIZE//4, tip_y + self.CELL_SIZE//2
        right_tip_x, right_tip_y = tip_x + self.CELL_SIZE//4, tip_y + self.CELL_SIZE//2
        p5.stroke(TuringGui.colors[TuringGui.status[status]])
        p5.fill(TuringGui.colors[TuringGui.status[status]])
        p5.triangle(tip_x, tip_y, left_tip_x, left_tip_y, right_tip_x, right_tip_y)
    
    
    def draw_table_description(self,base_point_x, base_point_y, col_number = 0) :
        """ draw the firts line of a table of states"""
        texts = ["current state", "read", "write", "move", "next state"]         
        for i in range(5) :
            p5.fill(TuringGui.colors["WHITE"])
            p5.stroke(TuringGui.colors["BLACK"])
            p5.rect(base_point_x+i*60, base_point_y, 60,20)
            p5.stroke(TuringGui.colors["BLACK"])
            p5.fill(TuringGui.colors["BLACK"])
            p5.text(texts[i], base_point_x+i*60+30, base_point_y+10)
            
    def draw_tables_cell(self, bpx, bpy, w, h, content, highlight_step, current_state, read = False) :
        """ draw one cell of the states table"""
        if self.machine.current_state == current_state and read and(
            TuringGui.steps[self.step] == highlight_step or self.status == 'error'):            
            color = TuringGui.colors[TuringGui.status[TuringGui.steps[self.step]]]
        else :
            color = TuringGui.colors['BLACK']
        p5.fill(TuringGui.colors['WHITE'])
        p5.stroke(color)
        p5.rect(bpx, bpy,w,h)
        p5.fill(color)                 
        p5.text(content, bpx+w//2, bpy+h//2)
        
    
    def draw_states_table_column(self, col_number = 0) :
        """ Draw one column of states table (firts col is for states 0 to 2, second col for states 3 to 5)"""
        bpx = self.X_SHIFT + col_number*self.SCREEN_WIDTH//2
        bpy = 2*self.Y_SHIFT+self.CELL_SIZE
        self.draw_table_description(bpx, bpy, col_number)
        value_read = self.machine.tape[self.machine.pointer]
        for n in range(min(len(self.machine.states)-3*col_number,3)) :
            state_to_draw = n+col_number*3
            self.draw_tables_cell(bpx, bpy+20+n*60, 60, 60, f"e{state_to_draw}", 'change', state_to_draw, True)
            if None in self.machine.states[state_to_draw] :
                r = "None"
                w,m,c = self.machine.states[state_to_draw][None]
            else :
                r,w,m,c = ("","","","")
            self.draw_tables_cell(bpx+60, bpy+20+n*60, 60, 20, r, 'read', state_to_draw, value_read == None)
            self.draw_tables_cell(bpx+120, bpy+20+n*60, 60, 20, w, 'write', state_to_draw, value_read == None)
            self.draw_tables_cell(bpx+180, bpy+20+n*60, 60, 20, m, 'move', state_to_draw, value_read == None)
            self.draw_tables_cell(bpx+240, bpy+20+n*60, 60, 20, c, 'next_state', state_to_draw, value_read == None)
            if 0 in self.machine.states[state_to_draw] :
                r = "0"
                w,m,c = self.machine.states[state_to_draw][0]
            else :
                r,w,m,c = ("","","","")
            self.draw_tables_cell(bpx+60, bpy+20+n*60+20, 60, 20, r, 'read', state_to_draw, value_read == 0)
            self.draw_tables_cell(bpx+120, bpy+20+n*60+20, 60, 20, w, 'write', state_to_draw, value_read == 0)
            self.draw_tables_cell(bpx+180, bpy+20+n*60+20, 60, 20, m, 'move', state_to_draw, value_read == 0)
            self.draw_tables_cell(bpx+240, bpy+20+n*60+20, 60, 20, c, 'next_state', state_to_draw, value_read == 0)
            if 1 in self.machine.states[state_to_draw] :
                r = "1"
                w,m,c = self.machine.states[state_to_draw][1]
            else :
                r,w,m,c = ("","","","")
            self.draw_tables_cell(bpx+60, bpy+20+n*60+40, 60, 20, r, 'read', state_to_draw, value_read == 1)
            self.draw_tables_cell(bpx+120, bpy+20+n*60+40, 60, 20, w, 'write', state_to_draw, value_read == 1)
            self.draw_tables_cell(bpx+180, bpy+20+n*60+40, 60, 20, m, 'move', state_to_draw, value_read == 1)
            self.draw_tables_cell(bpx+240, bpy+20+n*60+40, 60, 20, c, 'next_state', state_to_draw, value_read == 1)

            
    def draw_states_table(self) :
        """ Draw state table as given to the Turing Machine"""
        p5.textSize(10)
        p5.textAlign(p5.CENTER)
        nb_col = len(self.machine.states)//4+1
        for i in range(nb_col) :
            self.draw_states_table_column(i)
            
        
    def draw(self) :
        """P5 draw function"""
        p5.background(TuringGui.colors['GRAY'])
        p5.frameRate(50)
        p5.stroke(TuringGui.colors['BLACK'])
        p5.fill(TuringGui.colors['BLACK'])        
        p5.textSize(15)
        p5.text("TURING MACHINE", 70, self.Y_SHIFT//2)
        next_write, next_move, next_turing_state = self.machine.pre_process()
        if self.machine.current_state == -1 :
            self.status='finished'
        if self.status == 'started' :
            p5.fill(TuringGui.colors[TuringGui.status[TuringGui.steps[self.step]]])
            p5.stroke(TuringGui.colors[TuringGui.status[TuringGui.steps[self.step]]])
            txt = TuringGui.steps[self.step]
        else :
            p5.fill(TuringGui.colors[TuringGui.status[self.status]])
            p5.stroke(TuringGui.colors[TuringGui.status[self.status]])
            txt = self.status
        p5.text(txt, self.SCREEN_WIDTH//2, self.Y_SHIFT//2)
        if self.auto_move :
            auto_move_button_bg_color = 'BLUE'
            auto_move_button_text_color = 'CYAN'
        else :
            auto_move_button_bg_color = 'CYAN'
            auto_move_button_text_color = 'BLUE'
        self.auto_move_button.draw(auto_move_button_bg_color, auto_move_button_text_color)
        if not self.auto_move :
            self.next_step_button.draw('GREEN', 'BLUE')
            
        self.draw_states_table()        
        
        if self.status == 'started' :
            if self.auto_move and (p5.millis()-self.last_click>self.tempo):
                self.last_click = p5.millis()# not a real click, but needed 
                self.step =(self.step + 1)%len(TuringGui.steps)
                if TuringGui.steps[self.step] == 'change' :
                    self.machine.transition()
                    self.tape = deepcopy(self.machine.tape)
            if p5.mouseIsPressed and (p5.millis()-self.last_click)>250:
                self.last_click = p5.millis()
                if not(self.auto_move) and (p5.mouseX, p5.mouseY) in self.next_step_button :               
                    self.step =(self.step + 1)%len(TuringGui.steps)
                    if TuringGui.steps[self.step] == 'change' :
                        self.machine.transition()
                        self.tape = deepcopy(self.machine.tape)
                if (p5.mouseX, p5.mouseY) in self.auto_move_button :
                    self.auto_move = not(self.auto_move)
            if TuringGui.steps[self.step] == 'move' :
                if abs(self.pointer_position-(self.machine.pointer+next_move))> 0.1 :
                    self.pointer_position += next_move*0.1
                else :
                    self.pointer_position =(self.machine.pointer+next_move)
            elif TuringGui.steps[self.step] == 'write'  :
                self.tape[self.pointer_position]  = next_write
            elif TuringGui.steps[self.step] == 'change' :
                self.pointer_position = self.machine.pointer
                    
        self.draw_tape()
        self.draw_pointer()
        if self.status == 'finished' :
            p5.stop()                 
        
                       
            


