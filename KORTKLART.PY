import turtle
import random
turtle.speed(0)
turtle.penup()
turtle.setposition(0, 0)
turtle.bgcolor("black")
värden = ["2","3","4","5","6","7","8","9","10","K","Q","J","A"]
suits = ["♣","♠","♦","♥"]
deck = []
valda = []
for i in suits:
    for v in värden:
        deck.append(i+v)                     #kombinera listorna, skapade alla kort
 
 
class card():
    def __init__(self):
        pass
 
class heart(card):
    def __init__(self, color):
        self.color = color

class spade(card):                  #Skapar klasser och subklass
    def __init__(self, color):
        self.color = color
       
class diamond(card):
    def __init__(self, color):
        self.color = color
class clover(card):
    def __init__(self, color):
        self.color = color
     
 
for i in deck:
    if "♣" in i:
        i = clover("black")
        print(i)  
    elif "♠" in i:
        i = spade("black")      
        print(i)                              #Lägger in korten i klasserna
    elif "♦" in i:
        i = diamond("red")
        print(i)  
    elif "♥" in i:
        i = heart("red")
        print(i)  
 
for i in range(4):
    valda.append(random.choice(deck))             #Väljer 4 kort
print(valda)
 
turtle.setposition(-600,0)
def draw(self):
    turtle.pendown()
    turtle.fillcolor("white")
    turtle.penup()
    turtle.pendown()
    turtle.begin_fill()
    for i in range(2):
 
 
        turtle.forward(150)
        turtle.right(90)                #ritar kvadraterna/outlines på korten
        turtle.forward(225)
        turtle.right(90)
       
    turtle.end_fill()
    turtle.penup()
    turtle.forward(40)
    turtle.right(90)                          #ritar ut name och suit
    turtle.forward(122)
    turtle.pendown()
    
    if "♣" in self:
        turtle.pencolor("black")
     
    elif "♠" in self:
        turtle.pencolor("black")                  #Väljer vilka kort som ska ha vilken färg
                                         
    elif "♦" in self:
        turtle.pencolor("red")
     
    elif "♥" in self:
        turtle.pencolor("red")
    turtle.write(self, font=('Impact', 45))
    turtle.pencolor("black")
    turtle.penup()
    turtle.right(180)
    turtle.forward(122)              
    turtle.right(90)                                    
    turtle.forward(300)
 
for i in valda:
    draw(i)           #loopar draw funktionen beroende på antal i "valda", vilket är 4 då det är 4 kort
turtle.done()
 

