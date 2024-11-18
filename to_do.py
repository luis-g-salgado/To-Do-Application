# Create an empty list to which a user can add tasks.
to_do_list = []


# Define 'add', 'remove', and 'load' functions that will be available menu options.
def load_list():
    """
    Loads the tasks in To-Do List
    """
    if to_do_list:
        print("Your To-Do List: ")
        count = 1
        for item in to_do_list:
            print(f"{count}: {item}")
            count += 1
    else:
            print("To-Do List is empty.")

def add_task():
    """
    Adds a task to the To-Do list
    """
    task = input("Enter the task you wish to add: ")
    to_do_list.append(task)
    print(f"'{task}' has been added to your To-Do list.")

def remove_task():
    """
    Removes a task from the To-Do list using the tasks "index number"
    """
    if not to_do_list:
        print("No tasks to delete!")
    else:
        load_list()
    try:
            index = int(input("Enter task number to delete: ")) - 1
            if 0 <= index < len(to_do_list):
                removed_task = to_do_list.pop(index)
                print(f"Task '{removed_task}' deleted!")
            else:
                print("Invalid task number!")

# Using exceptions to handle errors during user input. 
# This will show an error message if an invalid value is input.
    except ValueError:
        print("Please enter a numerical value.")
    except IndexError:
        print("Invalid index! Please try again.")


# While loop to keep the interactive menu open until User prompts "Quit" option.   
while True:
    print("\nTo-Do List:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Quit")

    choice = input("\nEnter your choice: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        load_list()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        break
    else:
        print("Invalid choice!")