import turtle
from time import sleep
import random


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
            t.fillcolor(random.choice(['red', 'green', 'blue', 'black', 'white', 'yellow']))
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
    
def longueurR(t, d : int, n : int) :
    if n == 0 :
        t.forward(d)
    else :
        longueurR(t, d//3, n-1)
        t.left(60)
        longueurR(t, d//3, n-1)
        t.right(120)
        longueurR(t, d//3, n-1)
        t.left(60)
        longueurR(t, d//3, n-1)
        
def vonKoch(d, n) :
    
    screen = turtle.Screen()
    screen.bgcolor('lightgray')
    t = turtle.Turtle()
    t.penup()
    t.goto(-d//2, -d//2)
    t.pendown()
    t.speed(0)
    for _ in range(3) :
        longueurR(t, d,n)
        t.left(120)
    screen.exitonclick()
    
    

vonKoch(300,3)
# if __name__ == "__main__" :
#     while True :
        
#         traceSierpinski(200,0,speed = 0)
#         traceSierpinski(200,1, speed= 0)
#         traceSierpinski(200,2, speed = 0)
#         traceSierpinski(200,3, speed = 0)
#         traceSierpinski(200,4, speed = 0)
#         traceSierpinski(200,7, speed = 0)
