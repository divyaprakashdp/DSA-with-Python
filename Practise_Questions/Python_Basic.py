import datetime
import math

import sys


class Questions:
    """
    1. Write a Python program to print the following string in a specific format (see the output).
    Sample String :
        "Twinkle, twinkle, little star, How I wonder what you are! Up above the world
        so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
    Output :

    Twinkle, twinkle, little star,
        How I wonder what you are!
            Up above the world so high,
            Like a diamond in the sky.
    Twinkle, twinkle, little star,
        How I wonder what you are
    """

    print("Sol 1:",
          "\nTwinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a "
          "diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are")

    """
    2. Write a Python program to get the Python version you are using.
    """
    print("Sol 2:", sys.version)

    """
    3. Write a Python program to display the current date and time.
    """
    print("Sol 3:", datetime.datetime.now())

    """
    4. Write a Python program which accepts the radius of a circle from the user and compute the area
    """

    def areaOfCircle(self, radius):
        print(f"Area of circle with radius {radius} is: ", math.pi * radius * radius)

    """
    5. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
    """

    def reverseNames(self, firstname, lastname):
        print(lastname, firstname)
        # print(name[::-1])

    """
    6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
    """

    def convertToTuple(self):
        values = input("Input some comma seprated numbers : ")
        list = values.split(',')
        tupleResult = tuple(list)
        print(tupleResult)

    def getExtension(self, filename):
        extension = filename.split(".")[-1]
        print(f"Extension name of file {filename} is :", extension)

    """
    8. Write a Python program to display the first and last colors from the following list.
    color_list = ["Red","Green","White" ,"Black"]
    """
    def getColor(self, list):
        first_color = list[0]
        last_color = list[-1]
        print("First Color: ", first_color ,"\nLast Color: ", last_color)

    """
    9. Write a Python program to display the examination schedule. (extract the date from exam_st_date)
    exam_st_date = (11, 12, 2014)
    """
    # def examDate(self,commaSeparatedDate):
        # print(commaSeparatedDate.split(", ").join("/"))

