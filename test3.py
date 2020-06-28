name = "Anyla"
print(name)
name = list(name)
print(name)
name[1] = input("Put a letter: ")
name = ".".join(name).upper()
print(name)
print("")
message = "hey there :)"
for i in range (1,10):
    message = message.swapcase()
    print(message)

 # this will make all inputs in uppercase

userInput = input("Please input a lowercase word: ")

print(userInput.upper())

# Odd or even number?

number = int(input("Please put a number: "))

number = number%2

if number == 0:
    print("%i IS EVEN" %number)
    
if number > 0:
    print("%i IS ODD" %number)
