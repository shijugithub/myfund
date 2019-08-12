#!/usr/bin/python

def theFile():
   print("You have entered theFile function")
   fileSelection = raw_input("Enter the file location : ")
   print("The file you have selected is : " + str(fileSelection))
   theFile = open(fileSelection)
   theFileLines = theFile.readline()
   firstLine = theFileLines

   theHeaders = firstLine.split(",")
   noOfHeadings = len(theHeaders)
   print("Number of headings : " + str(noOfHeadings))
   for heading in theHeaders:
      print(heading)

   while theFileLines:
      theValues = theFileLines.split(",")
      print("======")
      print("Each value in the line is as follows:")
      for eachValue in theValues:
         print(str(eachValue))

      #invDictionary = {}
      #for heading in theHeaders:
      #   invDictionary[heading] = 



      #print(theFileLines)
      #print("*********")
      theFileLines=theFile.readline()
   theFile.close()

theFile()
