"""
- Ask user to enter their age
- If the number is between 0 and 12, display a message indicating “You are a child.”
- If the number is between 13 and 19, display a message indicating “You are a teenager.”
- If the number is between 20 and 59, display a message indicating “You are an adult.”
- If the number is equal or greater than 60, display a message indicating “You are a senior citizen.”
"""

age = int(input("Enter your age: "))

if age >= 0 and age <= 12:
    print("You are a child.")
if age >= 13 and age <= 19:
    print("You are a teenager.")
if age >= 20 and age <= 59:
    print("You are an adult.")
if age >= 60:
    print("You are a senior citizen.")