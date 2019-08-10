#!/usr/bin/python

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
   print(theResult)
   print("")

def theWhileLoop():
   theValue="Good"
   while (theValue != "Exit"):
      theValue=raw_input("Enter Exit to exit: ")
      print(theValue)
      print("")


main()
theVar= "Cool it is"
print(theVar)
theAddFn(1,2)
getTheVarNadd()
theWhileLoop()

