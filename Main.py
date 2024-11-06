from Computer_Guess import computer_guess

minimum = int(input("Please input the minimum of the range the computer will guess: "))
maximum = int(input("Please input the maximum of the range the computer will guess: "))

current_guess = computer_guess(minimum, maximum)

computer_success = False

while not computer_success:
    print("Please use H to indicate if the guess is too high. L if it's too low. C if it's correct")
    print("Is the number " + str(current_guess) + "?")
    result = input()
    result = result.upper()
    if result == "H":
        #Update the maximum range using the current guess - 1 to avoid duplicating previous guess
        maximum = current_guess - 1
        current_guess = computer_guess(minimum, maximum)
    elif result == "L":
        #Update the minimum range using the current guess + 1 to avoid duplicating previous guess
        minimum = current_guess + 1
        current_guess = computer_guess(minimum, maximum)
    elif result == "C":
        print("Yay! The computer guessed your number " + str(current_guess) + " correctly!")
        computer_success = True