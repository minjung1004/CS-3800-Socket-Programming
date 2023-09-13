# Ask client for their name
user_name = input("Name: ")
output = "Client of " + user_name
print(output)
# Ask client to choose number between 1 to 100
def choose_int(): 
    pick_int = input("Choose a number between 1 and 100: ")
    # change data type from str to int
    user_int = int(pick_int)
    if user_int > 0 and user_int < 101:
        print(user_int) 
    else:
        print("Error: Input interger is not between 1 and 100. Try again.")
        choose_int()

choose_int()