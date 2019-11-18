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