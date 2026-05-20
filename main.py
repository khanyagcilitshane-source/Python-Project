# Import the random module to generate random numbers for the guessing game
import random

# Main program loop
# The menu will keep showing until the user chooses to Exit

while True:
    # Display the main menu 
    print("\n-- Main Menu --")
    print("1. Grade Calculator") 
    print("2. Even or Odd Checker")
    print("3. Number Guessing Game")
    print("4. Study Planner")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    # Grade Calculator
    if choice == '1':
        print("\n-- Grade Calculator --")
        try:
            # Determine grade based on score
            score = float(input("Enter your score (0-100): "))
            if score >= 90:
             grade = "A"
            elif score >= 80:
             grade = "B"
            elif score >= 70:
             grade = "C"
            elif score >= 60:
             grade = "D"
            else:
             grade = "F"

            print(f"Your grade is: {grade}")
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 100.")

    # Even or Odd Checker
    elif choice == '2':
        # Check if a number is even or odd
        print("\n-- Even or Odd Checker --")
        try:
            number = int(input("Enter a number: "))
            if number % 2 == 0:
                print(f"{number} is even.")
            else:
                print(f"{number} is odd.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    # Number Guessing Game
    elif choice == '3':
        # Generate a random number between 1 and 10 and give the user 3 attempts to guess it
        print("\n-- Number Guessing Game --")
        secret = random.randint(1, 10)
        attempts = 3
        guessed = False
        print("I have selected a number between 1 and 10. You have 3 attempts to guess it.")

        for i in range(attempts):
            try:
                guess = int(input(f"Attempt {i+1}: "))
                if guess == secret:
                    print("Congratulations! You've guessed the number.")
                    guessed = True
                    break
                elif guess < secret:
                    print("Too low! Try again.")
                else:
                    print("Too high! Try again.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 10.")

        if not guessed:
            print(f"Sorry, you've used all attempts. The number was: {secret}")

    # Study Planner
    elif choice == '4':
        # Ask the user how many subjects they have and how many hours they have to study, then calculate how many hours they should spend on each subject
        print("\n-- Study Planner--")
        try:
            subjects = int(input("How many subjects? "))
            hours = float(input("How many hours do you have today? "))
            if subjects > 0 and hours > 0:
                per_subject = round(hours / subjects, 2)
                print(f"\nStudy {per_subject} hours for each subject.")
            else:
                print("Subjects and hours must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

    # Exit
    elif choice == '5':
        # Exit the program
        print("Thanks for using the main menu. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

    input("\nPress Enter to continue...")


