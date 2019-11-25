# TurtleController
Simple controller for Python Turtle that can load commands from text files.

USAGE:

At command line:
```
> python runturtle.py "turtle_files\\square.txt"
```

In python interactive shell:
```
> import turtle_controller
> turt = turtle_controller.Turtle()
> turt.load_commands("turtle_files\\square.txt")
> turt.Run()
> turt.run_command("forward 20")
```
NOTE: These instructions and labels are not case-sensitive.

The example text files provided do not all work properly. Some of them are for the old version of the program. .txt and .turt files are equivalent.


Movement Instructions:
- forward [distance]
  - Move turtle forwards [distance] amount.

- backward [distance]
  - Move turtle backwards [distance] amount.

- left [amount]
  - Rotate turtle counter clockwise [amount] degrees

- right [amount]
  - Rotate turtle clockwise [amount] degrees

- circle [radius] [extent] [steps]
  - Draw a circle starting at a point on its edge.
  - Extent is in degrees and dictates how much of the circle to move around.

- square [side_length] [extent]
  - Draw a square counter-clockwise with side_length
  - Extent is the number of sides to draw.

- goto, setposition [x] [y]
  - Set turtle position to [[x], [y]]

- setx [x]
  - set x coordinate to [x]

- sety [y]
  - set y coordinate to [y]

- setheading [bearing]
  - Set turtle to face [bearing]. 0 is East/Right. 90 is North/Up

- reset
  - return turtle to [0, 0]

Control Instructions:
- loop [num_iterations]
  - Start a loop with number of iterations specified

- endloop
  - Decrement or end current loop on stack. This is required.

- var [variable_name] [value]
  - Creates a variable with [variable_name] and [value]

- input [variable_name] [default_value]
  - Take input for a variable from the command line
  - default_value is optional and a null input will send this.

- add [varaible_name] [addition]
  - Adds together the value of [variable_name] and [addition]
  - Result is stored in [variable_name]

- sub [varaible_name] [subtraction]
  - Subtracts [subtraction] from the value of [variable_name]
  - Result is stored in [variable_name]

- mult [varaible_name] [multiplication]
  - Multiplies the value of [variable_name] by [multiplication]
  - Result is stored in [variable_name]

- div [varaible_name] [division]
  - Divides the variable in [variable_name] by [division]
  - Result is stored in [variable_name]

- neg [variable_name]
  - Multiplies [variable_name] by -1

- undo [number]
  - Undo [number] of previous moves. If no number is specified then 1 move is undone

- done
  - Stops turtle from taking any more input but holds the window open.


Aesthetic Instructions:
- colour [colour]
  - Sets pen colour. [colour] is either a string from preset list or a hex value.
  - Can also be 3 values

- randomcolour
  - Sets pen colour to random RGB value.

- penup, pendown, switchpen
  - Sets pen up, down or flips pen state

- stamp
  - Stamp an image of the turtle onto the page.

- dot
  - Places a dot on the canvas

- name [name]
  - Sets the name of the turtle.

- speed [speed]
  - Sets the movement speed of the Turtle, between 1 and 9.

- shape [shape]
  - Sets the turtle shape to the shape specified. These are builtin from turtle.
