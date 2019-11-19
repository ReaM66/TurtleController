import sys
import turtle_controller_two

def load_commands(filename):
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
    return lines_out

if __name__ == '__main__':
    running = False
    try:
        filename = sys.argv[1]
    except:
        print(f"{filename} can't be found. You get shaft instead.")
        filename = "turtle_files\\shaft.txt"
    commands = load_commands(filename)
    turtle = turtle_controller_two.Turtle(commands)
    for res in turtle.run():
        pass

    while True:
        command = input(": ")
        if command == "quit":
            print("Quitting...")
            break
        else:
            turtle.run_command(command)
