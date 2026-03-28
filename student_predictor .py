#Student Pass/Fail Predictor

def predict_pass_fail(hours, attendance):

    #Simple rules (AI logic)
    if hours >= 3 and attendance >= 75:
       return "PASS"
    else:
        return "FAIL"
    
#User input loop
while True:
    print("\n--- Student Predictor ---")

    hours = float(input("Enter study hours per day:"))
    attendance = float(input("Enter attendance percentage:"))

    result = predict_pass_fail(hours, attendance)

    print("Result:", result)

    choice = input("Check another? (yes/no):")
    if choice.lower() != "yes":
          break
