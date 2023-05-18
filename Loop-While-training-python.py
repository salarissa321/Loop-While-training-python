



#------------------------------------------------
#------- Loop => While Training-----------
#----Simple Password Guess----------------
#------------------------------------------------



tries = 4

mainPassword = "Salar@123"

inputPassword = input("Write Your Password : ") # Write Your Password :

while inputPassword != mainPassword : # True

    tries -= 1 # tries = tries - 1

    print(f"Wrong Password. {tries} Chances left") # Wrong Password. 3 Chances left

    inputPassword = input("Write Your Password : ")

    if tries == 0 :
        print("All Tries Are finished")
        break
        print("Will Not Print") 

else :
    print("Correct Password")



