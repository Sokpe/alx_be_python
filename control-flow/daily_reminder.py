task= input("Describe Your task for today: ").lower()
priority= input("What is the priority of this task? (high, medium, low): ").lower()
time_bound=input("Is this task time-bound? (yes or no): ").lower()
match task_priority:
      
    case "high":
        print(f"Your task: {task} is of high priority.")
    case "medium":
        print(f"Your task: {task} is of medium priority.")
    case "low":
        print(f"Your task: {task} is of low priority.")
        
        if time_bound == "yes":
            print("Make sure to complete it soon.")

    
