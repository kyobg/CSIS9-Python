name = "Jadon"
print(name)
name = list(name)
print(name)
let1 = input("Enter First Letter: ")
name.insert(2,let1)
print(name)

let2 = input("Enter Second Letter: ")

name.remove("o")
name.insert(4,let2)
name = ''.join(name)
print(name);
yes=1
if name == "Jayden":
    for yes in range(0,10):
        print("thats correct!")
