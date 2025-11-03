from add_task import  add_task
from edit_task import  edit_task
from remove_task import  remove_task
from view_list import  view_list
from sort_by import sort_by
from save_list import save_list
from load_list import load_list
from get_date import get_date

import sys

def main():

    task_list = load_list()

    run = True
    while run:
        try:
            choice = int(input("Would you like to: "
                               + "\n1) Add a task     2) Edit a task"
                               + "\n2) Remove a task      4) View all tasks"
                               + "\n5) Sort the task list     6) Quit"
                               + "\n: "
                               )
                         )
        except:
            print("Invalid input, please try again")
            continue

        try:
            match choice:
                case 1:
                    add_task(
                        task_list,
                        input("Enter the title of the task: "),
                        input("Enter the description of the task: "),
                        get_date(),
                        int(input("Please enter the priority level as a number 1-5: "))
                    )
                case 2:

                    task = input("Please enter the name of the task to be edited: ")

                    due_date = input("Do you want to change the due date (Y/n): ")
                    if due_date == "Y":
                        due_date = get_date()
                    else:
                        due_date = ""

                    print("For the following, please enter nothing if you wish for them to remain unchanged.")
                    new_title = input("What do you want the new title to be? ")
                    description = input("What do you want the new description to be? ")

                    completed = input("Is the task completed? (Y/n) ")
                    if completed == "Y":
                        completed = True
                    elif completed != "": # will not trigger is user wants it to remain unchanged
                        completed = False

                    priority = int(input("What priority level is the task? 1-5 "))

                    # used to remove anything the user doesn't want to change
                    kwargs = {
                        "new_title": new_title,
                        "description": description,
                        "due_date": due_date,
                        "completed": completed,
                        "priority": priority,
                    }
                    kwargs = {k:v for k,v in kwargs.items() if v != ""}

                    edit_task(**kwargs)

                case 3:
                    remove_task()
                case 4:
                    view_list()
                case 5:
                    sort_by()
                case 6:
                    run = False
                    sys.exit()
        except:
            print("Oops, something went wrong. Please try again and ensure all your inputs are correct.")

        save_list()


main()