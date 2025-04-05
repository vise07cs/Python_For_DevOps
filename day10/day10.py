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


# # The above code takes a list of folder paths as input from the user, converts it to a list, and then iterates over each folder path. It attempts to list the files in each folder using os.listdir(). If the folder is not found or if there are permission issues, it prints an error message.
# # The code handles exceptions using try-except blocks to catch FileNotFoundError and PermissionError. This way, the program continues to run even if one of the folder paths is invalid or inaccessible.
# # The code is useful for checking the contents of multiple folders and handling errors gracefully.

# excepion handling in python

# exception handling is a way to handle errors or exceptions that may occur during the execution of a program. In Python, you can use try-except blocks to catch and handle exceptions. Here's an example:
#
# # try:
# #     # Code that may raise an exception  
# #     result = 10 / 0  # This will raise a ZeroDivisionError
# #     print("Result:", result)  
# except ZeroDivisionError:
#     # Code to handle the exception
#     print("Error: Division by zero is not allowed.")
# except Exception as e:
#     # Code to handle any other exception
#     print("An error occurred:", str(e))
# # else:
# #     # Code that runs if no exception occurs
# #     print("No exceptions occurred.")
# # finally:
# #     # Code that always runs, regardless of exceptions
# #     print("This block always executes.")
