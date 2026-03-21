'''2. The "Coordinate Lock" (Tuples)
Goal: Practice immutability and unpacking.

The Data: start_point = (10, 20)

The Task: 
1.  Try to change the first number of the tuple to 50. (Note what happens when you run it!).
2.  Unpack the start_point into two variables: x and y.
3.  Print: "The robot is at X: [x] and Y: [y]".'''


start_point = (10, 20)

first, second = start_point
first = 50
start_point =(first,second)

x, y = start_point
print(f"The robot is at X: {x} and Y: {y}")