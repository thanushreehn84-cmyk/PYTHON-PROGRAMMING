phone=input("Phone: ")
phonebook={
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four"
}
output=""
for ch in phone:
    output+=phonebook.get(ch,"!")+""
print(output)