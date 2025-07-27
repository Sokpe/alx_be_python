def add_item(shopping_list):
    item = input("Enter item name: ")
    shopping_list.append(item)
    print(f"Item '{item}' added to the list.")

def remove_item(shopping_list):
    item = input("Enter item name: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"Item '{item}' removed from the list.")
    else:
        print(f"Item '{item}' not found in the list.")

def display_list(shopping_list):
    if not shopping_list:
        print("The list is empty.")
    else:
        print("Shopping list:")
        for i, item in enumerate(shopping_list, start=1):
            print(f"{i}. {item}")

def main():
    shopping_list = []
    while True:
        print("\nShopping List Manager")
        print("1. Add item")
        print("2. Remove item")
        print("3. Display list")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice. Please enter a number.")
            continue

        if choice == 1:
            add_item(shopping_list)
        elif choice == 2:
            if not shopping_list:
                print("The list is empty. Please add some items first.")
            else:
                remove_item(shopping_list)
        elif choice == 3:
            display_list(shopping_list)
        elif choice == 4:
            print("Exiting the shopping list manager.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()

