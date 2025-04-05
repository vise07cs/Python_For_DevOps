# students = [
#   {
#     'name': "John",
#     'age': 20,
#     'grade': "A",
#     'subjects': ["Math", "Science", "English"],
#     'address': {
#       'street': "123 Main St",
#       'city': "New York",
#       'state': "NY"
#     }
#   },
#   {
#     'name': "Alice",
#     'age': 22,
#     'grade': "B",
#     'subjects': ["History", "Math", "Art"],
#     'address': {
#       'street': "456 Elm St",
#       'city': "Los Angeles",
#       'state': "CA"
#     }
#   }, 
#   {
#     'name': "Bob",
#     'age': 21,
#     'grade': "C",
#     'subjects': ["Science", "English", "PE"],
#     'address': {
#       'street': "789 Oak St",
#       'city': "Chicago",
#       'state': "IL"
#     }
#   }
# ]

# print(students[0]['name'])  # Accessing the name of the first student



ec2_instances = [
  
    {'instance1': {'id': 'i-1234567890abcdef0', 'type': 't2.micro', 'status': 'running'}},
    {'instance2': {'id': 'i-0987654321fedcba0', 'type': 't2.small', 'status': 'stopped'}},
   
    {'instance3': {'id': 'i-1122334455667788', 'type': 't2.medium', 'status': 'running'}}
  
]
print(ec2_instances[0])  # Accessing the ID of the first EC2 instance


print(len(ec2_instances))  # Accessing the ID of the first EC2 instance

print(ec2_instances[1]['instance2']['type'])  # Accessing the ID of the second EC2 instance

# the above code defines a list of dictionaries representing EC2 instances, each with an ID, type, and status. It then prints the first instance's details. You can access other instances similarly by changing the index in the list.

# The code is useful for managing and retrieving information about EC2 instances in AWS. You can extend it to perform actions like starting, stopping, or terminating instances using the AWS SDK for Python (Boto3).





# sets in python
# Sets are unordered collections of unique elements. They are useful for storing and manipulating data without duplicates. Here's an example of how to create and use sets in Python:
  
# # Creating a set
my_set = {1, 2, 3, 4, 5}
print("Original set:", my_set)
my_set.add(6)  # Adding an element
print("Set after adding 6:", my_set)    

my_set.add(4)  # Adding an element
print("Set after adding 4:", my_set)     #same element will not be added again

#usecase--> to store s3 bucket names in a set to avoid duplicates