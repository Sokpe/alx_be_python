Task= input("Describe Your task for today: ").lower()
Priority= input("What is the priority of this task? (high, medium, low): ").lower()
Time_bound=input("Is this task time-bound? (yes or no): ").lower()
match Priority:
      
    case "high":
        print(f"Your task: {Task} is of high priority.")
    case "medium":
        print(f"Your task: {Task} is of medium priority.")
    case "low":
        print(f"Your task: {Task} is of low priority.")
        
        if Time_bound == "yes":
            print("Make sure to complete it soon.")

    