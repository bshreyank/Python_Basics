def calculate_bmi(weight, height):
    """
    Calculates the Body Mass Index (BMI) given weight in kilograms (kg) and height in meters (m).
    """
    bmi = weight / (height ** 2)
    return bmi

def interpret_bmi(bmi):
    """
    Interprets the BMI value and provides a corresponding category.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# Example usage:
weight = float(input("Enter your weight in kilograms (kg): "))
height = float(input("Enter your height in meters (m): "))

bmi = calculate_bmi(weight, height)
category = interpret_bmi(bmi)

print("Your BMI is: {:.2f}".format(bmi))
print("Category: ", category)
