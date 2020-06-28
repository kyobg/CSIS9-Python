while True:
    try:
        age = int(input("Enter any number to quit: "))
        if age < 0 or age > 123: # if a bad value
            continue # makes the loop resume from the beginning
            print('hi') # will never show, b/c of the continue
        else: # if it is a good value , b/w 1 to 123
            break
    except ValueError:
        print("You did not enter an integer, let's try this again")
        continue

print(ValueError)
