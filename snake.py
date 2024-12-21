from turtle import Turtle, Screen

class Snake:
    def __init__(self):
        self.body=[]
        self.create_body()


    def create_body(self):
        for i in range(3):
            tim=Turtle("square")
            tim.color("white")
            tim.penup()
            p=-(20*i)
            tim.setpos(p,0)
            self.body.append(tim)

    def add_segment(self,pos):
        tim=Turtle("square")
        tim.color("white")
        tim.penup()
        tim.setpos(pos)
        self.body.append(tim)

    def extend(self):
        self.add_segment(self.body[-1].position())
    def move(self):
        for i in range(len(self.body)-1,0,-1):
            new_x=self.body[i-1].xcor()
            new_y=self.body[i-1].ycor()
            self.body[i].goto(new_x,new_y)
        self.body[0].forward(20)
        
    def snakeup(self):
        if self.body[0].heading() != 270:
            self.body[0].setheading(90)
    
    def snakedown(self):
        if self.body[0].heading() != 90:
            self.body[0].setheading(270)

    def snakeleft(self):
        if self.body[0].heading() !=0 :
            self.body[0].setheading(180)
    
    def snakeright(self):
        if self.body[0].heading() != 180:
            self.body[0].setheading(0)


    


