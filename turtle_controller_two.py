import turtle
import random

class Turtle(turtle.Turtle):
    keywords = {"forward", "backward", "left", "right", "circle", "square", "loop",
                "endloop", "setposition", "goto", "setx", "sety", "reset", "setheading",
                "undo", "penup", "pendown", "switchpen", "shape", "stamp", "dot",
                "colour", "randomcolour", "name", "speed", "var", "del", "add", "sub",
                "neg", "mult", "div", "done"}
    def __init__(self, commands=[], turtle_name="Terry", speed=6, shape="classic"):
        """Initialise turtle with filename, name and a speed."""
        super().__init__()
        turtle.colormode(255)
        self._name = turtle_name
        super().speed(speed)
        super().shape(shape)
        self.commands = commands
        self._pc = 0
        self._loop_stack = []
        self._variables = {'x':0, 'y':0}

    def set_commands(self, commands, append=False):
        """Sets commands. Will either add them to commands or overwrite."""
        if append:
            self.commands.extend(commands)
        else:
            self.commands = commands

    def run(self):
        """Run all commands in buffer"""
        print(f"{self._name} is ready to go!")
        self._pc = 0
        while self._pc < len(self.commands):
            self.run_command(self.commands[self._pc])
            self._pc += 1
            yield (self._pc < len(self.commands))
        print(f"{self._name} is finished!")

    def run_command(self, command):
        """Send 1 command to turtle. If command is the name of a function it is executed."""
        print(f"{self._name} is trying {command}")
        location = self.position()
        self._variables['x'] = location[0]
        self._variables['y'] = location[1]
        print(f"Variables: {self._variables}")

        try:
            command, *data = command.split(" ")
            if command in ['var', 'add', 'sub', 'mult', 'div', 'neg']:
                data = list(map(self.convert, data))
            else:
                data = list(map(self.convert_vars, data))
        except:
            print(f"Error: {self._name} could not perform command {command}")
            return None
        if command in self.keywords:
            getattr(self, command)(*data)
        else:
            print(f"{self._name} doesn't know how to do {command}.")

    def var(self, name, data=0):
        """Assigns a variable."""
        if isinstance(data, str):
            data = self._variables[data]
        self._variables[name] = data

    def add(self, first, second):
        """Adds data in second to first. First must be a variable."""
        try:
            if isinstance(second, str):
                second = self._variables[second]
            self._variables[first] += second
        except:
            print(f"Could not add together {first} + {second}")

    def sub(self, first, second):
        try:
            if isinstance(second, str):
                second = self._variables[second]
            self._variables[first] -= second
        except:
            print(f"Could not subtract {first} - {second}")

    def mult(self, first, second):
        try:
            if isinstance(second, str):
                second = self._variables[second]
            first_num = self._variables[first]
            self._variables[first] = int(first_num * second)
        except:
            print(f"Could not multiply {first} * {second}")

    def div(self, first, second):
        try:
            if isinstance(second, str):
                second = self._variables[second]
            first_num = self._variables[first]
            self._variables[first] = int(first_num / second)
        except:
            print(f"Could not divide {first} / {second}")


    def neg(self, variable):
        try:
            val = self._variables[variable]
            self._variables[variable] = -1*val
        except:
            print(f"Could not negate {variable}")

    def loop(self, iterations):
        """Initialise loop"""
        self._loop_stack.append([iterations, self._pc])

    def endloop(self):
        try:
            n, start = self._loop_stack[-1]
        except IndexError:
            print("No loops remaining.")
            return
        if n == 1:
            self._loop_stack.pop()
        else:
            self._loop_stack[-1][0] -= 1
            self._pc = start

    def circle(self, radius, extent=None, steps=None):
        """Draw a circle with the built in turtle circle function."""
        super().circle(radius, extent, steps)

    def square(self, length):
        """Draw a square with given side length."""
        for i in range(4):
            self.forward(length)
            self.left(90)

    def reset(self):
        """Reset turtle to origin."""
        self.home()

    def colour(self, args):
        """Sets colour"""
        print(f"Colour set to {args}")
        super().color(args)

    def randomcolour(self):
        """Chooses random rgb values and assigns to colour."""
        r = random.randrange(1, 255)
        g = random.randrange(1, 255)
        b = random.randrange(1, 255)
        self.colour((r,g,b))

    def switchpen(self):
        """Flip pen state."""
        if self.isdown():
            self.penup()
        else:
            self.pendown()

    def name(self, new_name):
        """Set turtle name."""
        self._name = new_name

    def undo(self, num=1):
        """Undo specified number of commands"""
        for i in range(num):
            super().undo()

    def done(self):
        """Forces window to stay open after completion. Function for runturtle.py. No
        more commands can be executed after this one."""
        turtle.done()

    def convert_vars(self, input):
        """Calls convert, but resolves string variables too."""
        input = self.convert(input)
        if not isinstance(input, list):
            input = [input]
        converted = []
        for item in input:
            if item in self._variables:
                converted.append(self._variables[item])
            else:
                converted.append(item)
        if len(converted) == 1:
            converted = converted[0]
        return converted

    def convert(self, input):
        """
        Converts a string to an int or float.
        Converts a list of strings into a list of strings, ints or floats.
        Args:
            input (str, list[str]): string or list of strings to attempt to convert.
        Returns:
            (str, int, float, list[...]): Depending on data contained in input.
        """
        if not isinstance(input, list):
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
