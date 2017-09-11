# CSC 221
# M1T1
# Michael J. Campbell
# 11 Sept 2017
"""
Created on Sun Sep 10 20:21:00 2017

@author: mcamp004
"""


    

print ("Welcome to Mark V Addinator")
print ("Make A Selection: A) ADD  B) ADD MORE  C) GAME")
d1a= input ("A) ADD  B) ADD MORE  C) GAME [A/B/C]: ")
if d1a == "A": 
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
  
sum = float(number1) + float(number2)
print('The sum of {0} and {1} is {2}'.format(number1, + number2, sum))
if d1a == "B":
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    number3 = float(input("Enter the third number: "))
    number4 = float(input("Enter the fourth number: ")) 
    sum = float(number1) + float(number2) + float(number3) + float(number4)
    print('The sum of {0} and {1} is {2}'.format(number1, + number2, + number3, + number4, sum))
if d1a == "C":
  print ("This Feature Is Available To Preorder Customers Only." )

print (" Do you want to Continue")
d1a= input ("Y = Yes   N = No")
if d1a == "Y": 
 print ("Restart Program")
if d1a == "N":
 print ("Thank you for using the Mark V Addinator! Be Sure to Preorder The Mark VI At The Mathshop Today!")
