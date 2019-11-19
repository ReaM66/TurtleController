import turtle
import random

class Turtle(object):
    def __init__(self, command_filename="", turtle_name="Terry", speed=6):
        """Initialise turtle with filename, name and a speed."""
        self.mrTurtle = turtle.Turtle()
        turtle.colormode(255)
        self.set_name(turtle_name)
        self.set_speed(speed)
        if command_filename:
            self.load_commands(command_filename)
        self.pc = 0
        self.loop_counters = {}

    def load_commands(self, filename):
        """Load the command file and set self.commands"""
        lines_out = []
        try:
            with open(filename, "r") as inFile:
                for line in inFile.readlines():
                    comment = line.find(';')  # Don't read comments after ';'
                    if comment != -1:
                        line = line[:comment]
                    line = line.strip()
                    if len(line) > 0:  # Don't read lines of length 0.
                        lines_out.append(line)
        except FileNotFoundError:
            print(f"File {filename} not found.")
        self.commands = lines_out

    def Run(self):
        """Run all commands in buffer"""
        print(f"{self.name} is ready to go!")
        self.pc = 0
        while self.pc < len(self.commands):
            self.run_command(self.commands[self.pc])
            self.pc += 1
        print(f"{self.name} is finished!")

    def Step(self, steps=1):
        """Step through specified number of commands. 1 if no number specified."""
        for i in range(steps):
            try:
                self.run_command(self.commands[self.pc])
                self.pc += 1
            except IndexError:
                self.pc = 0
                self.run_command(self.commands[self.pc])
                self.pc += 1

    def StepThrough(self):
        """Run all commands, but wait for input between each command."""
        self.pc = 0
        while self.pc < len(self.commands):
            input("Press Enter.")
            self.run_command(self.commands[self.pc])
            self.pc += 1

    def queue_command(self, command):
        """Add a command to the buffer"""
        self.commands.append(command)

    def run_command(self, command):
        """Send 1 command to turtle. Big switch case handles command."""
        print(f"{self.name} is trying {command}")
        command = command.lower()
        try:
            command = command.split(" ")
            if len(command) > 1:
                data = [convert(item) for item in command[1:]]
            else:
                data = None
            command = command[0]
        except:
            print(f"Error: {self.name} could not perform command {command}")
            return None

        if command in ["forward", "forwards", "f", "fwd"]:
            self.forward(data[0])
        elif command in ["backward", "backwards", "back", "b", "bck"]:
            self.backward(data[0])
        elif command in ["left", "l", "lft"]:
            self.turn(-data[0])
        elif command in ["right", "r", "turn", "rgt", "trn"]:
            self.turn(data[0])
        elif command in ["move", "goto", "mv", "mov"]:
            self.set_position(data)
        elif command in ["reset", "origin", "centre", "cnt"]:
            self.set_position([0, 0])
        elif command in ["circle", "crc"]:
            self.circle(data)
        elif command in ["stamp", "print", "prt", "smp"]:
            self.stamp()
        elif command in ["undo", "und"]:
            if data is None:
                self.undo(1)
            else:
                self.undo(data[0])
        elif command in ["face", "setheading", "fac"]:
            self.face(data[0])
        elif command in ["loop", "startloop", "lop"]:
            if data[1] in self.loop_counters:
                pass
            else:
                self.loop_counters[data[1]] = [data[0], self.pc]
        elif command in ["endloop", "end"]:
            loop_name = data[0]
            loop_data = self.loop_counters[loop_name]
            if loop_data[0] > 1:
                self.pc = loop_data[1]
                self.loop_counters[loop_name][0] -= 1
            else:
                del self.loop_counters[loop_name]
        elif command in ["colour", "color", "setcolour", "clr"]:
            self.colour(data)
        elif command in ["penup", "up"]:
            self.penup()
        elif command in ["pendown"]:
            self.pendown()
        elif command in ["pen"]:
            self.switchpen()
        elif command in ["name", "setname"]:
            self.set_name(data[0])
        elif command in ["speed", "setspeed"]:
            self.set_speed(data[0])
        elif command == "run":
            self.Run()
        elif command == "randcolour":
            self.randomcolour()
        else:
            print(f"{self.name} doesn't know how to do {command}")

    def forward(self, data):
        """Go forwards a certain amount."""
        self.mrTurtle.forward(data)

    def backward(self, data):
        """Go backwards"""
        self.mrTurtle.backward(data)

    def turn(self, data):
        """Turn clockwise specified amount in degrees. Commands 'left' and 'right' both
        map to this function. Commands for 'left' are made negative."""
        self.mrTurtle.right(data)

    def face(self, data):
        """Face a certain heading."""
        self.mrTurtle.setheading(data)

    def set_position(self, data):
        """Move turtle to coordinates"""
        x = data[0]
        y = data[1]
        self.mrTurtle.setposition(x, y)

    def circle(self, data):
        """Draw a circle with the built in turtle circle function."""
        radius = data[0]
        extent = None
        steps = None
        if len(data) == 2:
            extent = data[1]
        if len(data) == 3:
            extent = data[1]
            steps = data[2]
        self.mrTurtle.circle(radius, extent, steps)

    def randomcolour(self):
        """Chooses random rgb values and assigns to colour."""
        r = random.randrange(1, 255)
        g = random.randrange(1, 255)
        b = random.randrange(1, 255)
        self.colour((r,g,b))


    def colour(self, data):
        """Modify turtle colour."""
        if len(data) == 1:
            data = data[0]
        elif len(data) == 3:
            data = (data[0], data[1], data[2])
        else:
            return None
        print("Colour set to {}".format(data))
        self.mrTurtle.color(data)

    def penup(self):
        """Pen up."""
        self.mrTurtle.penup()

    def pendown(self):
        """Pen down."""
        self.mrTurtle.pendown()

    def switchpen(self):
        """Flip pen state."""
        if self.mrTurtle.isdown():
            self.mrTurtle.penup()
        else:
            self.mrTurtle.pendown()

    def stamp(self):
        """Stamp a copy of turtle."""
        self.mrTurtle.stamp()

    def undo(self, num):
        """Undo specified number of commands"""
        for i in range(num):
            self.mrTurtle.undo()

    def set_speed(self, speed):
        """Set the movement speed of turtle."""
        self.mrTurtle.speed(speed)

    def set_name(self, name):
        """Set the turtle name"""
        self.name = name

    def done(self):
        """Forces window to stay open after completion. Function for runturtle.py. No
        more commands can be executed after this one."""
        turtle.done()


def convert(input):
    """
    Converts a string to an int or float.
    Converts a list of strings into a list of strings, ints or floats.
    Args:
        input (str, list[str]): string or list of strings to attempt to convert.
    Returns:
        (str, int, float, list[...]): Depending on data contained in input.
    """
    if isinstance(input, str):
        input = [input]
    converted = []
    for item in input:
        try:
            if "." in item:
                converted.append(float(item))
            else:
                converted.append(int(item))
        except ValueError:
            converted.append(item)
    if len(converted) == 1:
        converted = converted[0]
    return converted
