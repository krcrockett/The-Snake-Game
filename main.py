# Simple Snake Game in Python 3 for Beginners
# made by jacob and kylie
# graph snake version 1
from tkinter import *
import turtle
import time
import random
import matplotlib.pyplot as plt
listofpoint=[0]
listoftime=[0]
def true_gameing():
   top.destroy()
   gameing()
def gameing():
   global firstclick
   global start_time
   global score
   global min
   global reall_score
   global listofpoint
   global listoftime
   global reall_score
   delay = 0.1

   # Score
   score = 0
   high_score = 0

   # Set up the screen
   wn = turtle.Screen()
   wn.title("Snake Game by @TokyoEdTech")
   wn.bgcolor("green")
   wn.setup(width=600, height=600)
   wn.tracer(0)  # Turns off the screen updates

   # Snake head
   head = turtle.Turtle()
   head.speed(0)
   head.shape("square")
   head.color("black")
   head.penup()
   head.goto(0, 0)
   head.direction = "stop"

   # Snake food
   food = turtle.Turtle()
   food.speed(0)
   food.shape("circle")
   food.color("red")
   food.penup()
   food.goto(0, 100)

   segments = []

   # Pen
   pen = turtle.Turtle()
   pen.speed(0)
   pen.shape("square")
   pen.color("white")
   pen.penup()
   pen.hideturtle()
   pen.goto(0, 260)
   pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))
   firstclick = True

   # Functions
   def graph():
       plt.plot(listoftime,listofpoint)
       plt.show()
   def go_stop():
       head.direction = "stop"

   # converts sec to mins
   def time_convert(sec):
       global min
       min = sec / 60
       return min

   # chechs if the first move to start timer
   def true_start():
       global firstclick
       global start_time
       if firstclick == True:
           firstclick = False
           start_time = time.time()

   def go_up():
       global firstclick
       if head.direction != "down":
           head.direction = "up"
           true_start()

   def go_down():
       if head.direction != "up":
           head.direction = "down"
           true_start()

   def go_left():
       if head.direction != "right":
           head.direction = "left"
           true_start()

   def go_right():
       if head.direction != "left":
           head.direction = "right"
           true_start()

   def move():
       if head.direction == "up":
           y = head.ycor()
           head.sety(y + 20)

       if head.direction == "down":
           y = head.ycor()
           head.sety(y - 20)

       if head.direction == "left":
           x = head.xcor()
           head.setx(x - 20)

       if head.direction == "right":
           x = head.xcor()
           head.setx(x + 20)

   # Keyboard bindings
   wn.listen()
   wn.onkeypress(go_up, "w")
   wn.onkeypress(go_down, "s")
   wn.onkeypress(go_left, "a")
   wn.onkeypress(go_right, "d")
   wn.onkeypress(go_up, "W")
   wn.onkeypress(go_down, "S")
   wn.onkeypress(go_left, "A")
   wn.onkeypress(go_right, "D")
   wn.onkeypress(go_stop, "space")
   wn.onkeypress(graph, "F")
   wn.onkeypress(graph, "f")

   # Main game loop
   while True:
       wn.update()
       # Check for a collision with the border
       if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
           time.sleep(1)
           head.goto(0, 0)
           head.direction = "stop"
           x = random.randint(-290, 290)
           y = random.randint(-290, 290)
           food.goto(x, y)
           firstclick = True
           end_time = time.time()
           time_lapsed = end_time - start_time
           min=time_convert(time_lapsed)


           # Hide the segments
           for segment in segments:
               segment.goto(1000, 1000)

           # Clear the segments list
           segments.clear()

           # Reset the score
           reall_score=score
           score=0
           listoftime.append(min)
           listofpoint.append(reall_score)

           # Reset the delay
           delay = 0.1

           pen.clear()
           pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                     font=("Courier", 24, "normal"))

           # Check for a collision with the food
       if head.distance(food) < 20:
           # Move the food to a random spot
           x = random.randint(-290, 290)
           y = random.randint(-290, 290)
           food.goto(x, y)

           # Add a segment
           new_segment = turtle.Turtle()
           new_segment.speed(0)
           new_segment.shape("square")
           new_segment.color("grey")
           new_segment.penup()
           segments.append(new_segment)

           # Shorten the delay
           delay -= 0.001

           # Increase the score
           score += 10

           if score > high_score:
               high_score = score

           pen.clear()
           pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                     font=("Courier", 24, "normal"))

           # Move the end segments first in reverse order
       if head.direction != "stop":
           for index in range(len(segments) - 1, 0, -1):
               x = segments[index - 1].xcor()
               y = segments[index - 1].ycor()
               segments[index].goto(x, y)
           # else:
           #     segments[index].goto(segments[index].xcor(), segments[index].ycor())

       # Move segment 0 to where the head is

       if len(segments) > 0 and head.direction != "stop":
           x = head.xcor()
           y = head.ycor()
           segments[0].goto(x, y)

       move()

       # Check for head collision with the body segments
       for segment in segments:
           if segment.distance(head) < 20 and head.direction != "stop":
               time.sleep(1)
               head.goto(0, 0)
               head.direction = "stop"
               x = random.randint(-290, 290)
               y = random.randint(-290, 290)
               food.goto(x, y)
               firstclick = True
               end_time = time.time()
               time_lapsed = end_time - start_time
               # Hide the segments
               for segment in segments:
                   segment.goto(1000, 1000)

               # Clear the segments list
               segments.clear()

               # Reset the score
               reall_score=score
               score = 0
               min = time_convert(time_lapsed)
               listoftime.append(min)
               listofpoint.append(reall_score)

               # Reset the delay
               delay = 0.1

               # Update the score display
               pen.clear()
               pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                         font=("Courier", 24, "normal"))

       time.sleep(delay)
   wn.mainloop()



top = Tk()
top.title("Snake Game")
title = Label(top, text="Snake Game \n Click to begin!", font=("Comic Sans MS", 20, "bold"))       #title
title.pack()


b1 = Button(top, text="Click me", command=true_gameing,height=3,width=7)      #button
b1.pack()
top.geometry("300x300")      #window



top.config(bg="green")
top.mainloop()


