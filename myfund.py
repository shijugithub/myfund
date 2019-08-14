#!/usr/bin/python

import Investment

def main():
   #print("You have entered theFile function")
   #fileSelection = raw_input("Enter the file location : ")
   fileSelection = "/file/temp.txt"
   theFile = open(fileSelection)
   theFileLines = theFile.readline()
   firstLine = theFileLines
      
   theHeaders = firstLine.split(",")
   noOfHeadings = len(theHeaders)

   theFileLines=theFile.readline()
   listOfInvestments = []
   
   while theFileLines:
      theValues = theFileLines.split(",")
      investment = dict(zip(theHeaders, theValues))
      theAccountNo = "INV" + str(investment['ACCOUNT_No'])
      listOfInvestments.append("theAccountNo")
      
      theAccountNo =Investment.Investment(investment['BANK'], investment['DESCRIPTION'], investment['BRANCH'], investment['ACCOUNT_No'], investment['DEP_DATE'], investment['DEP_AMT'], investment['Mat_Dt'], investment['CURRENCY'], investment['TYPE'], investment['INT_%'], investment['Mat_Amt'])
      
      theAccountNo.printReport()
      theFileLines=theFile.readline()
   theFile.close()

   

main()
