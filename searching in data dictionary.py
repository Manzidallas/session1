
# Data dictionary which displays three students with age and their names 


students = [
    {
        "name" : "Nkiko Hertier",
        "age": 192
    },

    {
        "name" : "Manzi Seka Prince",
        "age": 2002
    },

    {
        "name" : "Niyomugabo Bosco",
        "age": 100
    }
]

name = "Manzi Seka Prince"
found = 0

for student in students:
    if student["name"] == name:
        print(f"{name} was found")
        found = 1
        break
    
if (found == 0):
    print(f"{name} was not found")

# print(student[0])

# print the first student you must pass in the variable with its index
