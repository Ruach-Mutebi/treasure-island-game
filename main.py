print('''
                                         
                                         
            ,d                           
            88                           
,adPPYba, MM88MMM ,adPPYYba, 8b,dPPYba,  
I8[    ""   88    ""     `Y8 88P'   "Y8  
 `"Y8ba,    88    ,adPPPPP88 88          
aa    ]8I   88,   88,    ,88 88          
`"YbbdP"'   "Y888 `"8bbdP"Y8 88          
                                         
                                         
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
direction = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n')
if direction.lower() != "left":
 print("Fall into a hole, GAMEOVER")
if direction.lower() == "left":
 decide=input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n')
 if decide.lower() != "wait":
  print("Attaked by trout, GAMEOVER")
 if decide.lower() == "wait":
  color=input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")
  if color.lower() == "red":
   print("Burned By Fire, GAMEOVER")
  if color.lower() == "blue":
   print("Eaten By Beasts, GAMEOVER")
  if color.lower() == "yellow":
   print("You Win")
  else:
    print("GAMEOVER")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload