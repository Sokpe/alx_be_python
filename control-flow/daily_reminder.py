def get_task_details():
    task = input("Enter a task description: ")
    priority = input("Enter the task's priority (high, medium, low): ").lower()
    while priority not in ["high", "medium", "low"]:
        priority = input("Invalid priority. Please enter high, medium, or low: ").lower()

    time_bound = input("Is the task time-bound? (yes or no): ").lower()
    while time_bound not in ["yes", "no"]:
        time_bound = input("Invalid input. Please enter yes or no: ").lower()

    return task, priority, time_bound

def provide_reminder(task, priority, time_bound):
    match priority:
        case "high":
            reminder = f"You have a high-priority task: {task}"
        case "medium":
            reminder = f"You have a medium-priority task: {task}"
        case "low":
            reminder = f"You have a low-priority task: {task}"

    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    else:
        reminder += "."

    print(reminder)

def main():
    task, priority, time_bound = get_task_details()
    provide_reminder(task, priority, time_bound)

if __name__ == "__main__":
