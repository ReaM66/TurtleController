import sys
import turtle_controller

if __name__ == '__main__':
    try:
        filename = sys.argv[1]
    except:
        print(f"{filename} can't be found. You get shaft instead.")
        filename = "turtle_files\\shaft.txt"
    turtle = turtle_controller.Turtle(filename)
    turtle.Run()
    turtle.done()
