from add_task import  add_task
from edit_task import  edit_task
from remove_task import  remove_task
from view_list import  view_list
from sort_by import sort_by
from save_list import save_list
from get_date import get_date

import sys

task_list = []

run = True
while run:
    try:
        choice = int(input("Would you like to: "
                           + "1) Add a task     2) Edit a task"
                           + "2) Remove a task      4) View all tasks"
                           + "5) Sort the task list     6) Quit"
                           )
                     )
    except:
        print("Invalid input, please try again")
        continue

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
            edit_task()
        case 3:
            remove_task()
        case 4:
            view_list()
        case 5:
            sort_by()
        case 6:
            run = False
            sys.exit()

    save_list()