#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Opening Letter Format
with open("./Input/Letters/starting_letter.txt", 'r') as start:
    starting_letter = start.read()
# print(starting_letter)

# Open Name List
with open("./Input/Names/invited_names.txt", "r") as names:
    name_list = names.readlines()
# print(name_list)

# Remove \n from names in name list
new_name_list = []
for name in name_list:
    new_name_list.append(name.strip())
# print(new_name_list)

# Write customised letter for everyone in name list in Output/ReadyToSend Folder
for name in new_name_list:
    new_letter = starting_letter.replace("[name]", name)
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as letter:
        letter.write(new_letter)