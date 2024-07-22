

# text-based adventure game
current_scenario="start"

while current_scenario!="end":
    if current_scenario=="start":
        print("you are at the start of your adventure \n")
        print("You see two paths ahead. Which path will you take?")
        print("1. Path of the Warrior")
        print("2. Path of the Mage")
        print("3. Quit the game")
        
        choice=input("choice any one number from 1,2,3 \n")
        if choice == "1":
             current_scenario="warrior"
            
        elif choice == '2':
           current_scenario = "mage"
           
        elif choice == '3':
           print("Quitting the game. Goodbye!")    
           exit(  )
           
        else:
           print("invalid number,plzz choice number only 1 or 2\n")
      
    if current_scenario=="warrior":
         print("You chose the Path of the Warrior.\n")
         print("You encounter a fierce dragon.")
         print("What will you do?")
         print("1. Fight the dragon")
         print("2. Flee from the dragon\n")
         
         choice==input("choice any one number from 1,2 ")
         if choice=="1":
             print("You bravely fight the dragon and emerge victorious!")
             current_scenario = "treasure"
         elif choice == '2':
             print("You run away from the dragon. Coward!")  
             current_scenario = "treasure" 
         else:
             print("Invalid choice. Please enter 1 or 2.")
    
    elif current_scenario == "mage":
         print("You chose the Path of the Mage.")
         print("You find a mysterious spellbook.")
         print("What will you do?")
         print("1. Study the spellbook")
         print("2. Ignore the spellbook and continue exploring")
        
         choice = input("Enter your choice (1-2): \n")
        
         if choice == '1':
             print("You learn powerful spells from the spellbook!\n")
             current_scenario = "treasure"
             
         elif choice == '2':
            print("You continue exploring without touching the spellbook.\n")
            current_scenario = "treasure"
            
         else:
            print("Invalid choice. Please enter 1 or 2.")
    
    elif current_scenario == "treasure":
         print("You find a hidden treasure!")
         print("Congratulations! You completed your adventure.\n")
         
         print("1 -> Exit ")
         print("2-> re-Play\n")
         choice = input("Enter your choice (1-2): \n")
         if choice == "1":
             exit( )
         else:
             current_scenario = "start"   
         
                 
print("Game over. Thanks for playing!")
        