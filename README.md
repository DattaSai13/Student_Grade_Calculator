# Student Grade Calculator – Week 2 Python Basics

## 📌 Project Overview
This project is a beginner-level Python application developed to understand
decision-making and repetition in Python programming. The program takes student
marks as input, applies grading logic, and displays the corresponding grade along
with an encouraging message.

## 🎯 Project Goals and Objectives
- Learn how to make decisions using if-elif-else statements
- Understand and use comparison operators
- Implement loops for input validation
- Create reusable code using functions
- Handle invalid inputs gracefully

## ⚙️ Setup Instructions (Step-by-Step)
1. Download and install Python from https://www.python.org
2. Verify installation by running:
   ```
   python --version
   ```
3. Download this project folder or clone the repository
4. Open a terminal or command prompt
5. Navigate to the project directory
6. Run the program using:
   ```
   python grade_calculator.py
   ```

## 🧱 Code Structure
```
Student_Grade_Calculator/
│
├── README.md                 # Project documentation
├── grade_calculator.py       # Main Python program
├── test_cases.txt            # Test cases and validation
├── screenshots/              # Output screenshots
│   └── *.png
```

## 🖼️ Visual Documentation
- Screenshots are included inside the `screenshots/` folder
- They demonstrate valid execution, invalid input handling, and grading output

## 🔧 Technical Details

### Algorithm
1. Display program title
2. Ask user to enter student name
3. Repeatedly ask for marks until valid input (0–100)
4. Calculate grade using grading rules
5. Display marks, grade, and message

### Grading Logic
- A : 90 – 100
- B : 80 – 89
- C : 70 – 79
- D : 60 – 69
- F : 0 – 59

### Functions Used
- calculate_grade(marks): Returns grade and encouraging message

### Data Structures Used
- Variables (int, string)

### Architecture
- Single-file procedural Python program
- Sequential execution with function calls

## 🧪 Testing Evidence
Refer to test_cases.txt for tested inputs and expected outputs.

## 🧠 What I Learned
- Conditional statements in Python
- Loop-based input validation
- Writing reusable functions
- Applying logic to real-world problems

## ✅ Project Status
Completed and tested successfully.
