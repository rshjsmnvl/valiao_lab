"""
- Ask the user to enter their BMI
- If the input BMI is less than or equal to 0, print "Invalid Input"
- If the input BMI less than 18.5, print "Category: Underweight"
- If the input BMI is less than 25, print "Category: Normal Weight"
- If the input BMI is less than 30, print "Category: Overweight"
- If the input BMI is 30 and above, print "Category: Obese"
"""

bmi = float(input("Enter your BMI: "))

if bmi <= 0:
    print("Invalid Input")
else:
    if bmi < 18.5:
        print("Category: Underweight")
    else:
        if bmi < 25.0:
            print("Category: Normal Weight")
        else:
            if bmi < 30:
                print("Category: Overweight")
            else:
                if bmi >= 30:
                    print("Category: Obese")