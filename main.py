import time
import random
import colorgram
from turtle import Screen, Turtle
SATRTING_POSITION = [(0,0),(-20,0),(-40,0) ]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.sety(280)
        self.hideturtle()
        self.write("Score= 0",False,"center",("Arial",10,"normal"))

    def Update_score(self, wwynik):
        self.write("Score= "+str(wwynik),False,"center",("Arial",10,"normal"))

    def game_over(self):
        self.write("GAME OVER. YOUR SCORE is " + str(wwynik), False, "center", ("Arial", 10, "normal"))



class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("red")
        self.speed("fastest")
        random_x=random.randint(-250,250)
        random_y = random.randint(-250, 250)
        self.goto(random_x, random_y)

    def refres(self):
        random_x = random.randint(-250, 250)
        random_y = random.randint(-250, 250)
        self.goto(random_x, random_y)



class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]

    def add_segment(self):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()

        newx = self.segments[len(self.segments)-1].xcor()
        newy = self.segments[len(self.segments)-1].ycor()
        new_segment.goto(newx,newy)
        self.segments.append(new_segment)
        #self.segments[len(self.segments)-1].goto(newx, newy)

    def create_snake(self):
        for position in SATRTING_POSITION:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            newx = self.segments[seg_num - 1].xcor()
            newy = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(newx, newy)

        self.head.forward(MOVE_DISTANCE)

    def check_collisions(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            newx = self.segments[seg_num - 1].xcor()
            newy = self.segments[seg_num - 1].ycor()
            if self.segments[seg_num].xcor()==self.head.xcor() and self.segments[seg_num].ycor()==self.head.ycor():
                return False

    def up(self):
        if self.head.heading() !=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() !=UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() !=RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() !=LEFT:
            self.head.setheading(RIGHT)




screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

#starting_positions=[(0,0),(-20,0),(-40,0) ]

#segments=[]
wwynik=0
snake=Snake()
food=Food()
wynik=Score()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.update()

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.check_collisions()==True:
        game_is_on=False

    if snake.head.distance(food) <15:
        food.refres()
        wwynik+=10
        wynik.clear()
        wynik.Update_score(wwynik)
        snake.add_segment()

    if snake.head.xcor()>280 or snake.head.xcor()< -280 or snake.head.ycor()>280 or snake.head.ycor()< - 280:
        game_is_on=False
        wynik.clear()
        wynik.game_over()



screen.exitonclick()