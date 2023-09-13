import json
# Ask client for their name
user_name = input("Name: ")
output = "Client of " + user_name
print(output)
pick_int = input("Choose a number between 1 and 100: ")
user_int = int(pick_int)

dictionary = {
        "name" : user_name,
        "integer": user_int,
}

json_object = json.dumps(dictionary, indent=4)
 
with open("sample.json", "w") as outfile:
    outfile.write(json_object)