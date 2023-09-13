import json
# Ask client for their name
user_name = input("Name: ")
output = "Client of " + user_name
print(output)
pick_int = input("Choose a number between 1 and 100: ")
user_int = int(pick_int)
# Ask client to choose number between 1 to 100
# def choose_int(): 
#     pick_int = input("Choose a number between 1 and 100: ")
#     # change data type from str to int
#     user_int = int(pick_int)
#     if user_int > 0 and user_int < 101:
#         print(user_int) 
#         make_json()
       
#     else:
#         print("Error: Input interger is not between 1 and 100. Try again.")
#         choose_int()

dictionary = {
        "name" : user_name,
        "integer": user_int,
}

json_object = json.dumps(dictionary, indent=4)
 
with open("sample.json", "w") as outfile:
    outfile.write(json_object)
        
# choose_int()


