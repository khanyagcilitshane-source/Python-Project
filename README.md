# Python-Project
# Python Mini Toolkit

## Project Description
Python Mini Toolkit is a beginner-friendly Python project that combines multiple mini applications into one menu-driven program. The program allows users to calculate grades, check whether a number is even or odd, play a number guessing game, and create a simple study planner.

The project was created using a single Python file because the main program did not require helper files or additional modules besides Python’s built-in `random` module.

---

## Features
- Grade Calculator
- Even or Odd Checker
- Number Guessing Game
- Study Planner
- Menu-driven interface
- User input validation
- Error handling using `try` and `except`

---

## Python Concepts Used
This project uses several important beginner Python concepts, including:

- Variables
- Data types (`int`, `float`, `string`, `boolean`)
- Conditional statements (`if`, `elif`, `else`)
- Loops (`while`, `for`)
- Functions (`print()`, `input()`, `round()`)
- Exception handling (`try` and `except`)
- Operators (`%`, `>`, `<`, `==`)
- Boolean logic (`and`, `or`, `not`)
- Random module (`random.randint()`)

---

## Code Explanation
The program starts by importing the `random` module, which is used in the Number Guessing Game to generate a random number between 1 and 10.

A `while True` loop is used to keep the menu running until the user chooses the Exit option. Inside the loop, the menu options are displayed using `print()` statements, and the user selects an option using the `input()` function.

### Grade Calculator
The Grade Calculator asks the user to enter a score between 0 and 100. The program uses `if`, `elif`, and `else` statements to determine the correct grade:
- 90 and above = A
- 80–89 = B
- 70–79 = C
- 60–69 = D
- Below 60 = F

The program also uses `try` and `except` to prevent crashes if the user enters invalid input.

### Even or Odd Checker
This feature asks the user for a whole number and checks whether it is even or odd using the modulus operator `%`.

Example:
```python
number % 2 == 0
```

If the remainder is 0, the number is even. Otherwise, it is odd.

### Number Guessing Game
The Number Guessing Game uses:

```python
random.randint(1, 10)
```

to generate a random secret number between 1 and 10.

The user has 3 attempts to guess the correct number. A `for` loop controls the attempts, while conditional statements check if the guess is:
- correct,
- too high,
- or too low.

A Boolean variable called `guessed` is used to track whether the player wins or loses.

### Study Planner
The Study Planner asks the user:
- how many subjects they have,
- and how many study hours are available.

The program divides the hours equally among the subjects using:

```python
hours / subjects
```

The `round()` function is used to keep the answer to 2 decimal places.

### Exit Option
The Exit option uses:

```python
break
```

to stop the infinite `while True` loop and end the program.

---

## How to Run the Project

1. Make sure Python is installed on your computer.
2. Save the Python file.
3. Open a terminal or command prompt.
4. Navigate to the folder where the file is saved.
5. Run the program using:

```bash
python filename.py
```

Replace `filename.py` with the actual name of your Python file.

---

## Challenges I Faced
One challenge I faced during this project was deciding how to structure my code. At first, I wanted to use `def` functions for each feature, but I found it complicated as a beginner. Later, I changed my approach and used one main file with conditional statements and loops instead.

Another challenge was understanding how loops and error handling worked together, especially when validating user input.

---

## What I Learned
Through this project, I learned:
- How to create a menu-driven Python application
- How loops keep a program running
- How conditional statements control program flow
- How to handle invalid user input using `try` and `except`
- How to use the `random` module
- How to make programs more user-friendly

---

## Future Improvements
In the future, I would like to:
- Add more mini tools and games
- Improve the design of the menu
- Use functions (`def`) to make the code cleaner
- Save user data using files
- Add score tracking for the guessing game

---

## Author
**Khanya Gcilitshane**
