weapons = ["sword", "gun", "axe", "rifle"]
zombieWeakness = weapons[0]
print("You have encountered a zombie. Prepare for battle. ")
print( "Possible weapons are: " + weapons[0] + " " + weapons[1] +  " " + weapons[2]+ " " + weapons[3] ) 
choice = input("Type 1 to choose weapon from list. Type 2 to enter your own weapon. ")
if choice == "1":
  weapon1 = input("Enter weapon name: ")
elif choice == "2":
  weapon1 = input("Enter weapon name: ")
  weapons.append(weapon1)
if weapon1 == zombieWeakness:
  print("You have won!")
else:
  print("You have lost")
print(zombieWeakness)