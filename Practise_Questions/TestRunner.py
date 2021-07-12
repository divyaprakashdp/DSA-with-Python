# from Python_Basic import Questions
#
# Q = Questions()
#
# Q.areaOfCircle(1.1)
#
# Q.reverseNames("Divya", "Prakash")
# # Q.convertToTuple()
# Q.getExtension("abc.java")
# Q.getColor(["Red","Green","White" ,"Black"])
# Q.examDate(11, 12, 2014)

def printNum(number):
    if number>0:
        print(number)
        printNum(number-1)


printNum(10)
