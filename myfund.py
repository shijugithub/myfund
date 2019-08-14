#!/usr/bin/python

import Investment

def main():
   #print("You have entered theFile function")
   #fileSelection = raw_input("Enter the file location : ")
   fileSelection = "/file/temp.txt"
   theFile = open(fileSelection)
   theFileLines = theFile.readline()
   firstLine = theFileLines
      
   george = Investment.Investment("BANK")

   theHeaders = firstLine.split(",")
   noOfHeadings = len(theHeaders)

   theFileLines=theFile.readline()
   listOfInvestments = []
   
   while theFileLines:
      theValues = theFileLines.split(",")
      investment = dict(zip(theHeaders, theValues))
      theAccountNo = "INV" + str(investment['ACCOUNT No'])
      listOfInvestments.append("theAccountNo")
      globals()['obj_%s' % theAccountNo] = Investment.Investment(investment['ACCOUNT No'])
      #vars()[theAccountNo] = Investment.Investment(investment['ACCOUNT No'])
      #theAccountNo.printReport()
      obj_INT_10523300008488.printReport()      
      theFileLines=theFile.readline()
   theFile.close()

   

main()
