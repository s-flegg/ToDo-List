def save_list(filename, task_list):
    with open(filename, "w") as f:
        f.write(task_list)