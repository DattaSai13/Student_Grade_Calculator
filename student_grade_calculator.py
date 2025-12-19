# Student Grade Calculator
# Week 2: Decision Making & Loops in Python

def calculate_grade(marks):
    """
    This function takes marks as input and returns grade and message
    """
    if marks >= 90:
        return "A", "Excellent work! Keep shining! 🌟"
    elif marks >= 80:
        return "B", "Very Good! Keep it up! 👍"
    elif marks >= 70:
        return "C", "Good job! You can do even better! 🙂"
    elif marks >= 60:
        return "D", "You passed. Put in more effort next time! 💪"
    else:
        return "F", "Don't give up. Practice makes perfect! 🌱"


print("📘 Welcome to the Student Grade Calculator 📘\n")

# Taking student name
student_name = input("Enter student name: ")

# Input validation using while loop
while True:
    try:
        marks = int(input("Enter marks (0-100): "))
        if 0 <= marks <= 100:
            break
        else:
            print("❌ Invalid input! Marks must be between 0 and 100.")
    except ValueError:
        print("❌ Please enter a valid number.")

# Calculate grade
grade, message = calculate_grade(marks)

# Display result
print("\n📊 RESULT FOR", student_name.upper())
print("---------------------------")
print(f"Marks: {marks}/100")
print(f"Grade: {grade}")
print(f"Message: {message}")
print("---------------------------")
