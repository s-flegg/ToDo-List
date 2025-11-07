def add_task(task_list, title, description, due_date, completed, priority):
    """Add a task to the tasklist

    Parameters:
        task_list (list): The list of all tasks
        title (str): The title of the task
        description (str): The task description
        due_date (object): The datetime.datetime that the task is due
        completed (bool): True if the task is completed
        priority (int): Priority level from 1-5, 1 is the most important

    Returns:
          list: Updated task list with the new task added
    """
    task = {
        "Title": title,
        "Description": description,
        "Due Date": due_date,
        "Completed": completed,
        "Priority": priority,
    }
    task_list.append(task)
    return task_list
