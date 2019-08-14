#!/usr/bin/python

class Investment:
   def __init__(self, BANK, DESCRIPTION, BRANCH, ACCOUNT_No, DEP_DATE, DEP_AMT, Mat_Dt, CURRENCY, TYPE, INT, Mat_Amt):
      self.theACno = ACCOUNT_No
      self.BANK = BANK
      self.DESCRIPTION = DESCRIPTION
      self.BRANCH = BRANCH
      self.ACCOUNT_No = ACCOUNT_No
      self.DEP_DATE = DEP_DATE
      self.DEP_AMT = DEP_AMT
      self.Mat_Dt = Mat_Dt
      self.CURRENCY =CURRENCY
      self.TYPE = TYPE
      self.INT = INT
      self.Mat_Amt =Mat_Amt

   def printAccount(self):
      print("The account number is : " + str(self.ACCOUNT_No))

   def printBank(self):
      print("The account number is : " + str(self.BANK))

   def printDepAmt(self):
      print("The account number is : " + str(self.DEP_AMT))
