#!/usr/bin/python
import myfund_add

def main():
   print("You are in the main function")
   print("Hello World")
   theVar= "This is cool"
   print(theVar)
   print("")

def theAddFn(var1, var2):
   print("You entered theAddFn function")
   theResult=var1 + var2
   print(theResult)
   print("")

def getTheVarNadd():
   print("You entered getTheVarNadd function")
   var1=int(input("Enter the first integer : "))
   if(var1 == 1):
      var1=10
      print("Since 1st integer is 1, it will be changed to 10")
   print("")
   var2=int(input("Enter the secornd integer : "))
   theResult= var1 + var2
   print("The sum is : " + str(theResult))
   print("")

def theWhileLoop():
   theValue="Good"
   while (theValue != "Exit"):
      theValue=raw_input("Enter Exit to exit: ")
      print("The value you entered is : " + theValue)
      print("")

def theList():
   print("You are entering theList function")
   myList = []
   theValue = "Good"
   while (theValue != "Exit"):
      theValue = raw_input("Enter a value in the List. Enter Exit to exit : ")
      if (theValue != "Exit"):
         myList.append(theValue)
   print("The number of entries you made is : " + str(len(myList)))
   print("")
   print("The values you entered are : ")
   print(str(myList))
   print("")
   print("The values you entered are : ")
   for theList in myList:
     print(theList)

def theFile():
   print("You have entered theFile function")
   fileSelection = raw_input("Enter the file location : ")
   print("The file you have selected is : " + str(fileSelection))

#main()
theVar= "Cool it is"
print(theVar)
#theAddFn(1,2)
#getTheVarNadd()
#theWhileLoop()
#theList()
theFile()
print("The Secret is : " + str(myfund_add.theSecret()))
