# Author:Zuriahn Yun
# Date:2/28/2023
# Description:Plot Earthquakes

import turtle

# copied from my lab 5 solution:
def teleport(t, x, y):
    """ Move the turtle to (x, y), ensuring that nothing is drawn along the
        way. Postcondition: the turtle's orientation and up/down state is the
        same as before.
    """
    # save the current pen state
    pen_was_down = t.isdown()
    
    # pick up pen, move to coordinates
    t.up()
    t.goto(x, y)
    
    # restore pen state
    if pen_was_down:
        t.down()

# copied from A4, with a couple slight modifications:
def turtle_setup(canv_width, canv_height):
    """ Set up the canvas and a turtle; return a turtle object in hidden
        state. The canvas has size canv_width by canv_height, with a
        coordinate system where (0,0) is in the center, and automatic
        re-drawing of the canvas is disabled. Set the background image to
        earth.png.
    """
    # create a turtle to color pixels with
    t = turtle.Turtle()
   
    # set the screen size, coordinate system, and color mode:
    screen = t.getscreen()
    screen.setup(canv_width, canv_height)
    turtle.colormode(255) # specify how colors are set: we'll use 0-255
    
    t.hideturtle() # hide the turtle triangle
    screen.tracer(0, 0) # turn off redrawing after each movement
    
    turtle.bgpic('earth.png') # set the background image
    turtle.update()
    return t

def parse_row(line):
    """ Parse a line of the csv file, returning a dict with keys
    for latitude, longitude, timestamp, and magnitude.
    Pre: line is an unprocessed string representing a line of the file.
    Post: the returned dict has the following keys with values according
          to the data in the given line of the file:
            "latitude" -> (float)
            "longitude" -> (float)
            "timestamp" -> (str)
            "magnitude" -> (float)
    """
    
    # split the line into its constituent numbers
    #Splitting the line
    line =line.split(',')
    #Dividing each split into its data
    latitude = float(line[0])
    longitude = float(line[1])
    timestamp = str(line[2])
    magnitude = float(line[3])
    # create a dictionary and populate it with the given keys
    #Adding the data into a dictionary 
    dictionary = {"lat":latitude,"long":longitude,"time":timestamp,"magnitude":magnitude}
    
    # return the resulting dictionary
    return dictionary
def main():
    """ Main function: plot a circle on a map for each earthquake """
    # we'll scale coordinates and canvas to be 720x360, double
    # the size of the range of lat/lon coordinates
    scale = 2.0
    
    # call turtle_setup to set up the canvas and get a turtle
    t = turtle_setup(scale * 360, scale * 180)
    t = turtle.Turtle()
    # open earthquakes.csv for reading
    #Opening the csv file
    earth = open('earthquakes.csv', 'r')
    #Reading the csv file
    lines = earth.readlines()
    #Hiding turtle
    turtle.hideturtle()
    #Setting pensize and color
    turtle.pensize(1)
    turtle.pencolor('red')
   
    # parse each line of the file using parse_row and add each returned
    #quakes is an empty list
    quakes =[]
    #Reading all lines except the first one 
    for i in lines[1:]:
        dictionary = parse_row(i)   
    # dictionary into a list (skip the headers on the first line!)
        quakes.append(dictionary)
    #Rows start at 0 because the first line was not read
    row = 0
    
    #For loop to check every line
    for i in quakes:
        #When magnitutde is higher than 1.0 make a circle 
        quakes[row]["magnitude"] > 1.0
        t.hideturtle()
        #Circle location and radius
        x = (quakes[row]["long"])*2
        y = (quakes[row]["lat"])*2
        teleport(turtle,x,y)
        turtle.circle(quakes[row]["magnitude"])
        row+=1
    #Updating so that it shows up immediately 
    turtle.update()
if __name__ == "__main__":
    main()
