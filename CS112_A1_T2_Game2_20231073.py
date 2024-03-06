# File : CS112_A1_T2_Game2_20231073 
# Purpose : A scrabble game in python . Each player take a different num from 1 to 9 . if a player has picked three numbers that add up to 15, that player wins the game. 
# Author :  Salma Ashraf Hassan mostafa
# ID : 20231073 

# Initialize the list of numbers and two empty lists for each player
my_list = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]
new_list1 = []
new_list2 = []
sum_1 = 0 
sum_2 = 0  
counter_1 = 0 
counter_2 = 0 
c = True  
# Display game instructions
print("welcome to the scrabble game : ")
print ("   Each player takes turns picking a number from the list")
print("   Once a number has been picked, it cannot be picked again")
print("   If a player has picked three numbers that add up to 15, that player wins the game. ")
print("   However, if all the numbers are used and no player gets exactly 15, the game is a draw.")
while my_list != [] :
    
    while c == True and counter_1 <= 5 :
      # Player 1's turn
       
       print ("now , player_1 play ")
       while True :
        try :
            i = int(input("please choose a num 1 to 9: "))
            if 1 <= i <= 9:
                if i  in my_list :
                 break  
                else :
                  print("Number is taken before . please choose another number")
            else:
                print("Number must be between 1 and 9.")
        except :
            print("Invalid input. Please enter a valid number.")
       
       my_list . remove(i)
       new_list1 . append(i)
        # Check if Player 1 has won
       if counter_1 <= 3 :
          sum_1 = sum_1 + i
          counter_1 += 1
       if counter_1 == 4 :
          counter_1 += 1
          if (new_list1[0]+new_list1[1]+new_list1[2]==15 or new_list1[1]+new_list1[2]+new_list1[3]==15 or new_list1[0]+new_list1[3]+new_list1[2]==15 or new_list1[0]+new_list1[1]+new_list1[3]==15 ) :
               print("player_1 wins") 
               print("--END GAME--")
               c=False
       elif counter_1 == 5:
            counter_1+=1
            if (new_list1[0]+new_list1[1]+new_list1[2]==15 or new_list1[1]+new_list1[2]+new_list1[3]==15 or new_list1[0]+new_list1[3]+new_list1[2]==15 or new_list1[0]+new_list1[1]+new_list1[3]==15 or  new_list1[0]+new_list1[3]+new_list1[4]==15 or new_list1[0]+new_list1[1]+new_list1[4]==15 or new_list1[0]+new_list1[2]+new_list1[4]==15 or new_list1[2]+new_list1[1]+new_list1[4]==15 or  new_list1[1]+new_list1[3]+new_list1[4]==15 or new_list1[4]+new_list1[2]+new_list1[3]==15 ) :
                   print("player_1 wins")
                   print("--END GAME--")
                   c=False
                   
       if sum_1 == 15 and counter_1 == 3 :
           print("player_1 wins")
           print("--END GAME--")
           c = False
        
       if(c == True and counter_2 < 4):  
          print ("now we have :" , my_list)
         # Player 2's turn
          print ("now , player_2 play")
    
          while True:
            try:
               y = int(input("please choose a num 1 to 9: "))
               if 1 <= y <= 9:
                  if y in my_list :
                   break  
                  else :
                     print("Number is taken before . please choose another number")
               else:
                  print("Number must be between 1 and 9.")
            except :
               print("Invalid input . Please enter a valid number.")

          my_list . remove(y)
          new_list2 . append(y)
           # Check if Player 2 has won
          if counter_1 <= 3 :
             sum_2 = sum_2 + y
             counter_2 += 1
          else:
              counter_2 += 1
              if (new_list2[0]+new_list2[1]+new_list2[2]==15 or new_list2[1]+new_list2[2]+new_list2[3]==15 or new_list2[0]+new_list2[3]+new_list2[2]==15 or new_list2[0]+new_list2[1]+new_list2[3]==15 ) :
                print("player_2 wins")
                print("--END GAME--")
                c=False
          if sum_2 == 15 and counter_2 == 3:
            print("player_2 wins")
            print("--END GAME--")
            c = False
          elif sum_2 != 15 and counter_2 <3:

            print ("now we have : " , my_list)
      # Check for a drew 
    if (counter_1 == 5 and counter_2 == 4 ) or (counter_1 == 6) :
      if c == True :
        print("the game is drew") 
        c = False
