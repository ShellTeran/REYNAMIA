
import turtle

turtle.speed(10)
turtle.bgcolor("black")
turtle.pensize(3)

# Función para dibujar las curvas del corazón
def func():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)

# Dibujar el corazón
turtle.color("red", "red")
turtle.begin_fill()

turtle.left(140)
turtle.forward(111.65)
func()

turtle.left(120)
func()
turtle.forward(111.65)

turtle.end_fill()

# Escribir las letras dentro del corazón
turtle.penup()
turtle.goto(0, 60)
turtle.color("white")

turtle.write("K y S",
             align="center",
             font=("Arial", 28, "bold"))

# Escribir las letras dentro del corazón
turtle.penup()
turtle.goto(0, -40)
turtle.color("red")

turtle.write("Durame toda la vida",
             align="center",
             font=("Arial", 16, "bold"))
turtle.penup()
turtle.goto(0, -80)
turtle.color("red")

turtle.write("Mi futura esposa <3",
             align="center",
             font=("Arial", 16, "bold"))
turtle.hideturtle()
turtle.done()
