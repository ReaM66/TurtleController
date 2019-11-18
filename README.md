# TurtleController
Simple controller for Python Turtle that can load commands from text files.

USAGE:
At command line:
> python runturtle.py "turtle_files\\square.txt"

In python interactive shell:
> import turtle_controller

> turt = turtle_controller.TurtleController()

> turt.load_commands("turtle_files\\square.txt")

> turt.Run()

> turt.run_command("forward 20")


Instructions:
forward, forwards, f, fwd [distance]
  Move turtle forwards [distance] amount.

backward, backwards, b, bck, back [distance]
  Move turtle backwards [distance] amount.

left, l, lft [amount]
  Rotate turtle counter clockwise [amount] degrees

right, r, rgt, turn [amount]
  Rotate turtle clockwise [amount] degrees

move, goto, mv, mov [x] [y]
  Set turtle position to [[x], [y]]

reset, origin, centre, cnt
  return turtle to [0, 0]

circle, crc [radius] [extent] [steps]
  Draw a circle starting at a point on its edge.
  Extent is in degrees and dictates how much of the circle to move around.

stamp, print, prt, smp  
  Stamp an image of the turtle onto the page.

undo, und [number]
  Undo [number] of previous moves. If no number is specified then 1 move is undone.

face, setheading, fac [bearing]
  Set turtle to face [bearing]. 0 is East/Right. 90 is North/Up

loop, startloop, lop [num_iterations] [name]
  Start a loop with number of iterations specified and [name]

endloop, end [name]
  End loop with [name]. This is required.

penup, pendown, pen
  Sets pen up, down or flips pen state

colour, color, setcolour, col [colour]
  Sets pen colour. [colour] is either a string from preset list or a hex value.
  Can also be 3 values
