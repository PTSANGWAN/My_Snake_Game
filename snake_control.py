from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score
snake=Snake()
food=Food()
score=Score()
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()
screen.onkey(snake.snakeup,"Up")
screen.onkey(snake.snakedown,"Down")
screen.onkey(snake.snakeleft,"Left")
screen.onkey(snake.snakeright,"Right")
game_is_on=True
p=0
while game_is_on:    
    time.sleep(0.1)
    screen.update()
    snake.move()
    if snake.body[0].distance(food)<15:
        food.refresh()
        snake.extend()
        p=p+1
        score.write_score(p)
    
    if snake.body[0].xcor()>295 or snake.body[0].xcor()<-295 or snake.body[0].ycor()>295 or snake.body[0].ycor()<-295:
        game_is_on=False
        score.game_over()
    for segment in snake.body[1:]:
        if snake.body[0].distance(food)<15:
            game_is_on=False
            score.game_over()

       
screen.exitonclick()