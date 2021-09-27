import turtle
from time import sleep


def testTurtle() :
    screen = turtle.Screen()
    screen.bgcolor('lightgray')
    donatello = turtle.Turtle()
    donatello.forward(100)
    donatello.left(90)
    donatello.forward(50)
    donatello.right(45)
    donatello.backward(80)
    donatello.setx(-300)
    

def traceSierpinski(long,n, speed=5) :
    
    def sier(t,long, n)  :
        if n==0 :
            t.left(60)
            t.begin_fill()
            for _ in range(3) :
                t.forward(long)
                t.right(120)
            t.end_fill()
            t.right(60)
        else :
            sier(t, long//2, n-1)
            t.forward(long//2)
            sier(t, long//2, n-1)
            t.penup()
            t.left(120)
            t.forward(long//2)
            t.right(120)
            t.pendown()
            sier(t, long//2, n-1)
            t.left(60)
            
            t.backward(long//2)
            t.right(60)
            
    screen = turtle.Screen()
    screen.bgcolor('lightgray')
    rafaello = turtle.Turtle()
    rafaello.speed(speed)
    sier(rafaello, long, n)
    sleep(2)
    screen.reset()
    rafaello.hideturtle()
    


if __name__ == "__main__" :
    while True :
        
        traceSierpinski(200,0,speed = 0)
        traceSierpinski(200,1, speed= 0)
        traceSierpinski(200,2, speed = 0)
        traceSierpinski(200,3, speed = 0)
        traceSierpinski(200,4, speed = 0)
        traceSierpinski(200,7, speed = 0)
