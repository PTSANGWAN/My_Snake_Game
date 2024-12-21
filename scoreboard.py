from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        # self.write("Score:", True, "center", ("Arial",8,"normal"))
        # self.color("white")
        # self.write((0,0), True)
        
        self.write_score(p=0)
        
        
    def write_score(self,p):
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.clear()
        self.write(f"Score: {p} ", True, "center",("Arial",18,"normal"))
    
    def game_over(self):
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.hideturtle()
        
        self.write(" GAME OVER ", True, "center",("Arial",18,"normal"))

        

