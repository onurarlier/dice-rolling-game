#loop
#Ask: roll the dice?
#If user enters yes
#    Generate two random numbers between 1 and 12
#    print them
#If user enters no
#   Print thank you message
#   Terminate
#Else
#   İnvalid choice
import random
while True :
   
   choice = input("Roll the dices (yes or no): ").lower()

   
   if choice == "yes" :
      number = int(input("How many dice you want to roll: "))
      sumofdice = 0
      for i in range(number):
       dice = random.randint(1,6)
       sumofdice = sumofdice + dice
       print(f'number {dice} roll {i+1}')
      print(f'sum:{sumofdice}')



      
    

   elif choice == "no" :
    print("Thank you for playing")
    break

   else :
    print("Invalid Choice")
    continue
