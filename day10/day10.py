import os
# # Taking user input and storing it in the variable 'number'

# number = (input("Enter a number: "))

# print("The number is: ", number)
# print("The type of the number is: ", type(number))

# # Converting the string to an integer
# number = int(number)
# print("The number is: ", number)
# print("The type of the number is: ", type(number))


folders=input("Enter a list of folder paths separated by spaces: ")
print(folders)
# Taking user input and storing it in the variable 'folders'

converted_folders = folders.split()
# converting the string to a list
# using the split() method
print(converted_folders)
print(type(converted_folders))


for f in converted_folders:  # Iterate over the list of folder paths
    try:
        files = os.listdir(f)
        print(f"Files in {f}: {files}")
    except FileNotFoundError:
        print(f"Error: Folder '{f}' not found.")
    except PermissionError:
        print(f"Error: Permission denied for folder '{f}'.")