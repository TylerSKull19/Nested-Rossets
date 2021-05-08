...
#CSC101 Lab 3
#part 4: Rosettes
#Tyler Smith
#9/10/2020
...

N = int(input("Enter number of sides for polygon: "))
R = int(input("Enter number of repetitions: "))


import turtle

rosette_size = 10
for rosettes in range(5):
  for reps in range(R):
    for sides in range(N):
        turtle.forward(rosette_size)
        turtle.left((360 / N))
    turtle.left(360 / R)
  rosette_size += 20
        
turtle.done
