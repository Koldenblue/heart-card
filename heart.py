import turtle, random

wn = turtle.Screen()
wn.bgcolor('light pink')
wn.title('Hello, Sarah!')

colorChoices = ['red', 'orange', 'orchid', 'green', 'blue', 'violet', 'salmon']
for darkColor in range(len(colorChoices)):
    darkColor = 'dark ' + colorChoices[darkColor]
    colorChoices.append(darkColor)
print(colorChoices)

# This code will draw nested rectangles
# alex = turtle.Turtle()
# alex.penup()
# alex.setx(-400)
# alex.sety(200)
# alex.pendown()
# lengthMovement = 100
# widthMovement = 25
# for i in range(20):
#     alex.color(random.choice(colorChoices))
#     alex.forward(widthMovement)
#     alex.left(90)
#     alex.forward(lengthMovement)
#     alex.left(90)
#     alex.forward(widthMovement)
#     alex.left(90)
#     alex.forward(lengthMovement)
#     alex.left(90)
#     lengthMovement -= 5
#     widthMovement -= 1.25

heart = turtle.Turtle()
heart.speed(10)
heart.penup()
#heart.setx(-350)
heart.sety(-300)
heart.pendown()
heart.pensize(9)
heartMovement = 400
numHearts = 20   
heart.left(45)
x = 0
for j in range(numHearts):
    heart.color(colorChoices[x])
    x = x + 1
    if x > len(colorChoices) - 1:
        x = 0
    heart.forward(heartMovement)
    heart.circle(heartMovement / 2, extent=180)
    heart.right(90)
    heart.circle(heartMovement / 2, extent=180)
    heart.forward(heartMovement)
    heart.penup()
    heart.left(135)
    heart.forward(10)
    heart.right(45)
    heart.pendown()
    heartMovement = heartMovement - (numHearts)
    


wn.mainloop()
