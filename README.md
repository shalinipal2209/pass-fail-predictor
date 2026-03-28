# PROJECT TITLE
Student Pass/Fail Predictor

# PROJECT OVERVIEW
This project is a simple rule-based AI system designed to predict whether a student will pass or fail based on key factors like daily study hours and attendance percentage. It works by applying predefined logical conditions to the input provided by the user. The system acts as a basic intelligent agent that takes inputs from the environment and makes a decision accordingly. It demonstrates fundamental AI concepts such as decision-making, classification, and rule-based reasoning. The project is easy to implement, requires no external libraries, and runs instantly. It serves as a beginner-friendly example of how AI can be used to solve real-world problems in education.

# OBJECTIVES
1. To design a simple rule-based system that predicts student performance (pass/fail).

2. To apply basic AI concepts like decision-making and intelligent agents.

3. To classify outcomes based on input parameters such as study hours and attendance.

4. To demonstrate how logical rules can solve real-world problems without complex models.

5. To build an easy-to-understand and efficient system for academic performance evaluation.

# TOOLS AND TECHNOLOGIES USED
1. Python – Used as the programming language to implement the logic and build the system.
   
2. Built-in Functions – Used for input, output, and basic operations (no external libraries required).
 
3. Command Line / Terminal – Used to run and interact with the program.
 
4. Rule-Based Logic – Used to make decisions based on predefined conditions (AI concept).
 
5. Basic Text Editor / IDE (like VS Code or Notepad) – Used to write and execute the code.

# REQUIREMENTS
Hardware Requirements:
1. A computer or laptop with at least 2 GB RAM.
   
2. Processor capable of running Python (any modern CPU will work).
   
3. Keyboard and display for input and output.
   
Software Requirements:
1. Python 3.x installed on the system.
 
2. A text editor or IDE to write and run the code (e.g., VS Code, PyCharm, or even Notepad).
 
3. Command line/terminal to execute the program.
   
Functional Requirements:
1. User must be able to input study hours and attendance percentage.
 
2. System should predict “PASS” or “FAIL” based on the rules.
 
3. User should be able to run multiple predictions in one session.
   
Non-Functional Requirements:
1. The program should be simple and fast, giving instant results.
 
2. No internet or external libraries are needed.
   
3. The system should be user-friendly and easy to understand, suitable for beginners.

# ALGORITHMS
1. Start the program.
  
2. Take input from the user:
    Study hours per day
    Attendance percentage
   
3. Apply decision rules:
   If study hours ≥ 3 AND attendance ≥ 75%, then predict PASS.
   Else, predict FAIL.
   
4. Display the result (PASS or FAIL) to the user.
   
5.Ask the user if they want to enter another input.
  If yes, go back to step 2.
  If no, exit the program.

6. End.

# HOW TO RUN IT?
1. Install Python
   
    Ensure Python 3.x is installed on your computer.

    Verify installation by checking the version in Command Prompt or Terminal.

2.Create the Python File

  Open a text editor or IDE (Notepad, VS Code, PyCharm, etc.).

   Copy the program logic into a new file.

   Save the file with a .py extension (e.g., student_predictor.py).

3. Open Command Line / Terminal
   
    Navigate to the folder where the Python file is saved.
4. Run the Program
   
   Execute the Python file using the command python filename.py or python3 filename.py.
5. Enter Inputs
   
    Input the student’s study hours per day when prompted.

     Input the student’s attendance percentage when prompted.

6. View the Result
   
    The program will display whether the student will PASS or FAIL.

7. Continue or Exit
   
  Choose whether to check another student by typing yes or no.

  If yes, repeat steps 5–6; if no, the program will exit.

# CHALLENGES FACED
1. Defining accurate rules – Choosing the correct thresholds for study hours and attendance to make accurate predictions can be tricky.
   
2. Limited decision-making – Since it’s a rule-based system, it cannot adapt or learn from new data.
   
3. Handling unexpected inputs – Users might enter invalid data (like text instead of numbers), which can cause errors.
   
4. Scalability – This simple system works for small input sets, but cannot handle complex scenarios with multiple parameters.
   
5. No probabilistic reasoning – The system cannot handle uncertainty or borderline cases; it’s purely deterministic.
   
6. Lack of data-driven accuracy – Predictions are based on fixed rules, not on real historical student data, so accuracy may be limited.
