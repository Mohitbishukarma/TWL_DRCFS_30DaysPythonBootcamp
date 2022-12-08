# Dictionaries 

# dictionary declearing
cmds = {
    "start":"start the program",
    "pause":"pause the program",
    "stop":"stop the program",
}
# accessing data
print(cmds["start"])

print(cmds.get("stop"))

# updating the dictionary

cmds["start"] = "starting the program"
print(cmds.get("start"))

# dictionary methods
# .items()

cmds_list = cmds.items()
print(cmds_list)

for cmd in cmds_list:
    print(f"Username : {cmd[0]}, Password : {cmd[1]}")


# .clear() ---> clares all the key-value pairs in the dictionary.
# cmds.clear()
print(cmds)

# .keys() ---> returns the list of all keys in given dictionary
cmds_keys_list = cmds.keys()
print(cmds_keys_list)

# .values() ---> returns the list of all the values in the dictionary
cmds_values_list = cmds.values()
print(cmds_values_list)

# 
cmds.update("Mohit BK")
print(cmds)


# Log in system using dictionary
users = {
    "Mohit BK":"mohit123",
    "Hari KC":"hari123",
    "Syam Thakuri":"syam123",
}

username = input("Enter your username: ")
password = input("Enter your password: ")

if users.get(username) is None:
    print("username does not exist.")
elif users[username] == password:
    print("Welcome "+username)
else:
    print("Incorrect Password")

# Log in system using dictionary
users = {
    "Mohit BK":"mohit123",
    "Hari KC":"hari123",
    "Syam Thakuri":"syam123",
}

username = input("Enter your username: ")
password = input("Enter your password: ")

if users.get(username) is None:
    print("username does not exist.")
elif users[username] == password:
    print("Welcome "+username)
else:
    print("Incorrect Password")



