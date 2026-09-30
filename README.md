The Odd-Even Calculator is a simple Python program that checks whether a number entered by the user is odd or even.

The program takes an integer as input and uses the modulus (%) operator to determine the result.

Features
Accepts user input.
Identifies whether the number is odd or even.
Displays the result clearly.
Easy to understand for beginners learning Python.
How It Works

The program divides the number by 2 and checks the remainder:

If the remainder is 0, the number is Even.
If the remainder is not 0, the number is Odd.

Example:

Input:

Enter a number: 8

Output:

8 is an Even number.

Input:

Enter a number: 7

Output:

7 is an Odd number.
Python Code
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is an Even number.")
else:
    print(num, "is an Odd number.")
