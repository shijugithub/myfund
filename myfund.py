#!/usr/bin/python

def theFile():
   print("You have entered theFile function")
   fileSelection = raw_input("Enter the file location : ")
   print("The file you have selected is : " + str(fileSelection))
   theFile = open(fileSelection)
   theFileLines = theFile.readline()
   firstLine = theFileLines

   theHeaders = firstLine.split(",")
   for heading in theHeaders:
      print(heading)

   while theFileLines:
      #print(theFileLines)
      #print("*********")
      theFileLines=theFile.readline()
   theFile.close()

theFile()
