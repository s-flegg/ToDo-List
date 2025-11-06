def save_list(filename, task_list):
    filename = input("Enter filename, ending in .py: ")
    with open(filename, "w") as f:
        f.write(str(task_list))


